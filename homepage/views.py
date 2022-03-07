
from django.views.generic import ListView,DetailView
from .models import Post

# Create your views here.
class ViewAllPost(ListView):
    model = Post
    template_name = 'home.html'
class ViewDetails(DetailView):
    model = Post
    template_name = 'details.html'