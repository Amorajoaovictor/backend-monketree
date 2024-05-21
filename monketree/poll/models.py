from django.contrib import admin
from django.db import models

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    birth = models.DateField()
    # id_arvore = models.ForeignKey(arvore, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nickname)

    class Meta:
        verbose_name_plural = "Usuarios"


class Block(models.Model):
    title = models.CharField(max_length=100)
    #estilo = models.CharField(max_length=50)
    link = models.URLField()

    def __str__(self):
        return self.title


class Click(models.Model):
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField (default='127.0.0.1')

    def __str__(self):
        return f'Clique no {self.block.title} em {self.timestamp}'


class Tree(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @admin.display(description='Link')
    def link(self):
        user = User.objects.get(id=self.user.id)
        nickname = user.nickname
        return f"https://www.monketree/{nickname}"

    link.short_description = 'link'


