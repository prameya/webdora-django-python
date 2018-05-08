from datetime import datetime

from django.db import models
from django.utils import timezone

from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.template.defaultfilters import slugify

from tinymce.models import HTMLField
from taggit.managers import TaggableManager

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(_('Title'), max_length = 255)
    body = HTMLField(_('Body'), default='Insert body text here.')
    summary = models.TextField(_('Summary'), null=True, blank=True)
    image = models.ImageField(_('Image'), blank=True, null=True, upload_to='blog/%Y/%m/%d')
    published = models.BooleanField(default=False)
    modified = models.DateTimeField(_('Modified'), default=datetime.now)
    
    slug = models.SlugField(_('Slug'), max_length=255, unique=True, blank=True)
    #tags = TaggableManager()

    class Meta:
        ordering = ['-modified']
        verbose_name = 'Blog'

    def __unicode__(self):
        return 'Blog: %s' % self.title

    def __str__(self):
        return 'Blog: %s' % self.title

    def was_published_recently(self):
        return self.timestamp >= timezone.now() - datetime.timedelta(days=1)

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slug = slugify(self.title)
            counter = 1
            while self.__class__.objects.filter(slug=self.slug).exists():
                self.slug = '{0}-{1}'.format(slug, counter)
            counter += 1
        return super(BlogPost, self).save(*args, **kwargs)

class Admin:
    pass
