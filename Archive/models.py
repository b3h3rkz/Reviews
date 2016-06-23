from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Level(models.Model):
    level = models.CharField(blank=False, unique=True, max_length=3)

    def uploaded_files(self):
        return self.upload_set.count()

    def __str__(self):
        return self.level


class Student(User):
    level = models.ForeignKey(Level)

    def student_level(self):
        return self.level_set.all()

    def __str__(self):
        return self.username


class Course(models.Model):
    name = models.CharField(max_length=30, blank=False)
    course_code = models.CharField(max_length=10, unique=True)
    lecturer = models.ForeignKey(User)
    level = models.ForeignKey(Level)

    def __str__(self):
        return self.name


class Upload(models.Model):
    title = models.CharField(blank=False, max_length=100)
    file = models.FileField(upload_to='media')
    upload_date = models.DateTimeField(auto_now_add=True)
    level = models.ForeignKey(Level)
    course = models.ForeignKey(Course)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('file', 'uploaded_by')


class Comments(models.Model):
    commenter = models.ForeignKey(User)
    post = models.ForeignKey(Upload, related_name="upload_comment")
    comment = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.comment