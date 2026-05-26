from django.shortcuts import render, redirect
from .models import Note, Category


def home(request):

    search = request.GET.get('search')

    if search:

        notes = Note.objects.filter(title__icontains=search)

    else:

        notes = Note.objects.all()

    context = {
        'notes': notes
    }

    return render(request, 'home.html', context)



def add_note(request):

    categories = Category.objects.all()

    if request.method == 'POST':

        title = request.POST.get('title')
        content = request.POST.get('content')
        category_id = request.POST.get('category')

        category = Category.objects.get(id=category_id)

        Note.objects.create(
            title=title,
            content=content,
            category=category
        )

        return redirect('home')

    context = {
        'categories': categories
    }

    return render(request, 'add_note.html', context)



def delete_note(request, id):

    note = Note.objects.get(id=id)

    note.delete()

    return redirect('home')



def update_note(request, id):

    note = Note.objects.get(id=id)

    categories = Category.objects.all()

    if request.method == 'POST':

        note.title = request.POST.get('title')

        note.content = request.POST.get('content')

        category_id = request.POST.get('category')

        note.category = Category.objects.get(id=category_id)

        note.save()

        return redirect('home')

    context = {
        'note': note,
        'categories': categories
    }

    return render(request, 'update.html', context)