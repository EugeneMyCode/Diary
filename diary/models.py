from django.db import models

# Create your models here.
class Diary(models.Model):
    title = models.CharField(max_length=100, blank = False)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']
        verbose_name_plural = 'diaries'
    
    def __str__(self):
        return self.title