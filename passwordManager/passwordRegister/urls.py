from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.password_list, name='password_list'),
    path('password/<int:id>/',views.password_form,name='password_update'),
    path('password/delete/<int:id>/',views.password_delete,name='password_delete'),
    path('password/',views.password_form, name='password_insert'),
    path('export/',views.password_export,name='password_export'),
    path('import/',views.password_import,name='password_import'),

]