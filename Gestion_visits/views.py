from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from Gestion_visits.models import Fonctionnaire, Histo_Prestation, Visiteur, date
import datetime , locale


def go_home(request):

    fonction = Fonctionnaire.objects.all()
    return render(request,'plus-admin\demo_1\home.html',{'Fonctionnaire':fonction[0]})

def go_table(request):
    locale.setlocale(locale.LC_ALL, 'fr')
    today =datetime.datetime.now().strftime('%Y-%m-%d') 
    depart = get_object_or_404(Fonctionnaire, nom_F='Zak' )
    
    histo_pres = Histo_Prestation.objects.select_related('code_vist','code_F','code_Pres','code_date').filter(code_date__visit_date="2022-04-18"  ).order_by('-code_date__visit_date')  
    histo_pres_today = Histo_Prestation.objects.select_related('code_vist','code_F','code_Pres','code_date').filter(code_date__visit_date="2022-04-18" ,status="En coure" ,code_F__nom_F='Zak' ).order_by('-code_date__visit_date')  
    return render(request ,'plus-admin\demo_1\pages\s_tables\s_basic-table.html',{'prestation_histo':list(histo_pres) , 'En_coure':list(histo_pres_today) , 'Date_time':datetime.datetime.now().strftime("%B %d-%Y")
                              , 'len_histo_pres_today':len(list(histo_pres_today)), 'len_histo_pres':len(list(histo_pres))   , 'depart':depart})