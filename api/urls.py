from django.urls import path
from .import views
 
from .views import PostList,PostDetail


#  urlpatterns = [
#     path('/', StatusAPIView.as_view()),
#     path('create/', StatusCreateAPIView.as_view()),

app_name='api'

urlpatterns = [
    # path('',views.home,name='home'),
    path('postList/',PostList.as_view()),
    path('postDetail/<int:pk>',PostDetail.as_view()),
    
   
]
