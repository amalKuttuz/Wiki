from django.shortcuts import render,HttpResponse
import wikipedia as wp
# Create your views here.
def home(request):
    result={}
    search={}
    title={}

    if(request.method=='POST'):
        search=request.POST['search']
    # try:
    title=search
    result=wp.summary([search],sentences=100)

    # except:
    #      return HttpResponse("The search does not match with any topic in wikipedia")
    
    return render(request, 'index.html',{"result":result,"title":title})



