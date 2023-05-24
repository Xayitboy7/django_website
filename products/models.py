from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.username

# class Story(models.Model):
#     title = models.CharField(max_length=100)
#     text = models.TextField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now_add=True)
#     genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title
    

# class Comment(models.Model):
#     text = models.TextField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     story = models.ForeignKey(Story, on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.author.username} - {self.story.title}"

# class Image(models.Model):
#     image = models.ImageField(upload_to='images')
#     story = models.ForeignKey(Story, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.story.title} - {self.id}"


# class Genre(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField()

#     def __str__(self):
#         return self.name



# class Favorite(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     story = models.ForeignKey(Story, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.user.username} - {self.story.title}"

# class Rating(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     story = models.ForeignKey(Story, on_delete=models.CASCADE)
#     value = models.IntegerField()
    
#     def __str__(self):
#         return f"{self.user.username} - {self.story.title} ({self.value})"





class Glav(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='Untitled')
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    romani = models.CharField(max_length=50)
    blogs = models.CharField(max_length=50)
    still = models.CharField(max_length=50)

    def __str__(self):
        # return self.name,self.title
        return f"{self.name} - {self.title}"


class Roman(models.Model):
    title = models.CharField(max_length=255, default='Untitled')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    text = models.TextField()
    otziv = models.CharField(max_length=50)
    comment = models.CharField(max_length=50)
    still = models.CharField(max_length=50)
    value = models.IntegerField()

    def __str__(self):
        return self.name


class Block(models.Model):
    title = models.CharField(max_length=255, default='Untitled')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    roman = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.name


class Stix(models.Model):
    title = models.CharField(max_length=255, default='Untitled')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    stix = models.TextField()
    otziv = models.CharField(max_length=50)
    comment = models.CharField(max_length=50)
    value = models.IntegerField()
    def __str__(self):
        return self.name


class Sobit(models.Model):
    title = models.CharField(max_length=255, default='Untitled')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    text = models.TextField()
    roman = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Resens(models.Model):
    title = models.CharField(max_length=255, default='Untitled')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    text = models.TextField()
    lack = models.CharField(max_length=50)
    roman = models.CharField(max_length=50)

    def __str__(self):
        return self.name