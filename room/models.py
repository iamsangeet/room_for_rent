from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.title

class Room(models.Model):
    title = models.CharField(max_length=100)
    no_of_rooms = models.PositiveIntegerField()
    price = models.FloatField()
    location = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='room/', null=True, blank=True)
    publish_date = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "room"

