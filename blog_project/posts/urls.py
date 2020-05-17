from django.urls import path
from rest_framework.routers import SimpleRouter
#from .views import UserViewSet, PostViewSet
from .views import PostList, PostDetail, UserList, UserDetail #FOR REGULAR VIEWS

# USING REGULARS URLS
urlpatterns = [
    path('users/', UserList.as_view()), # new
    path('users/<int:pk>/', UserDetail.as_view()), # new
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
]

# USING ROUTERS (SIMPLE ROUTER)
#router = SimpleRouter()

#router.register('users', UserViewSet, basename='users')
#router.register('', PostViewSet, basename='posts')

#urlpatterns = router.urls