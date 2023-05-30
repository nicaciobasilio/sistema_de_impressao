from django.shortcuts import render
from django.http import HttpResponse
from .models import ResponsavelTecnico, ProdutorRural, Propriedade, Diagnostico

def taskList(request):
    return render(request, 'diagnosticos/impressao.html')

def exibir_diagnostico(request):
    responsavel = ResponsavelTecnico.objects.first()
    produtor = ProdutorRural.objects.first()
    propriedade = Propriedade.objects.first()
    diagnostico = Diagnostico.objects.first()

    context = {
        'responsavel': responsavel,
        'produtor': produtor,
        'propriedade': propriedade,
        'diagnostico': diagnostico,
    }

    return render(request, 'diagnosticos/impressao.html', context)