from django.urls import path
from . import views
from .views import ItemdetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.index, name='index'),
  path('detail/<int:pk>',ItemdetailView.as_view(), name='item-detail'),
  
]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)