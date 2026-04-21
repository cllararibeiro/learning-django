from django.shortcuts import render, redirect, get_object_or_404
from .models import Consulta

def lista_consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'consultas/lista.html', {'consultas': consultas})

def criar_consulta(request):
    if request.method == 'POST':
        paciente = request.POST.get('paciente')
        data = request.POST.get('data')
        descricao = request.POST.get('descricao')

        Consulta.objects.create(
            paciente=paciente,
            data=data,
            descricao=descricao
        )

        return redirect('lista_consultas')

    return render(request, 'consultas/criar.html')

def deletar_consulta(request, id):
    consulta = get_object_or_404(Consulta, id=id)
    consulta.delete()
    return redirect('lista_consultas')

def editar_consulta(request, id):
    consulta = get_object_or_404(Consulta, id=id)

    if request.method == 'POST':
        consulta.paciente = request.POST.get('paciente')
        consulta.data = request.POST.get('data')
        consulta.descricao = request.POST.get('descricao')
        consulta.save()

        return redirect('lista_consultas')

    return render(request, 'consultas/editar.html', {'consulta': consulta})