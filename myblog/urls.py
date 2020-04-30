from django.urls import path
from . import views

urlpatterns=[
    path('',views.bloghome.as_view(),name='bloghome'),
    path('post/<int:pk>/',views.detailpost.as_view(),name='detail'),
     path('create/new/',views.createpost.as_view(),name='create'),
     path('post/<int:pk>/update/',views.updatepost.as_view(),name='update'),
      path('post/<int:pk>/delete/',views.deletepost.as_view(),name='delete'),
      path('user/<str:username>',views.userposts.as_view(), name='userposts')
]