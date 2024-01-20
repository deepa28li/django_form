from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def djform(request):
    ENFO=NameForm()
    d={'ENFO':ENFO}
    if request.method=='POST':
        FO=NameForm(request.POST)
        if FO.is_valid():
            return HttpResponse(str(FO.cleaned_data))
        else:
            return HttpResponse('Invalid submission')
    return render(request,'djform.html',d)