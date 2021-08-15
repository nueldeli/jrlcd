from django.urls import path
from .views import NurseryIndexView, NurseryDetailView

urlpatterns = [
	path('nursery_index/', NurseryIndexView.as_view(), name='nursery_index'),
	path('nursery_detail/<int:pk>', NurseryDetailView.as_view(), name='nursery_detail'),
	
]