from django.db import models

# Create your models here.
class employess(models.Model):
    name=models.CharField(max_length=20)
    department=models.CharField(max_length=30)
    id=models.IntegerField(primary_key=True)
    age=models.IntegerField()

# class
#     address=models.TextField()
#     phone_number=models.IntegerField()
#     joining_date=models.DateTimeField(auto_now_add=True)
#
#
# class employee_details(models.Model):
#     name=models.ForeignKey(id,on_delete=models.CASCADE)
#     department=models.ForeignKey(id,on_delete=models.CASCADE)
#     joining_date=models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return self.name



