from django.db import models

# Create your models here.
class Registry(models.Model):
    # id = models.CharField(max_length=250)
    ocassion = models.CharField(max_length=250) # pensare si es mejor que sea selecteed
    registry_title = models.CharField(max_length=100)
    name = models.CharField(max_length=13) ## pensar si es mejor que sea un campo diccionario
    event_date = models.DateField() 
    message = models.CharField(max_length=256)
    registry_link = models.CharField(max_length=50)
    show_who_sent_gifts = models.BooleanField(default=True)
    dark_mode = models.BooleanField(default=False)
    photo = models.CharField(max_length=250)

    def __str__(self):
        return self.registry_title
    

class Registry(models.Model):
    # id = models.CharField(max_length=250)
    ocassion = models.CharField(max_length=250) # pensare si es mejor que sea selecteed
    registry_title = models.CharField(max_length=100)
    name = models.CharField(max_length=13) ## pensar si es mejor que sea un campo diccionario
    event_date = models.DateField() 
    message = models.CharField(max_length=256)
    registry_link = models.CharField(max_length=50)
    show_who_sent_gifts = models.BooleanField(default=True)
    dark_mode = models.BooleanField(default=False)
    photo = models.CharField(max_length=250)

    def __str__(self):
        return self.registry_title