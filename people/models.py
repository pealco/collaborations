from django.db import models

class Specialization(model.Model):
    description = models.CharField(max_length="30")

class Person(models.Model):
    
    STATUS_CHOICES = (
        ('STUDENT', 'Graduate Student'),
        ('STAFF',   'Research Staff'),
        ('POSTDOC', 'Post-doctoral Fellow'),
        ('FACULTY', 'Faculty'),
        ('ADMIN',   'Administrative Staff'),
        ('VISIT',   'Visitor')
    )
    
    name           = models.CharField(max_length=50)
    status         = models.CharField(max_length=8, choices=STATUS_CHOICES)
    specialization = models.ManyToManyField(Specialization)
    collaborators  = models.ManyToManyField("self", blank=True)

    class Meta:
        verbose_name_plural = 'people'
        
    def __unicode__(self):
        return self.name