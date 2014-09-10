from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
from cau import CAU_GPA_Spider

def hello(request):
    return HttpResponse("Hello world")
    
def current_time(request):
    now = datetime.datetime.now()
    return render_to_response('current_time.html',{'current_date': now})
    
def main(request):
    return render_to_response('main.html')
    
def result(request):
    if 'user' in request.POST and 'password' in request.POST and request.POST['user'] and request.POST['password']:
        mySpider = CAU_GPA_Spider()
        mySpider.cau_init(request.POST['user'], request.POST['password'])
        return render_to_response('result.html', {'user': request.POST['user'], 'password': request.POST['password'], 'GPA': mySpider.GPA })
    else:
        return render_to_response('main.html',{'error': True})
