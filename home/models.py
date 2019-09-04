# from django.db import models
# from thepreventivemedicine import settings
# from django.utils.encoding import smart_text


# ARTICLE_CATEGORY = (

#     ('home_first', 'HOME_FIRST'),
#     ('how', 'HOW'),
#     ('home_second', 'HOME_SECOND'),
#     ('why', 'WHY'),
#     ('howmuch', 'HOWMUCH'),
# )

# class ArticleQuerySet(models.query.QuerySet):
    
#     def home_first(self):
#         return self.filter(publish='home_first')

    

# class ArticleManager(models.Manager):

#     def get_queryset(self):
#         return ArticleQuerySet(self.model, using=self._db)


#     def first_articles(self, *args, **kwargs):
#         # qs = super(ArticleManager, self).all(*args, **kwargs).published_movies()
#         qs = self.get_queryset().home_first()
#         return qs



# class Article(models.Model):
#     id           = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
#     publish      = models.CharField(max_length=120, choices=ARTICLE_CATEGORY, default='home_first')
#     title        = models.CharField(max_length=150, unique=True, null=False, verbose_name='Title')
#     text         = models.TextField(verbose_name='body')
#     articlecover = models.ImageField(upload_to='static/images', null=True, blank=True)
    

#     objects = ArticleManager()

#     class Meta:
#         verbose_name = 'Article'
#         verbose_name_plural = 'Articles'
    
#     def __str__(self):
#         return smart_text(self.title)