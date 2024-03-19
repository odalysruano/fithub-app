from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('routines/', views.routines_index, name='index'),
    path('routines/<int:routine_id>/', views.routines_detail, name='detail'),
    path('routines/create/', views.RoutineCreate.as_view(), name='routines_create'),
    path('routines/<int:pk>/update/', views.RoutineUpdate.as_view(), name='routines_update'),
    path('routines/<int:pk>/delete/', views.RoutineDelete.as_view(), name='routines_delete'),
    path('routines/<int:routine_id>/add_exercise/', views.add_exercise, name='add_exercise'),
    path('equipment/', views.EquipmentList.as_view(), name='equipment_index'),
    path('equipment/<int:pk>/', views.EquipmentDetail.as_view(), name='equipment_detail'),
    path('equipment/create/', views.EquipmentCreate.as_view(), name='equipment_create'),
    path('equipment/<int:pk>/update/', views.EquipmentUpdate.as_view(), name='equipment_update'),
    path('equipment/<int:pk>/delete/', views.EquipmentDelete.as_view(), name='equipment_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
