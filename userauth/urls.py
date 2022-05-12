from django.urls import path

from . import views


urlpatterns = [
    path('email/', views.send_email_to_all_user_view, name='send_email'),
]
