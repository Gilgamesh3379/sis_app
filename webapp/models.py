from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class SISapp(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Programs(models.Model):
    text = models.TextField()
    sis_app = models.ForeignKey(SISapp, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text + "-" + self.user.username

class Lecturers(models.Model):
    text = models.TextField()
    sis_app = models.ForeignKey(SISapp, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text + "-" + self.user.username

class Students(models.Model):
    text = models.TextField()
    sis_app = models.ForeignKey(SISapp, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text + "-" + self.user.username

class Parents(models.Model):
    text = models.TextField()
    sis_app = models.ForeignKey(SISapp, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text + "-" + self.user.username

class Courses(models.Model):
    text = models.TextField()
    sis_app = models.ForeignKey(SISapp, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text + "-" + self.user.username

class Marks(models.Model):
    text = models.TextField()
    sis_app = models.ForeignKey(SISapp, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text + "-" + self.user.username