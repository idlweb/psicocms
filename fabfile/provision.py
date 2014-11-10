from fabric.api import cd, env, execute, hide, lcd, require, put, roles, run, settings, sudo, task
from fabric.utils import fastprint, warn
from fabric.contrib import files

import os

@task
def check_requirements():
    """
    Check if OS-level requirements are satisfied. 
    """
    raise NotImplementedError


def is_installed_package(pkg_name):
    """
    If package ``pkg_name`` has already been installed on the the target OS,    
    returns ``True``, ``False`` otherwise.
    """
    result = ""
    with hide('running', 'stdout', 'stderr'):
        with settings(warn_only=True):
            result = run("dpkg-query -W -f='${Status}' %s" % pkg_name)
    if result == 'install ok installed':
        return True
    else:
        return False
        

def install_package(pkg_name):
    """
    Install a software package -- via APT -- on the target OS.
    
    Do nothing if the requested package is already installed 
    on the the target OS.
    
    Arguments:
    
    * ``pkg_name``: the name of the package to be installed.
    """
    with hide('commands'):
        if not is_installed_package(pkg_name):    
            sudo('apt-get install --yes %s' % pkg_name)


@task
@roles('admin')          
def install_system_requirements():
    """
    Install generic OS-level software
    """    
    fastprint("Installing generic software requirements...", show_prefix=True, end='\n')
    with hide('commands'):
        for pkg_name in env.provision_packages:
            fastprint("* %s" % pkg_name, end='\n')
            install_package(pkg_name)       
        
    
@task
@roles('admin')          
def create_system_user(username, home_dir=None, enable_passwd=False):
    """
    Create an OS-level user account.
    
    Arguments:
    
    * ``home_dir``: specify a home directory for the user (defaults to ``/home/<username>``)
    * ``enable_passwd``: specify if password-based logins are allowed or not (default to ``False``)   
    """
    fastprint("Creating user `%s'..." % username, show_prefix=True)
    with hide('commands', 'warnings'):
        with settings(warn_only=True):
            cmd = ['adduser']
            if home_dir is not None:
                cmd += ['--home %s' % home_dir]
            if not enable_passwd:
                cmd += ['--disabled-password']
            # set (empty) finger information, so no user input is required 
            cmd += ['--gecos', ',,,'] 
            cmd += [username]
            run(' '.join(cmd))      
    fastprint(" done." % env, end='\n')
        

@task
@roles('admin')          
def setup_web_user():
    """
    Create a passwordless account for ``WEB_USER`` on the remote machine(s).
    """
    require('web_user', 'web_root', 'web_user_hostkey', 
            provided_by=('staging', 'production'))
    with hide('commands'):
        # create system user
        create_system_user(env.web_user, home_dir=env.web_root)
        fastprint("Adding SSH key for user `%(web_user)s'..." % env, show_prefix=True)
        # copy SSH keyfile to a temporary remote location
        source = env.web_user_hostkey 
        tmpfile = '/tmp/id_rsa.pub'
        put(source, tmpfile, mode=0644)
        # create a ``.ssh/authorized_keys`` file, if not already existing
        run('mkdir -p %(web_root)s/.ssh' % env)
        auth_keys = os.path.join(env.web_root, '.ssh', 'authorized_keys') 
        run('touch %s' % auth_keys)
        # add the new key to the "authorized" ones
        run('cat %s >> %s' % (tmpfile, auth_keys))
        # adjust filesystem permissions
        run('chown -R %(web_user)s:%(web_user)s %(web_root)s' % env)
        fastprint(" done." % env, end='\n')
        


@task
@roles('admin')          
def setup_instance_user():
    """
    Create a passwordless account for ``WEB_USER`` on the remote machine(s).
    """
    require('web_user', 'domain_root', 'web_user_hostkey', 
           provided_by=('staging', 'production'))
    with hide('commands'):
        # create system user
        create_system_user(env.web_user, home_dir=env.domain_root)
        fastprint("Adding SSH key for user `%(web_user)s'..." % env, show_prefix=True)
        # ensure that ``WEB_USER``'s home directory actually exists
        # needed if ``create_system_user()`` fails (e.g. because ``WEB_USER`` already exists)
        run('mkdir -p %(domain_root)s' % env)
        # copy SSH keyfile to a temporary remote location
        source = env.web_user_hostkey 
        tmpfile = '/tmp/id_rsa.pub'
        put(source, tmpfile, mode=0644)
        with cd(env.domain_root):
            # create a ``.ssh/authorized_keys`` file, if not already existing
            run('mkdir -p .ssh' % env)
            auth_keys = os.path.join('.ssh', 'authorized_keys') 
            run('touch %s' % auth_keys)
            # add the new key to the "authorized" ones
            run('cat %s >> %s' % (tmpfile, auth_keys))
        # adjust filesystem permissions
        run('chown -R %(web_user)s:%(web_user)s %(domain_root)s' % env)
        fastprint(" done." % env, end='\n')


@task
@roles('web')        
def setup_postgres():
    """
    Perform PostgreSQL-related provisioning tasks on the target OS.
    """
    require('local_repo_root', 'postgres_conf_dir',  
            provided_by=('staging', 'production'))
    # install DEB package for PostgreSQL 
    install_package('postgresql')
    # upload conf files
    with hide('commands'):       
        with lcd(os.path.join(env.local_repo_root, 'postgres')):
            with cd(os.path.join(env.postgres_conf_dir)):
                fastprint("Updating `postgresql.conf'...", show_prefix=True)
                put('postgresql.conf', 'postgresql.conf' , mode=0644, use_sudo=True)
                sudo('chown postgres:postgres %(postgres_conf_dir)s/postgresql.conf' % env)
                fastprint(" done." % env, end='\n')
                fastprint("Updating `pg_hba.conf'...", show_prefix=True)
                put('pg_hba.conf', 'pg_hba.conf', use_sudo=True)
                sudo('chmod 0640 %(postgres_conf_dir)s/pg_hba.conf' % env)
                sudo('chown postgres:postgres %(postgres_conf_dir)s/pg_hba.conf' % env)
                fastprint(" done." % env, end='\n')
    execute(restart_postgres)
    
    
@task
@roles('admin')
def restart_postgres():
    """
    Restart PostgreSQL database server.
    """
    require('postgres_controller', provided_by=('staging', 'production'))
    fastprint("Restarting Postgres...", show_prefix=True)
    with hide('commands'):
        sudo('%(postgres_controller)s restart' % env)
    fastprint(" done." % env, end='\n')
