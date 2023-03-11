from django.urls import path

from main import views

app_name = 'api'

urlpatterns = [
    path('', views.companies_view, name="view_employee"),
    path('add-employee/', views.add_employee_view, name='add_employee'),
]
