from django.shortcuts import render

from plan.models import clsnetwork


# Create your views here.
def funnetwork(request,url_network):
    networks = clsnetwork.objects.all()

    #return render(request, 'plan/networkpage.html', context={'networks': networks})
    return render(request, 'plan/'+url_network+'.html', context={'networks': networks})

def funsystem(request):
    return render(request,'systempage.html')