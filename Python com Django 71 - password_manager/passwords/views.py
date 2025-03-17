from django.shortcuts import render, redirect, get_object_or_404
from .models import Folder, PasswordEntry
from django.contrib import messages

def home(request):
    folders = Folder.objects.all()
    return render(request, 'passwords/home.html', {'folders': folders})

def create_folder(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Folder.objects.create(name=name)
    return redirect('home')

def folder_detail(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)
    entries = PasswordEntry.objects.filter(folder=folder)
    return render(request, 'passwords/folder_detail.html', {'folder': folder, 'entries': entries})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Folder, PasswordEntry
from django.http import HttpResponse

# Exibir as pastas
def home(request):
    folders = Folder.objects.all()
    return render(request, 'passwords/home.html', {'folders': folders})

# Criar uma nova pasta
def create_folder(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Folder.objects.create(name=name)
    return redirect('home')

# Detalhes da pasta (com senha)
def folder_detail(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)
    entries = PasswordEntry.objects.filter(folder=folder)
    return render(request, 'passwords/folder_detail.html', {'folder': folder, 'entries': entries})

# Função para editar uma pasta
def edit_folder(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)
    
    if request.method == 'POST':
        new_name = request.POST.get('name')
        if new_name:
            folder.name = new_name
            folder.save()
            return redirect('home')  # Redireciona para a página inicial após editar a pasta.
    
    return render(request, 'passwords/edit_folder.html', {'folder': folder})

# Função para excluir uma pasta
def delete_folder(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)
    folder.delete()
    return redirect('home')  # Redireciona para a página inicial após excluir a pasta.


def add_password(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)
    
    if request.method == 'POST':
        entry_id = request.POST.get('entry_id')  # Verifica se é uma edição

        # Captura os campos principais
        site_name = request.POST.get('site_name')
        site_link = request.POST.get('site_link')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Captura os campos personalizados
        labels = request.POST.getlist('extra_field_label[]')
        values = request.POST.getlist('extra_field_value[]')
        extra_fields = {labels[i]: values[i] for i in range(len(labels)) if labels[i]}  # Ignora vazios

        if entry_id:  # Se for uma edição
            entry = get_object_or_404(PasswordEntry, id=entry_id)
            entry.extra_fields.update(extra_fields)  # Adiciona os novos campos sem sobrescrever os antigos
            entry.save()
        else:  # Se for um novo registro
            PasswordEntry.objects.create(
                folder=folder,
                site_name=site_name,
                site_link=site_link,
                username=username,
                password=password,
                extra_fields=extra_fields
            )

        return redirect('folder_detail', folder_id=folder.id)

    return render(request, 'passwords/folder_detail.html', {'folder': folder})

# Função para editar a senha
def edit_password(request, entry_id):
    entry = get_object_or_404(PasswordEntry, id=entry_id)

    # Para garantir que estamos passando o dicionário corretamente
    extra_fields = entry.extra_fields if entry.extra_fields else {}

    if request.method == 'POST':
        # Atualizando os campos principais
        entry.site_name = request.POST.get('site_name', entry.site_name)
        entry.site_link = request.POST.get('site_link', entry.site_link)
        entry.username = request.POST.get('username', entry.username)
        entry.password = request.POST.get('password', entry.password)

        # Atualizando ou criando campos personalizados
        extra_fields = {}

        extra_field_labels = request.POST.getlist('extra_field_label[]')
        extra_field_values = request.POST.getlist('extra_field_value[]')

        for label, value in zip(extra_field_labels, extra_field_values):
            if label and value:
                extra_fields[label] = value

        # Atualiza o campo extra_fields com os novos dados
        entry.extra_fields = extra_fields
        entry.save()

        messages.success(request, "Entrada atualizada com sucesso!")
        return redirect('folder_detail', folder_id=entry.folder.id)

    return render(request, 'passwords/edit_password.html', {'entry': entry, 'extra_fields': extra_fields})

# Função para excluir uma entrada de senha
def delete_password(request, entry_id):
    entry = get_object_or_404(PasswordEntry, id=entry_id)
    if request.method == 'POST':
        entry.delete()
        return redirect('folder_detail', folder_id=entry.folder.id)
