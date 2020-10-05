from django.db import models

# Create your models here.
JOP_TYPE=(
        ('Full Time','Full Time'),
        ('Part Time','Part Time'),
        
)

class vacancy_places(models.IntegerChoices):
    One=1
    Two=2
    Three=3
    Four=4
    Five=5
    Sex=6
    Seven=7
class job(models.Model):
    title=models.CharField(max_length=100)
    #location
    Job_TYPE=models.CharField(max_length=30 ,choices = JOP_TYPE)
    Discripion=models.TextField(max_length=600)
    Published_at=models.TimeField(auto_now=True)
    vacancy=models.IntegerField(choices=vacancy_places.choices)
    salery=models.IntegerField(default=000)
    Experience=models.IntegerField(default=0)
    referanse=models.ForeignKey('referanse',on_delete=models.CASCADE)
    def __str__(self):
        return self.title
class referanse(models.Model):
    name=models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.name