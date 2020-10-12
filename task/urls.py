from django.urls import path 

from . import views #(3) menimport views yang ada di apps

#(5) setelah itu kita membuat url patterns yang berisi path (views, dan nama index)
#halloworld=index
#jika di viev ada def baru, maka membuat path baru
urlpatterns = [
    path('', views.halloworld),
    # path('json/', views.jsonc),
    path('create/', views.create),
    path('<id>/delete/', views.delete),
    path('<id>/update/', views.update),

]