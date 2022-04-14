from django.urls import URLPattern, path
# from .views import PostList, PostDetail, UserDetail, UserList
from rest_framework.routers import SimpleRouter
from .views import UserViewset, PostViewset

# urlpatterns = [
#     path('users/', UserList.as_view()), 
#     path('users/<int:pk>/', UserDetail.as_view()), 
#     path('<int:pk>', PostDetail.as_view()),
#     path('', PostList.as_view())
# ]

router = SimpleRouter()
router.register('users', UserViewset, basename='users')
router.register('',PostViewset, basename='posts')


urlpatterns =  router.urls