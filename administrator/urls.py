
from django.conf.urls import url
from . import views

app_name='administrator';

urlpatterns = [
    url(r'^$',views.getAdminDashboard,name='admin-home'),
    url(r'^newOwner', views.NeHostelOwner.as_view(), name='newhostel'),
    #detail url pattern
    url(r'^(?P<pk>[0-9]+)/$',views.viewOwnerReport.as_view(),name='ownerreport'),

]
