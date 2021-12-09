from django.db import models







class Club(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    people = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default='club')
    image = models.ImageField(default='Images/None/No0img.jpg')


class Restaurant(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    Table = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default='restaurant')
    image = models.ImageField(default='Images/None/No0img.jpg')


class Room(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default='room')
    image = models.ImageField(default='Images/None/No0img.jpg')


class Meeting(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    people = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default='meeting')
    image = models.ImageField(default='Images/None/No0img.jpg')
    

class Banquet(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    plate = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default='banquet')
    image = models.ImageField(default='Images/None/No0img.jpg')
    



    
    
class Order(models.Model):
    def __str__(self):
        return self.name
    customer = models.CharField(max_length=70, default='admin')
    name = models.CharField(max_length=70)
    price = models.CharField(max_length=70)
    



class Task(models.Model):
    def __str__(self):
        return self.task_name
    task_name = models.CharField(max_length=200)
    task_desc = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    image = models.ImageField(upload_to='Images/', default='Images/None/No0img.jpg')
