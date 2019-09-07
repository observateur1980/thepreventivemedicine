
from django.urls import path
from  . import views


app_name = 'blog'
urlpatterns = [
    
    
    path('', views.Index.as_view(), name='index'),
    path('post-detail/<int:id>', views.Post_Detail.as_view(), name='post-detail'),
    path('by_cat_post_list/<int:cat_id>', views.By_Cat_Post_List.as_view(), name='by_cat_post_list'),
    

]

