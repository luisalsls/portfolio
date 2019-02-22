from django.shortcuts import render

# Create your views here.
def home(request):
    nome = 'Luísa'
    conhecimentos = ['Competências', 'Línguas', 'Porjetos','HTML', 'CSS', 'JavaScript','Python', 'Django', 'Git']


    return render(request, 'index.html',{'conhecimentos': conhecimentos})
