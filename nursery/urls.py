from django.urls import path
from .views import NurseryIndexView

urlpatterns = [
	path('nursery_index/', NurseryIndexView.as_view(), name='nursery_index'),
]