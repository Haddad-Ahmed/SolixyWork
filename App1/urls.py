from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django_filters.views import FilterView
from App1 import views
from App1.views import *

urlpatterns = [
    path('',views.index),
    path('id/<int:pk>', views.Collection_id),
    path('add',views.add,name="add"),
    path('create/', views.CollectionCreateView.as_view(), name='create_collection'),
    path('update/<int:pk>', views.CollectionUpdateView.as_view(), name='update_collection'),
    path('read/<int:pk>', views.CollectionReadView.as_view(), name='read_collection'),
    path('delete/<int:pk>', views.CollectionDeleteView.as_view(), name='delete_collection'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('acc/',views.accueil,name='acc'),
    path('CCol/',CreateCollection.as_view(),name='insert'),
    path('DCol/<int:pk>/', DeleteCollection.as_view(), name='delete'),
    path('UCol/<int:pk>/', UpdateCollection.as_view(), name='update'),
    path('Liste', views.Liste_Collection, name='List'),
    path('Filtre', FilterView.as_view(model=Collection))
]