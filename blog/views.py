from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post, Author, Category
from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.views.generic.list import View

# Create your views here.

def get_category_count():
    queryset = Post \
        .objects \
        .values('categories__id','categories__title') \
        .annotate(Count('categories__title'))
    
    return queryset


class Index(View):
    template_name = 'blog/index.html'
    
    def get(self, request, *args, **kwargs):
        category_count = get_category_count()
        most_recent = Post.objects.order_by('-timestamp')[:3]
        post_list = Post.objects.all()
        paginator = Paginator(post_list, 3)
        page_request_var = 'page'
        page = request.GET.get(page_request_var)

        try:
            paginated_queryset = paginator.page(page)
        except PageNotAnInteger:
            paginated_queryset = paginator.page(1)
        except EmptyPage:
            paginated_queryset = paginator.page(paginator.num_pages)

    
        context = {

            'active_page': 'blog',
            'queryset': paginated_queryset,
            'most_recent': most_recent,
            'page_request_var': page_request_var,
            'category_count': category_count,
            

        }

		
        return render(request, self.template_name, context)	

            
class Post_Detail(View):
    template_name = 'blog/post.html'

    def get(self, request, *args, **kwargs):
        
        id=kwargs["id"]
        category_count = get_category_count()
        most_recent = Post.objects.order_by('-timestamp')[:3]
        post = get_object_or_404(Post, id=id)
        increase_of_view = post.view_count
        increase_of_view +=1
        post.view_count=increase_of_view
        post.save()
        
        context = {
        'active_page': 'blog',
        'post': post,
        'most_recent': most_recent,
        'category_count': category_count,
        }

        return render(request, self.template_name, context)


    

class By_Cat_Post_List(View):
    template_name='blog/by_category.html'

    def get(self, request, *args, **kwargs):
        category_count = get_category_count()
        most_recent = Post.objects.order_by('-timestamp')[:3]
        cat_id = kwargs['cat_id']
        
        '''
        Step.objects.all().values('id','movie__title','state', 'movie__slug','movie__id', 'company__title','company__id','company__price', 'movie__added_by','movie__added_by__username', 'review').filter(id__exact = step_id)
        '''
        post_list_by_cat = Category.objects.all().values('post__id','post__title','title','post__timestamp').filter(id__exact = cat_id)
        
        context = {
            'active_page': 'blog',
            'post_list_by_cat': post_list_by_cat,
            'most_recent': most_recent,
            'category_count': category_count,
        }

    
        return render(request, self.template_name, context)



# def prev_page(request,curr_path):
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))