from django.db import models
class User(models.Model):
    name = models.CharField(max_length=100 ,null=False)
    email = models.EmailField(max_length=100, null=False)
    mobile = models.CharField(max_length=11, null=False)
    user_id = models.AutoField(primary_key=True)
    def isExists(self):
        if User.objects.filter(email=self.email):
            return True
        return False
    def __str__(self) -> str:
        return self.name
    

class Task(models.Model):
    PENDING = 'Pending'
    DONE = 'Done'
    TASK_TYPE = [
        (PENDING, 'Pending ⏳'),
        (DONE, 'Done ✔'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Task_detail = models.TextField()
    Task_type = models.CharField(max_length=100, choices=TASK_TYPE,)
    def __str__(self) -> str:
        return  f"{self.user.name} --Task:: {self.Task_detail}"
