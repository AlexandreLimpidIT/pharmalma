from django.shortcuts import render
import json

#working url : 
#http://127.0.0.1:8000/carte/?ville=suc%C3%A9+sur+erdre&points=[{"lat":47.344062,"lng":-1.5289619},{"lat":47.341824,"lng":-1.526767}]
def carte_view(request):
    ville = request.GET.get('ville')
    message = None
    points_str = request.GET.get('points')
    
    if points_str:
        try:
            points = json.loads(points_str) 
        except json.JSONDecodeError:
            points = []
            message = "Format de points invalide"

    context = {
        'ville': ville,
        'message': message,
        'points' : json.dumps(points)
    }
    return render(request, 'carte.html', context)