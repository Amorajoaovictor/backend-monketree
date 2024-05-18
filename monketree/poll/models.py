from django.db import models

class User(models.Model):
    email = models.EmailField()
    senha = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    # id_arvore = models.ForeignKey(arvore, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nickname)
    #
    class Meta:
        verbose_name_plural = "Usuarios"
