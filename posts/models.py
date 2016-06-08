from __future__ import unicode_literals

from django.utils.text import slugify
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save


class Post(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(null=True, blank=True,
                              width_field="width", height_field="height")
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-updated", "-timestamp"]


def pre_post_signal(sender, instance, *args, **kwargs):
    slug = slugify(instance.title)
    exists = Post.objects.filter(slug=slug).exists()

    if exists:
        slug = "%s-%s" % (slug, instance.id)
    instance.slug = slug

pre_save.connect(pre_post_signal, sender=Post)