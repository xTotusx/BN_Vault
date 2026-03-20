from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Equipo, Pallet, Recepcion

@login_required(login_url='/login/')
def dashboard_principal(request):
    context = {
        'total_recepciones': Recepcion.objects.count(),
        'total_equipos': Equipo.objects.count(),
        'total_pallets': Pallet.objects.count(),
    }
    return render(request, 'dashboard.html', context)