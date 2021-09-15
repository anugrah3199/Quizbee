from django.db import models

# Create your models here.

    

class Quiz(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "categories"

class Questions(models.Model):
    question = models.CharField(max_length = 250)
    optiona = models.CharField(max_length = 100)
    optionb = models.CharField(max_length = 100)
    optionc = models.CharField(max_length = 100)
    optiond = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 100)
    catagory = models.ForeignKey(Quiz,on_delete= models.CASCADE)

    class Meta:
        ordering = ('-catagory',)
        verbose_name_plural = "questions"
        verbose_name = "question"

    def __str__(self):
        return self.question
