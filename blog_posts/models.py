from django.db import models

# Create your models here.
class blog_posts(models.Model):
    title = models.CharField(max_length=100)
    #tag = models.CharField(max_length=50)
    text = models.CharField(max_length=2000)

    def __unicode__(self):
        return self.title

    def get_post_url(self):
        return reverse('post_edit', kwargs={'pk': self.pk})
