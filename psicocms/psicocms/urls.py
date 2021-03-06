from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from django.contrib import admin

from zinnia.views.channels import EntryChannel

admin.autodiscover()

admin.site.login = login_required(admin.site.login)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
#    url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),

    url(r'^accounts/login/$', 'django_cas_ng.views.login', name='cms_login'),
    url(r'^accounts/logout/$', 'django_cas_ng.views.logout', name='cms_logout'),
    
    url(r'^admin_tools/', include('admin_tools.urls')),

    url(r'^psicologi/$', EntryChannel.as_view(query='category:psicologi')), 
    url(r'^psichiatri/$', EntryChannel.as_view(query='category:psichiatri')),    

    url(r'^psicologi-forensi/$', EntryChannel.as_view(query='category:psicologi_forensi')), 
    url(r'^psicologi-clinici/$', EntryChannel.as_view(query='category:psicologi_clinici')),    
    url(r'^psicologi_del_lavoro/$', EntryChannel.as_view(query='category:psicologi_del_lavoro')),    


    url(r'', include('zinnia.urls', namespace='zinnia')),

    
)

from zinnia.sitemaps import TagSitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import AuthorSitemap

sitemaps = {'tags': TagSitemap,
            'blog': EntrySitemap,
            'authors': AuthorSitemap,
            'categories': CategorySitemap,}

urlpatterns += patterns(
    'django.contrib.sitemaps.views',
    url(r'^sitemap.xml$', 'index',
        {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', 'sitemap',
        {'sitemaps': sitemaps}),)


