from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# THIS IS FOR THE PROFILE

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coverpic=models.ImageField(default='default1.jpg', upload_to='profile_coverpic') 
    profilepic=models.ImageField(default='default.jpg', upload_to='profile_pic') 


    def __str__(self):
        
        return f'{self.user.username} profile' 


    # def save(self, *args,**kwargs):
    #     super(Profile, self).save(*args, **kwargs)

    #     coverpi= Image.open(self.coverpic.path)
    #     if coverpi.height > 400 or coverpi.width > 400:
    #         output_size=(1000,1000)
    #         coverpi.thumbnail(output_size)
    #         coverpi.save(self.coverpic.path)

    #     profilepi= Image.open(self.profilepic.path)
    #     if profilepi.height > 300 or profilepi.width > 300:
    #         output_size=(300,300)
    #         profilepi.thumbnail(output_size)
    #         profilepi.save(self.profilepic.path)
