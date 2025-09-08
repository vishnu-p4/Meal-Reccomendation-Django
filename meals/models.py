from django.db import models



class Disease(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Meals(models.Model):
    Category_choices = [('breakfast' , 'Breakfast'),('lunch' , 'Lunch'),('dinner' , 'Dinner')]
    name = models.CharField(max_length=100)
    description = models.TextField(null = True , blank = True)
    image = models.ImageField(upload_to = "uploads/meals" , blank=True)
    nutrients = models.JSONField(blank= True , null= True)
    diseases = models.ManyToManyField(Disease, related_name='meals')  
    category = models.CharField(choices = Category_choices , null=True)
    

    def __str__(self):
        return self.name
