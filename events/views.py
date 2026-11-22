

# Create your views here.
from django.http import JsonResponse  #it will write python dict into json http response
from django.views.decorators.http import require_GET
SAMPLE_EVENTS=[
    {
        "id":1,"title":"python Meetup","venue":"chennai","available_seats":50},
        {"id": 2, "title": "AI Conference", "venue": "Bengaluru", "available_seats": 0},
]

@require_GET
def event_list(request):
    return JsonResponse({"count":len(SAMPLE_EVENTS),"results":SAMPLE_EVENTS})