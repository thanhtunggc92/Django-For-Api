from django.urls import path
from . import views

urlpatterns=[
    path('',views.PostListView, name= 'Postoverview'),
    path('detail/<str:pk>/',views.PostDetail, name= 'Post-detail'),
    path('create/',views.PostCreate, name= 'Post-create'),
    path('update/<str:pk>/',views.PostUpdate, name= 'Post-update'),
    path('delete/<str:pk>/',views.PostDelete, name= 'Post-delete'),
]