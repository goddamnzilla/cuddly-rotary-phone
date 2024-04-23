from django.urls import path
from . import views
urlpatterns=[
    
    path('home/',views.index, name='list'),
    path('update_ticket/<str:pk>/', views.updateTicket, name='update_ticket'),
    path('delete/<str:pk>/', views.deleteTicket, name='delete_ticket'),
    path('',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('signout/',views.signout,name='signout'),

]