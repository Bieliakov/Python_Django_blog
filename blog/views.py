from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.views import generic

from django.http import HttpResponse

from .models import Post

#class BlogIndex(generic.ListView):
#    queryset = models.Entry.objects.published()
#    template_name = 'home.html'
#    paginate_by = 2

def index(request):
    latest_post_list = Post.objects.order_by('-post_pub_date')[:5]
    context = { 'latest_post_list': latest_post_list }
    return render(request, 'blog/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})

def comment(request, post_id):
    response = "You're looking at the comment %s."
    return HttpResponse(response % post_id)
"""

    Blog homepage – displays the latest few entries.
    Entry “detail” page – permalink page for a single entry.
    Year-based archive page – displays all months with entries in the given year.
    Month-based archive page – displays all days with entries in the given month.
    Day-based archive page – displays all entries in the given day.
    Comment action – handles posting comments to a given entry.

"""