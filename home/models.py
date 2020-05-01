from django.db import models

# Create your models here.
#Contact is the name of the table and name,email,phone...are the column of that table
'''phir migrations and migrate kro
migration- ye changes ko dekhta hai
migrate-un changes ko database me reflect kr deta hai
'''
#register the model in admin.py
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    subject=models.CharField(max_length=12)
    message=models.TextField()
    date=models.DateField()


    #ye function ka sirf role ye hai ki data base me kisi ka data uske naam se show hoga
    def __str__(self):
        return self.name
    

#ye sare column bn jayenge admin me    




