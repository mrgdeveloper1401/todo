from django.db import models
from django.utils.translation import gettext_lazy as _
from hashlib import sha1
from core.models import CreateMixin, UpdateMixixn


class Images(CreateMixin, UpdateMixixn):
    image = models.ImageField(upload_to='images/%Y/%m/%d', width_field='image_width', height_field='image_height')
    image_hash = models.CharField(max_length=40, blank=True, null=True)
    image_alt = models.CharField(max_length=50, blank=True, null=True)
    image_width = models.PositiveIntegerField(blank=True, null=True)
    image_height = models.PositiveIntegerField(blank=True, null=True)
    image_size = models.PositiveIntegerField(blank=True, null=True, default=0)
    is_active = models.BooleanField(default=True)
    
    @property
    def generate_hash(slef):
        hasher = sha1()
        for c in slef.image.chunks:
            hasher.update(c)
        return hasher
        
    
    def save(self, *args, **kwargs):
        self.image_hash = self.generate_hash
        self.image_size = self.image.size
        return super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'image'
        verbose_name = 'image'
        verbose_name_plural = 'images'