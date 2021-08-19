from django.shortcuts import render
from .models import Activity
from django.views.generic import ListView, DetailView

# Create your views here.
data_object = Activity.objects.all()

class ActivityIndexView(ListView):
	model = Activity
	template_name = 'activity/activity_index.html'

class ActivityDetailView(DetailView):
	model = Activity
	template_name = 'activity/activity_detail.html'

def planting_index(request):
	planting_2021_index = data_object.filter(year__icontains='2021').filter(activity_type__icontains='Planting')
	planting_2020_index = data_object.filter(year__icontains='2020').filter(activity_type__icontains='Planting')
	planting_2019_index = data_object.filter(year__icontains='2019').filter(activity_type__icontains='Planting')
	planting_2018_index = data_object.filter(year__icontains='2018').filter(activity_type__icontains='Planting')
	planting_2017_index = data_object.filter(year__icontains='2017').filter(activity_type__icontains='Planting')
	return render(request, 'activity/planting_index.html', {
			'planting_2021_index':planting_2021_index,
			'planting_2020_index':planting_2020_index,
			'planting_2019_index':planting_2019_index,
			'planting_2018_index':planting_2018_index,
			'planting_2017_index':planting_2017_index
		})
	
def corporate_index(request):
	corporate_2021_index = data_object.filter(year__icontains='2021').filter(activity_type__icontains='corporate')
	corporate_2020_index = data_object.filter(year__icontains='2020').filter(activity_type__icontains='corporate')
	corporate_2019_index = data_object.filter(year__icontains='2019').filter(activity_type__icontains='corporate')
	corporate_2018_index = data_object.filter(year__icontains='2018').filter(activity_type__icontains='corporate')
	corporate_2017_index = data_object.filter(year__icontains='2017').filter(activity_type__icontains='corporate')
	return render(request, 'activity/corporate_index.html', {
			'corporate_2021_index':corporate_2021_index,
			'corporate_2020_index':corporate_2020_index,
			'corporate_2019_index':corporate_2019_index,
			'corporate_2018_index':corporate_2018_index,
			'corporate_2017_index':corporate_2017_index
		})

def wilding_index(request):
	wilding_2021_index = data_object.filter(year__icontains='2021').filter(activity_type__icontains='Wilding')
	wilding_2020_index = data_object.filter(year__icontains='2020').filter(activity_type__icontains='Wilding')
	wilding_2019_index = data_object.filter(year__icontains='2019').filter(activity_type__icontains='Wilding')
	wilding_2018_index = data_object.filter(year__icontains='2018').filter(activity_type__icontains='Wilding')
	wilding_2017_index = data_object.filter(year__icontains='2017').filter(activity_type__icontains='Wilding')
	return render(request, 'activity/wilding_index.html', {
			'wilding_2021_index':wilding_2021_index,
			'wilding_2020_index':wilding_2020_index,
			'wilding_2019_index':wilding_2019_index,
			'wilding_2018_index':wilding_2018_index,
			'wilding_2017_index':wilding_2017_index
		})

def nursery_index(request):
	nursery_2021_index = data_object.filter(year__icontains='2021').filter(activity_type__icontains='Nursery')
	nursery_2020_index = data_object.filter(year__icontains='2020').filter(activity_type__icontains='Nursery')
	nursery_2019_index = data_object.filter(year__icontains='2019').filter(activity_type__icontains='Nursery')
	nursery_2018_index = data_object.filter(year__icontains='2018').filter(activity_type__icontains='Nursery')
	nursery_2017_index = data_object.filter(year__icontains='2017').filter(activity_type__icontains='Nursery')
	return render(request, 'activity/nursery_activity_index.html', {
			'nursery_2021_index':nursery_2021_index,
			'nursery_2020_index':nursery_2020_index,
			'nursery_2019_index':nursery_2019_index,
			'nursery_2018_index':nursery_2018_index,
			'nursery_2017_index':nursery_2017_index
		})