from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Country
from .forms import CountryForm


# 🔹 Vista de prueba (la que ya tenías)
def index(request):
    return HttpResponse("this is my first view !!!")


# 🔹 Vista para listar países
def country_list(request):
    countries = Country.objects.all().order_by('name')
    return render(request, 'authentication/country_list.html', {'countries': countries})


# 🔹 Crear un nuevo país
def country_create(request):
    if request.method == "POST":
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("authentication:country_list")
    else:
        form = CountryForm()

    return render(request, "authentication/country_form.html", {"form": form})


# 🔹 Vista para editar países
def country_edit(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == 'POST':
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            messages.success(request, 'País actualizado correctamente.')
            return redirect('authentication:country_list')
    else:
        form = CountryForm(instance=country)
    return render(request, 'authentication/country_form.html', {'form': form, 'country': country})
