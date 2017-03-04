from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Tienda(models.Model):
	user = models.ForeignKey(User, related_name='tiendas')
	name = models.CharField(max_length=140)
	slug = models.SlugField(max_length=300)

	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse('detail', args=[self.slug])