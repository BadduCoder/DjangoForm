from django.shortcuts import render,redirect
from .models import Confess
from django.utils import timezone 
from .forms import Confessform

# Create your views here.
def index(request):
	confessions = Confess.objects.all().order_by('-created_date')
	return render(request,'confess/index.html',{
		'confessions' : confessions,
	})

def confessnow(request):
	if request.method=="POST":
		form = Confessform(request.POST)
		if form.is_valid():
			confessed = form.save(commit=False)
			confessed.created_at = timezone.now()
			confessed.sender = request.user
			confessed.save()
			return redirect('index')
	else:
		form = Confessform()
		return render(request,'confess/form.html',{
			'form': form,
		})