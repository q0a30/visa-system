from django.shortcuts import render, redirect
from .models import Client

def home(request):
    query = request.GET.get('q')

    if query:
        clients = Client.objects.filter(full_name__icontains=query)
    else:
        clients = Client.objects.all()

    return render(request, 'home.html', {'clients': clients})


def add_client(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        passport_number = request.POST['passport_number']
        phone = request.POST['phone']
        photo = request.FILES['photo']
        passport_image = request.FILES['passport_image']

        Client.objects.create(
            full_name=full_name,
            passport_number=passport_number,
            phone=phone,
            photo=photo,
            passport_image=passport_image
        )
        return redirect('/')

    return render(request, 'add.html')