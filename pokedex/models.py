from django.db import models

class Trainer(models.Model):
    firt_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    birth_date = models.DateField()
    level = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.firt_name} {self.last_name}'


class Pokemon(models.Model):
    name = models.CharField(max_length=100, null=False)
    POKEMON_TYPES = {
        ('A','Agua'),
        ('F','Fuego'),
        ('E','Eléctrico'),
        ('T','Tierra'),
        ('P','Planta'),
        ('H','Hada'),
        ('L','Lucha'),
    }
    Type = models.CharField(max_length=50, choices=POKEMON_TYPES, null=False)
    weight = models.FloatField()
    height = models.FloatField()
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)
    picture = models.ImageField(upload_to='pokemon_images')

    def __str__(self):
        return self.name