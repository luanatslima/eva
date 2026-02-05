from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def sobre(request):
    return render(request, 'sobre.html')    

def clubes(request):
    return render(request, 'clubes.html')

def editoras(request):
    return render(request, 'editoras.html')

def livros(request):
    return render(request, 'livros.html')   

def configuracoes(request):
    return render(request, 'configuracoes.html')
