from django.db import models

class Person(models.Model):
    
    STATUS_CHOICES = (
        ('STUDENT', 'Graduate Student'),
        ('STAFF',   'Research Staff'),
        ('POSTDOC', 'Post-doctoral Fellow'),
        ('FACULTY', 'Faculty'),
        ('ADMIN',   'Administrative Staff'),
        ('VISIT',   'Visitor')
    )
    
    SPECIALIZATION_CHOICES = (
        ('PHONOLOGY', 'Phonology'),
        ('SYNTAX', 'Syntax'),
        ('SEMANTICS', 'Semantics'),
        ('ACQUISITION', 'Acquisition'),
        ('COMPUTATIONAL', 'Computational Linguistics'),
        ('PSYCHO', 'Psycholinguistics'),
        ('NEURO', 'Neurolinguistics')
        
    )
    
    name           = models.CharField(max_length=50)
    status         = models.CharField(max_length=8, choices=STATUS_CHOICES)
    specialization = models.CharField(max_length=12, choices=SPECIALIZATION_CHOICES)
    collaborators  = models.ManyToManyField("self", blank=True)

    class Meta:
        verbose_name_plural = 'people'
        
    def __unicode__(self):
        return self.name