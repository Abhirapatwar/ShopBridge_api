from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('entriesapi/', views.Entriesapi),
    path('entriesapi/<int:pk>', views.Entries1api),
]
