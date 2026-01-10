from django.db import models

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)

    def __str__(self):
        return self.nome
    
class clubeDeLivro(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_fundacao = models.DateField()

    def __str__(self):
        return self.nome
    
class Editor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
    
class Escritor(models.Model):
    nome = models.CharField(max_length=100)
    biografia = models.TextField()
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome
    
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    resumo = models.TextField()
    data_publicacao = models.DateField()
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    escritor = models.ForeignKey(Escritor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
