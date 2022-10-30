from django.urls import path, include
from .views import home, notes

urlpatterns = [
    path('home/', home, name='home'),
    path('notes/', notes, name='notes'),
    path('notes/<int:pk>', notes, name='note_details'),
]
