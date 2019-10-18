from django.db import models

class UserType(models.Model):
    user_type = models.CharField(max_length=100)

    def __str__(self):
        return self.user_type

class UserInfo(models.Model):
    first_name   = models.CharField(max_length=100)
    last_name    = models.CharField(max_length=100)
    user_type    = models.ForeignKey(UserType, on_delete= models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
       
    
    