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
    path('routines/<int:routine_id>/assoc_equipment/<int:equipment_id>/', views.assoc_equipment, name='assoc_equipment'),
    path('routines/<int:routine_id>/unassoc_equipment/<int:equipment_id>/', views.unassoc_equipment, name='unassoc_equipment'),
    path('equipments/', views.EquipmentList.as_view(), name='equipments_index'),
    path('equipments/<int:pk>/', views.EquipmentDetail.as_view(), name='equipments_detail'),
    path('equipments/create/', views.EquipmentCreate.as_view(), name='equipments_create'),
    path('equipments/<int:pk>/update/', views.EquipmentUpdate.as_view(), name='equipments_update'),
    path('equipments/<int:pk>/delete/', views.EquipmentDelete.as_view(), name='equipments_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
