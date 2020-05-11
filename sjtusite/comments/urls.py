from django.urls import path

from . import views

app_name = 'comments'
urlpatterns = [
    path('comment/<int:shop_pk>', views.comment, name='comment'),
]
