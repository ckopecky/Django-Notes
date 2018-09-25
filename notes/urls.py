from django.urls import path

from . import views
app_name = 'notes'

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.view_all_notes, name='view_all_notes'),
    path('<str:note_id>/', views.detailnote, name='detailnote'),
]