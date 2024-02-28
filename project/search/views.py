from django.shortcuts import render
from search.models import Student
# Create your views here.


def search(request):
    student = Student.objects.all()
    total = Student.objects.count()
    if request.method == 'GET':
        name = request.GET.get('name', '').strip()
        if name:
            student =Student.objects.filter(name__icontains = name)
            
    return render(request,'index.html',{'student':student,'total':total})
