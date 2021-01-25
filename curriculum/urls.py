from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('<str:dni>/', views.showCurriculum, name='curriculum-page')
]
