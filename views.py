from django.shortcuts import render
from django.http import HttpResponse

def Calculater(request):
    c=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('opr')
            if opr=='+':
                c=n1+n2
            elif opr=='-':
                c=n1-n2
            elif opr=='*':
                c=n1*n2
            else:
                c=n1/n2

    except:
        c="Invalid operation........."
    print(c)
    return render(request,"calculater.html",{'c':c})
def marksheet(request):
    if request.method == "POST":
        n1 = eval(request.POST.get('num1'))
        n2 = eval(request.POST.get('num2'))
        n3 = eval(request.POST.get('num3'))
        n4 = eval(request.POST.get('num4'))
        n5 = eval(request.POST.get('num5'))
        t=n1+n2+n3+n4+n5
        p=t*100/500
        data={
            "total":t,
            "per":p
        }
        return render(request,"marksheet.html",data)
    return render(request, "marksheet.html")