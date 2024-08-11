from django.db import models

# Create your models here.

    



class Art(models.Model):
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=256)
    url = models.CharField(max_length=256)

    def __str__(self):
        return self.name



class Ocassion(models.Model):
    # id = models.IntegerField(max_length=250)
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    # registries = 
    art = models.OneToOneField(
        Art,
        on_delete=models.PROTECT,
        primary_key=True,)
    # ocassion_id = models.IntegerField() 

    def __str__(self):
        return self.name    

class Sample_Message(models.Model):
    # id = models.CharField(max_length=250)
    comment = models.CharField(max_length=256)
    ocassion = models.ManyToManyField(Ocassion)

    def __str__(self):
        return self.comment
    

class Registry(models.Model):
    # id = models.AutoField(primary_key=True)
    # ocassion = models.OneToOneField(
    #     Ocassion,
    #     on_delete=models.PROTECT,
    #     primary_key=True,)
    ocassion = models.ForeignKey(Ocassion, related_name='registries', on_delete=models.CASCADE)
    registry_title = models.CharField(max_length=100)
    # name = models.CharField(max_length=13) ## pensar si es mejor que sea un campo diccionario
    event_date = models.DateField() 
    message = models.CharField(max_length=256)
    registry_link = models.CharField(max_length=50)
    show_who_sent_gifts = models.BooleanField(default=True)
    dark_mode = models.BooleanField(default=False)
    photo = models.CharField(max_length=250)
    

    def __str__(self):
        return self.registry_title
    
class Person(models.Model):
    name = models.CharField(max_length=256)
    registry = models.ForeignKey(Registry, related_name='persons', on_delete=models.CASCADE)


class Gift(models.Model):
    # id = models.CharField(max_length=250)
    amount = models.IntegerField()
    art_id = models.IntegerField()
    note = models.CharField(max_length=256)
    accepted = models.BooleanField(default=False)
    registry = models.ForeignKey(Registry, related_name='gifts', on_delete=models.CASCADE)

    def __str__(self):
        return self.amount
