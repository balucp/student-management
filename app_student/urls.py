from django.urls import path
from app_student import views

urlpatterns = [
    path('teacher/', views.TeacherAPI.as_view()),
    path('student/', views.StudentAPI.as_view()),
    path('mark/', views.MarkAPI.as_view()),
    # path('marklist/', views.MarkListAPI.as_view()),
    path('student/<int:id>/', views.StudentDetailAPI.as_view()),
    path('mark/<int:id>/', views.MarkDetailAPI.as_view())
]
