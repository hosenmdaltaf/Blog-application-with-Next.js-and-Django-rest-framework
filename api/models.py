from django.db import models
from django.conf import settings
from django.urls import reverse
# from account.models import Account
# from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey

class Author(models.Model):
    author= models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic',null=True,blank=True,default='man.png')
   
    def __str__(self):
        return str(self.author)

class Post(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)  #settings.AUTH_USER_MODEL
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    post_updated = models.DateField(auto_now=True)
    image=models.ImageField(upload_to='post_images', blank=True, null=True)
    # category = models.ForeignKey('Category',on_delete=models.CASCADE, null=True, blank=True)
    category = TreeForeignKey('Category', on_delete=models.CASCADE, null=True,blank=True)
 
#    share
    view_count=models.IntegerField(default=0)
   # slug=models.SlugField(blank=True,unique=True)


    def __str__(self):
        return str(self.author) + '---' + str(self.title)
 
    def get_absolute_url(self):
        return reverse('user_feeds:articale-detail', kwargs={'id':self.id})

    class Meta:
        ordering = ['-post_date']

    def num_comments(self):
        return self.comment_set.all().count()



# class Category(models.Model):
#     name = models.CharField(max_length=200,null=True,blank=True)
   
#     def __str__(self):
#         return self.name

class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', db_index=True)
    slug = models.SlugField()

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = (('parent', 'slug',))
        verbose_name_plural = 'categories'

    def get_slug_list(self):
        try:
            ancestors = self.get_ancestors(include_self=True)
        except:
            ancestors = []
        else:
            ancestors = [ i.slug for i in ancestors]
            slugs = []
        for i in range(len(ancestors)):
            slugs.append('/'.join(ancestors[:i+1]))
        return slugs

    def __str__(self):
        return self.name



class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)          
    text = models.TextField(blank=True, null=True )
    created_date = models.DateTimeField(auto_now_add=True)
   

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return str(self.created_by)

  



        






