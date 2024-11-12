from django.shortcuts import render
from .api_utils import get_data_from_rapidapi

def my_view(request):
    data = get_data_from_rapidapi('some-endpoint', params={'param1': 'value1'})
    context = {
        'data': data
    }
    return render(request, 'home.html', context)
