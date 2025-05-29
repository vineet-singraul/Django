from django.db import models

# Create your models here.


class Customer(models.Model):
    cus_name = models.CharField(max_length=60)
    cus_email = models.EmailField(unique=True)
    cus_password = models.CharField(max_length=50) 
    cus_cpassword = models.CharField(max_length=50)
    cus_image = models.ImageField(upload_to='image')
    cus_phone = models.IntegerField()
    cus_location = models.CharField(max_length=50)

class Query(models.Model):
    cus_name_q = models.CharField(max_length=50)
    cus_email_q = models.EmailField()
    cus_query_q = models.CharField(max_length=150)



class DynamicCards(models.Model):
    db_product_name = models.CharField(max_length=70)
    db_product_discription = models.CharField(max_length=400)
    db_product_discription2 = models.CharField(max_length=400)
    db_product_previous_price = models.IntegerField()
    db_product_offer_percentage = models.IntegerField()
    db_product_real_price = models.IntegerField()
    db_product_catagurays = models.CharField(max_length=100)  # <- no default here
    db_product_image1 = models.ImageField(upload_to='image')
    db_product_image2 = models.ImageField(upload_to='image')
    db_product_image3 = models.ImageField(upload_to='image')
    db_product_image4 = models.ImageField(upload_to='image')
    db_product_image5 = models.ImageField(upload_to='image')
    db_product_image6 = models.ImageField(upload_to='image')

