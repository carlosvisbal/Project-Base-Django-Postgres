from rest_framework.routers import DefaultRouter
from apps.posts.api.views import PostModelViewset

router_post = DefaultRouter()
router_post.register(prefix='posts', basename='post', viewset=PostModelViewset)
