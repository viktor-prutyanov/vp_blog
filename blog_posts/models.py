from django.db import models

class blog_posts(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=2000)

    def __unicode__(self):
        return self.title

    def get_post_url(self):
        return reverse('post_edit', kwargs={'pk': self.pk})
