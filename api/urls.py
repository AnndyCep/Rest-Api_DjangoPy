from django.urls import path
from .views import companiaView

urlpatterns = [
    path('companias/', companiaView.as_view(), name = "compania_list")
]

