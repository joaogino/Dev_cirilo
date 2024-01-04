from django.db import models

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    nome_de_usuario = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    rua = models.CharField(max_length=100)
    suíte = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    código_postal = models.CharField(max_length=20)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    site = models.URLField()
    empresa_nome = models.CharField(max_length=100)
    empresa_catchPhrase = models.CharField(max_length=100)
    empresa_bs = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Todo(models.Model):
    userId = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    concluído = models.BooleanField()

    def __str__(self):
        return self.title
class Post(models.Model):
    userId = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    postId = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return self.name