from django.db import models
import datetime as dt
# from django-cloudinary.models import CloudinaryField

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/',default='default value')
    # image = CloudinaryField('pictures')
    name = models.CharField(max_length =30)
    description = models.CharField(max_length = 100)
    location = models.ForeignKey('Location',on_delete=models.CASCADE,null=True)
    category=models.ForeignKey('Category',on_delete=models.CASCADE,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    #saves images
    def save_image(self):
        self.save()
    # delete the image database
    def delete_image(self):
        self.delete()
    # update image
    def update_image(self, name, description, location, category):
        self.name = name
        self.description = description
        self.location = location
        self.category = category
        self.save()

    # get all images
    @classmethod
    def get_all_images(cls):
        images = Image.objects.all()
        return images
    

    # get image by id
    @classmethod
    def get_image_by_id(cls, id):
        image = Image.objects.get(id=id)
        return image

    # get images by location
    @classmethod
    def filter_by_location(cls, location):
        images = Image.objects.filter(location=location)
        return images

    # get images by category
    @classmethod
    def filter_by_category(cls, category):
        images = Image.objects.filter(category=category)
        return images

    # search images
    @classmethod
    def search_image(cls, search_term):
        images = cls.objects.filter(name__icontains=search_term)
        return images
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    @classmethod
    def get_all_category(cls):
        categories = Category.objects.all()
        return categories
    def __str__(self):
        return self.name
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls,id,name):
        cls.objects.filter(id = id).update(name = name)    

class Location(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # save location to database
    def save_location(self):
        self.save()

    # update location
    def update_location(self, name):
        self.name = name
        self.save()

     # delete location from database
    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name

