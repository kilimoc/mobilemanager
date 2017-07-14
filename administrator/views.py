from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
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

class allRegisteredOwners(ListView):
    context_object_name = 'all_owners'
    template_name = 'administrator/allowners.html'

    def get_queryset(self):
        return HouseManager.objects.all()

