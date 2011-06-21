from django.conf.urls.defaults import patterns, url

from polls import views

urlpatterns = patterns('',

    url(
        regex=r'^$',
        view=views.poll_index,
        name='poll_index',
    ),

    url(
        regex=r'^(?P<poll_id>\d+)/$',
        view=views.poll_detail,
        name='poll_detail',
    ),
    
    # DON'T DO THIS!!!
    # This is a tuple and hence takes moar smartz to read
    # I call this 'baby obfuscated code'
    #(r'^blarg/$', views.poll_detail, "poll_detail")
    
    # DON'T DO THIS!!!
    # This is less explicit view call and Django has to do 'magic' to make it work
    # This means your stacktrace for generated bugs is longer
    # I call this 'making your code harder to debug'
    #url(
    #    regex=r'^(?P<poll_id>\d+)/$',
    #    view="polls.views.poll_detail",
    #    name='poll_detail',
    #),
    
)

