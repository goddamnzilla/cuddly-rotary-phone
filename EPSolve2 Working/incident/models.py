from django.db import models

# Create your models here.

class Ticket (models.Model):
    atm_id = models.CharField(max_length=20,default='')
    ticket_details = models.CharField(max_length=200,default='')
    city = models.CharField(max_length=30,default='')
    solved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=20,default='EPS User')
    
    def __str__(self):
        return self.ticket_details