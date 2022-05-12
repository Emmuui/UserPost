from django.urls import path
from userauth import views

urlpatterns = [
    path('userprofile/', views.UserViewSet.as_view({'get': 'list'})),
    path('userprofile/<int:pk>', views.UserViewSet.as_view({'get': 'retrieve'})),
    path('publication_list/', views.PublicationView.as_view()),
    path('followers/', views.FollowerView.as_view())
]
