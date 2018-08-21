from django.db import models

# Create your models here.
class Color(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'color'
        verbose_name_plural = 'clors'

    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Aluminium(models.Model):
    name = models.CharField(max_length=300,db_index=True)
    slug = models.SlugField(max_length=20, db_index=True)
    code = models.CharField(max_length = 20)
    image=models.ImageField(upload_to='alums/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    leng = models.PositiveIntegerField(default=5800)
    # doi ra kg
    change = models.DecimalField(max_digits=5, decimal_places=2)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ('code',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
