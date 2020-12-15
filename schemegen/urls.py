from django.urls import path

from schemegen import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adhaar', views.adhaar, name='adhaar'),
    path('requirements', views.requirements, name='requirements'),
    path('detail', views.detail, name='detail'),
    path('adhaar-hindi', views.adhaar_hindi, name='adhaar_hindi'),
path('requirements-hindi', views.requirements_hindi, name='requirements-hindi'),
]