from django.urls import re_path as url
from . import views


urlpatterns = [
    url(
        r'^posts/(?P<pk>[0-9]+)/$',
        views.get_delete_put_posts,
        name='get_delete_put_posts'
    ),
    url(
        r'^posts/$',
        views.get_post_posts,
        name='get_post_posts'
    )
]