from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import View

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import ArticleModelForm

from .models import Article

# Create your views here.
# Class based view as opposed to function based view in Products
class ArticleListView(ListView):
    template_name = 'blog/article_list.html'
    #queryset = Article.objects.all() # By default template searched for is like - <appname>/<modelName>_<viewName>.html. Example: blog/article_list.html

    # get_queryset() is called for every GET request on /blogs endpoint
    # So, if we don't define get_queryset() here but instead just have queryset
    # field above(line 21 uncommented), then new object created by ArticleCreateView
    # will not show up in list call until we restart the server using "python manage.py runserver"
    def get_queryset(self):
        return Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = 'blog/article_detail.html'
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id") # To get the value for id passed in input URL
        return get_object_or_404(Article, id=id_)

class ArticleCreateView(CreateView):
    template_name = 'blog/article_create.html'
    queryset = Article.objects.all()
    form_class = ArticleModelForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    template_name = 'blog/article_create.html'
    queryset = Article.objects.all()
    form_class = ArticleModelForm

    # To get a particular object to update
    def get_object(self):
        id_ = self.kwargs.get("id") # To get the value for id passed in input URL
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = 'blog/article_delete.html'
    #success_url = '/'

    def get_object(self):
        id_ = self.kwargs.get("id") # To get the value for id passed in input URL
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse("articles:article-list")


# Another way to define a "single" view class with all
# views defined as Class method based views.
class Article1ListView(View):
    template = "blog/article_list.html"
    all_objects = Article.objects.all()
    context = {
        "object_list": all_objects
    }

    # This one is for list view
    # Note: Here the name of the method should match the HTTP method name
    def get(self, request, *args, **kwargs):
        print(self.context)
        return render(request, self.template, self.context)

    def get_queryset(self):
        all_objects = Article.objects.all()
        context = {
            "object_list": all_objects
        }
        return context


class Article1DetailView(View):
    template = "blog/article_detail.html"
    context = {}

    # This one is for detail view
    def get(self, request, id=None, *args, **kwargs):
        self.context = {
            'object': get_object_or_404(Article, id=id)
        }
        return render(request, self.template, self.context)

class Article1CreateView(View):
    template = "blog/article_detail.html"
    context = {}

    def get(self, request, *args, **kwargs):
        # GET method to render the empty create form
        form = ArticleModelForm()
        self.context = {"form": form}
        return render(request, self.template, self.context)

    def post(self, request, *args, **kwargs):
        form = ArticleModelForm(request.POST)
        if form.is_valid():
            form.save()
        self.context = {"form": form}
        return render(request, self.template, self.context)

class Article1UpdateView(View):
    template = "blog/article_update.html"
    context = {}
    def get_object(self):
        id = self.kwargs.get('id')
        if id is not None:
            obj = get_object_or_404(Article, id=id)
            # self.context = {
            #     'object': obj
            # }
        return obj

    def get(self, request, *args, **kwargs):
        # GET method to render the empty create form
        obj = self.get_object()
        if obj is not None:
            # By passing instance=obj, it'll fill the form with
            # existing obj field values
            form = ArticleModelForm(instance=obj)
            self.context = {
                'form': form,
                'object': obj
            }
        print(obj.title)
        print(self.context)
        return render(request, self.template, self.context)

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj is not None:
            form = ArticleModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            self.context = {
                'form': form,
                'object': obj
            }
        return render(request, self.template, self.context)




