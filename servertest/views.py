from django.shortcuts import render
from servertest.models import ServerTestKV
# Create your views here.


def servertest(request):
    dbdata = ServerTestKV.objects.all()
    return render(request, 'servertest.html', {'dbdata': dbdata})
