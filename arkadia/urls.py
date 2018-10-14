from django.urls import path

from . import views

app_name = 'arkadia'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /arkadia/5/
    path('<int:property_id>/', views.detail, name='detail'),
     # ex: /arkadia/5/results/
    path('<int:property_id>/results/', views.results, name='results')
]