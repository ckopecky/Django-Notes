from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import PersonalNote
from .serializer import PersonalNoteViewSet

def index(request):
    return HttpResponse("Note Creator App!")
def view_all_notes(request):
    latest_note_list = PersonalNote.objects.all()
    context = {'latest_note_list': latest_note_list}
    return render(request, 'notes/index.html', context)

def detailnote(request, note_id):
    note = get_object_or_404(PersonalNote, pk=note_id)
    return render(request, 'notes/detail.html', {'note': note})

