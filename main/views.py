from django.shortcuts import render,HttpResponse
import wikipedia as wp
# Create your views here.
def home(request):
    result={}
    mm={}
    # title={
    #     'title':'homepage'
    # }
    if(request.method=='POST'):
        search=request.POST['search']
    try:
        result=wp.summary(search,sentences=100)
        title=("title",title)
        
       

    except:
         mm=wp.search(search, results=10, suggestion=False)
         
        #  mm=wp.suggest(search)
    #     return HttpResponse("The search does not match with any topic in wikipedia")
    
    return render(request, 'index.html',{"result":result})
    return render(request, 'index.html',{"mm":mm})
    return render(request, 'index.html',{"title":title})

    # return render(request,'index.html',)


