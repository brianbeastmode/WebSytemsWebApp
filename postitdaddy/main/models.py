from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django_resized import ResizedImageField
from tinymce.models import HTMLField
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from taggit.managers import TaggableManager
# Create your models here.
User = get_user_model()

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50, blank=True)
    bio = HTMLField()
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    points = models.IntegerField(default=0)
    profile_pic = ResizedImageField(size=[50,80], quality=100, upload_to="user_pic", default=None, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)
        super(UserProfile, self).save(*args, **kwargs)    

    def __str__(self):
        return str(self.fullname)   

class Community(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=400, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Community, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Communities'  

class Thread(models.Model):
    title = models.CharField(max_length=400)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = HTMLField()
    community = models.ManyToManyField(Community,)
    tags = TaggableManager()
    votes = models.ManyToManyField(User, related_name='postVoter')
    date = models.DateTimeField(auto_now_add=True)
    hit_count_generic = GenericRelation(
    HitCount, object_id_field='object_pk',
    related_query_name='hit_count_generic_relation')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Thread, self).save(*args, **kwargs)

    def __str__(self):
        return self.title