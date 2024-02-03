from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_student, name='view_student'),
    path('addstudent/', views.add_student, name='add_student'),
    path('editstudent/<int:id>', views.edit_student, name='edit_student'),
    path('removestudent/<int:id>', views.remove_student, name='remove_student'),
]
