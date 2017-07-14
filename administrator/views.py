from django.shortcuts import render
from django.views.generic import CreateView,DetailView
from administrator.models import HouseManager

# Create your views here.

def getAdminDashboard(request):
    return render(request, 'administrator/admin_dashboard.html')

#This is the view to create a new HostelOwner
class NeHostelOwner(CreateView):
    model = HouseManager
    fields = ['id_number','first_name','last_name','phone_number']

#Get specific owner details.

class viewOwnerReport(DetailView):
    model = HouseManager
    template_name = 'administrator/hostelowner_report.html'

