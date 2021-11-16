from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def listorders(request):
    return HttpResponse("下面是系统的测试...")

def brokenline(request):
    # there is no real data now, you can generate by yourself
    # 
    # extend your functions here
    return render(request, 'bigdata/index.html', locals())
