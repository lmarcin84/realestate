from django.shortcuts import get_object_or_404 ,render
from django.http import HttpResponse, Http404

from .models import Property

# Create your views here.


def index(request):
    latest_properties = Property.objects.order_by('-published_at')[:5]
    # output = ', '.join([s.signature for s in latest_properties])
    # return HttpResponse(output)
    #template = loader.get_template('arkadia/index.html')
    context = {
        'latest_properties': latest_properties,
    }
    return render(request, 'arkadia/index.html', context)


def detail(request, property_id):

    property = get_object_or_404(Property, pk=property_id)
    return render(request, 'arkadia/detail.html', {'property': property})

def results(request, property_id):
    response = "You're looking at results of property %s."
    return HttpResponse(response % property_id)
