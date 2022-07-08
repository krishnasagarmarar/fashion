from django.urls import path,include
from . import views
app_name='fashionapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('fashion/<int:fashion_id>/',views.details,name='details'),
    path('add/',views.add_fashion,name='add_fashion'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]