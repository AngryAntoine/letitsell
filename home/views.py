from django.shortcuts import render
from django.http import HttpResponse


def greeting_page(request):
    return render(request, 'home/greeting_page.html')

#def accontactors(request):
#    contactors = (
 #       {'id': 1,
#         'type': 'BF5000220',
#         'rated_current': '50A AC-3 25kW'},
#        {'id': 2,
#         'type': 'BF6500220',
#         'rated_current': '65A AC-3 30kW'},
#        {'id': 3,
#         'type': 'BF8000220',
 #        'rated_current': '80A AC-3 41kW'},
 #       {'id': 4,
 #        'type': 'BF9500220',
#         'rated_current': '95A AC-3 50kW'},
 #       {'id': 5,
#         'type': 'BF110000220',
#         'rated_current': '110A AC-3 60kW'},
#        {'id': 6,
#         'type': '11B50000220',
#         'rated_current': '500A AC-3 265kW'},)
#    return render(request, 'home/ACContactors.html', {'contactors': contactors})
