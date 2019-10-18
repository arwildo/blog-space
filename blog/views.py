from django.views import generic
from .models import Post
from django.views.generic import TemplateView

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class Policy(TemplateView):
    template_name = 'policy.html'
