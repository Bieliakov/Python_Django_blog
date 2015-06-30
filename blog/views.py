from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.views import generic

from .models import Post, Category,Tag

from blog.forms import UserForm, UserProfileForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
'''
Write your views¶

Each view is responsible for doing one of two things: Returning an HttpResponse object containing the content for the requested page, or raising an exception such as Http404. The rest is up to you.

Generally, a view retrieves data according to the parameters, loads a template and renders the template with the retrieved data. Here’s an example view for year_archive from above:
mysite/news/views.py

from django.shortcuts import render

from .models import Article

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)
    
https://docs.djangoproject.com/en/1.7/intro/overview/
по годовым архивам примеры + пример тимплейта
'''
'''
def home(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:3]
    #categories = []
    #for post in latest_post_list:
    #    category = Category.objects.select_related().get(slug=category_slug)
    latest_comments_list = Comment.objects.order_by('-pub_date')[:3]
    
    
    return render(request, 'blog/index.html', { 'latest_post_list': latest_post_list, 'categories': categories})
'''

categories = Category.objects.all()
three_last_posts = Post.objects.order_by('-pub_date')[:3]

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')

def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print (user_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render( request,
            'blog/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/blog/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your blog account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'blog/login.html', {})

def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    #categories = []
    #for post in latest_post_list:
    #    category = Category.objects.select_related().get(slug=category_slug)
   
    return render(request, 'blog/index.html', { 'latest_post_list': latest_post_list, 'categories': categories, 'three_last_posts': three_last_posts})

def detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    #categories_intermediate = Post_has_categories.objects.filter(post_id_id=post_id) 

    return render(request, 'blog/detail.html', {'post': post, 'categories': categories, 'three_last_posts': three_last_posts})

    
    
def category(request, category_slug):
    category = Category.objects.select_related().get(slug=category_slug)
    posts = category.post_set.all()
    
    return render(request, 'blog/category.html', {'posts': posts, 'category': category, 'categories': categories, 'three_last_posts': three_last_posts})

    '''
    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}
    
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_slug)
        context_dict['category_name'] = category.name
        
        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        posts = Post.objects.filter(category=category)
        
        # Adds our results list to the template context under name pages.
        context_dict['posts'] = posts
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass
    
    # Go render the response and return it to the client.
    return render(request, 'blog/category.html', context_dict)
    # делаем выборку выбранной категории
    '''
    '''category = get_object_or_404(Category, slug = 'new-category')
    #category = Category.objects.select_related().get(slug = category_slug) 
    # выбираем все статьи по выбранной категории
    posts = category.post_set.all() 
    # возвращаем выбранную категорию и статьи в шаблон category.html
    return render(request, 'category.html', {'posts': posts, 
                                            'category': category})
    '''


def tag (request, tag_slug):
    tag = Tag.objects.select_related().get(slug=tag_slug)
    posts = tag.post_set.all()

    return render(request, 'blog/tagpage.html', {'posts': posts, 'tag': tag, 'categories': categories, 'three_last_posts': three_last_posts})


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