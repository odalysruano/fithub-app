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
    path('accounts/signup/', views.signup, name='signup'),
]
