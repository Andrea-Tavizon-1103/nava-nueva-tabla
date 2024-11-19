from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto

def inicio_vista(request):
        losproductos = Producto.objects.all()
        return render(request, "gestionarProducto.html", {"misproductos": losproductos})

def registrarProducto(request):
    idproducto = request.POST["txtidproducto"]
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]
    precio = request.POST["numprecio"]
    stock = request.POST["numstock"]
    categoria = request.POST["txtcategoria"]
    fecha_agregado = request.POST["txtfecha_agregado"]

    Producto.objects.create(
        idproducto=idproducto,
        nombre=nombre,
        descripcion=descripcion,
        precio=precio,
        stock=stock,
        categoria=categoria,
        fecha_agregado=fecha_agregado,
        )
    return redirect("/")

def borrarProducto(request, idproducto):
        producto = get_object_or_404(Producto, idproducto=idproducto)
        producto.delete()
        return redirect("/")

def seleccionarProducto(request, idproducto):
        producto = get_object_or_404(Producto, idproducto=idproducto)
        return render(request, "editarProducto.html", {"producto": producto})

def editarProducto(request):
        idproducto = request.POST["txtidproducto"]
        nombre = request.POST["txtnombre"]
        descripcion = request.POST["txtdescripcion"]
        precio = request.POST["numprecio"]
        stock = request.POST["numstock"]
        categoria = request.POST["txtcategoria"]
        fecha_agregado = request.POST["txtfecha_agregado"]

        producto = get_object_or_404(Producto, idproducto=idproducto)

        producto.nombre = nombre
        producto.descripcion = descripcion
        producto.precio = precio
        producto.stock = stock
        producto.categoria = categoria
        producto.fecha_agregado = fecha_agregado
        producto.save()

        return redirect("/")
