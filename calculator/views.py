from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Calculator App" + ' '+ str(request))

from .models import Visit

def index(request):
    # Handle visit count
    if 'visit_count' not in request.session:
        visit, created = Visit.objects.get_or_create(id=1)
        request.session['visit_count'] = visit.count
    request.session['visit_count'] += 1

    # Update visit count in the database
    visit = Visit.objects.get(id=1)
    visit.count = request.session['visit_count']
    visit.save()

    return render(request, 'calculator/index.html', {
        'visits': request.session['visit_count']
    })


from django.http import JsonResponse

def add_numbers_api(request):
    num1 = float(request.GET.get('num1', 0))
    num2 = float(request.GET.get('num2', 0))
    result = num1 + num2
    return JsonResponse({'sum': result})

