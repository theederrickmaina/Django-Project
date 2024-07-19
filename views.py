from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import ObituaryForm

# def home(request):
#     return render(request, 'obituaries/submit_obituary.html')
def submit_obituary(request):
    if request.method == 'POST':
        form = ObituaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Replace with the name of your success page
    else:
        form = ObituaryForm()
    return render(request, 'obituaries/submit_obituary.html', {'form': form})



