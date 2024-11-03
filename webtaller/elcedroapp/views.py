from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db import connection

def index(request):
    return render(request, 'elcedroapp/index.html')


def crear_pedido(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion'),
        numero=request.POST.get('numero'),
        cantidad=request.POST.get('cantidad_bidones'),
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO Pedido (nombre, direccion, numero, cantidad_bidones) VALUES (%s, %s,%s,%s)", [nombre, direccion,numero,cantidad])
        return redirect(to='listar-pedidos')
    
    # Manejo para solicitudes GET (muestra el formulario)
    return render(request, 'elcedroapp/registrar.html')

def listar_pedidos(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Pedido")
        pedidos = cursor.fetchall()
    return render(request, 'elcedroapp/listar_pedidos.html', {'pedidos': pedidos})


