from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Section(models.Model):
    name = models.CharField(max_length=255, verbose_name='Section name')

    class Meta:
        db_table = 'sections'
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'


class Card(models.Model):
    headline = models.CharField(max_length=140, verbose_name='Headline')
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Section')
    description = models.TextField(verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    class Meta:
        db_table = 'cards'
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'


class CardImage(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, verbose_name='Card')
    image = models.ImageField(upload_to='card_images', verbose_name='Image')

    class Meta:
        db_table = 'card_images'
        verbose_name = 'Card Image'
        verbose_name_plural = 'Card Images'


class CardContact(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    location = models.CharField(max_length=255, verbose_name='Location')
    phone = PhoneNumberField(verbose_name='Phone number')
    email = models.EmailField(verbose_name='Email')

    class Meta:
        db_table = 'card_contacts'
        verbose_name = 'Card Contact'
        verbose_name_plural = 'Card Contacts'
