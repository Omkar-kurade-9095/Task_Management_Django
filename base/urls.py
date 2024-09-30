
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('addtask',addtask,name='addtask'),
    path('edit/<int:id>',edit,name='edit'),
    path('delete/<int:id>',delete,name='delete'),
    path('details/<int:id>',details,name='details'),
    path('history',history,name='history'),
    path('historydel/<int:id>',historydel,name='historydel'),
    path('clear',clear,name='clear'),
    path('restore/<int:id>',restore,name='restore'),
    path('Restoreall>',Restoreall,name='Restoreall'),
     
]
