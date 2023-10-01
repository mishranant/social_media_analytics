from django.urls import path
from . import views

app_name='posts'

urlpatterns = [
    path('', views.create, name='create'),
    path('<uuid:post_id>/analysis', views.analysis, name='analysis')
]
