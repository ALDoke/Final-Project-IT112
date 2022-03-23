from django.shortcuts import render
from .models import Task, TaskDetails
from .forms import Meetingform
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request): 
    return render(request, 'project/index.html')

def taskDetail(request, id):
    meeting-get_object_or_404(Meeting, pk=id)
    return render(request, 'club/taskdetail.html', {'task' : task})

@login_required
def newTask(request):
    form=Taskform

    if request.method=='POST':
        form=Taskform(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=Taskform()
    else:
        form=Taskform()
    return render(request, 'club/newtask.html', {'form': form})

def loginmessage(request):
    return render(request, 'club/loginmessage.html')

def logoutmessage(request):
    return render(request, 'club/logoutmessage.html')