from django.db import models
from rest_framework.exceptions import ValidationError
from django.core.validators import RegexValidator
# Create your models here.

    



class Art(models.Model):
    name = models.CharField(max_length=256, null=False)
    type = models.CharField(max_length=256)
    url = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    
    # def save(self, *args, **kwargs):
    #     if self.name == '':
    #         raise ValidationError('name cannot be empty')
    #     super().save(*args, **kwargs)



class Ocassion(models.Model):
    title = models.CharField(max_length=200)
    art = models.OneToOneField(
        Art,
        on_delete=models.PROTECT,
        primary_key=True,)

    def __str__(self):
        return self.title    

class Sample_Message(models.Model):
    comment = models.CharField(max_length=256)
    ocassion = models.ManyToManyField(Ocassion)

    def __str__(self):
        return self.comment
    

class Registry(models.Model):
    ocassion = models.ForeignKey(Ocassion, related_name='registries', on_delete=models.CASCADE)
    registry_title = models.CharField(max_length=100)
    event_date = models.DateField() 
    message = models.CharField(max_length=256)
    registry_link = models.CharField(
        max_length=50, 
        unique=True, 
        validators=[RegexValidator(r"^[a-zA-Z0-9_]+$", "Your link should just contain letters, numbers or underscore.")]
    )
    show_who_sent_gifts = models.BooleanField(default=True)
    dark_mode = models.BooleanField(default=False)
    photo_url = models.CharField(
        max_length=250, 
        validators=[RegexValidator(r"^.*\.(jpg|JPG|jpeg|PNG|png)$", "Your file has to be jpg or png.")]    
    )

    def __str__(self):
        return self.registry_title
    
class Person(models.Model):
    name = models.CharField(max_length=256, null=False)
    last_name = models.CharField(max_length=256, null=False)
    registry = models.ForeignKey(Registry, related_name='persons', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Gift(models.Model):
    amount = models.IntegerField()
    art_id = models.IntegerField()
    note = models.CharField(max_length=256)
    accepted = models.BooleanField(default=False)
    registry = models.ForeignKey(Registry, related_name='gifts', on_delete=models.CASCADE)

    def __str__(self):
        return self.note

# class Greeting(models.Model):
#     pass