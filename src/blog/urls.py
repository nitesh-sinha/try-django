from django.urls import path
from .views import ArticleListView, ArticleDetailView, \
                    ArticleCreateView, ArticleUpdateView, \
                    ArticleDeleteView, Article1ListView, Article1DetailView, Article1CreateView, Article1UpdateView

app_name = "articles"
urlpatterns = [
    # By default we need to use "pk" instead of "id", but to use "id" we need to add get_object() in our blog views.py
    #path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    #path('', ArticleListView.as_view(), name='article-list'),
    #path('create/', ArticleCreateView.as_view(), name='article-create'),
    #path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),

    # Another way to create view classes by inheriting from View class
    path('', Article1ListView.as_view(template='blog/article_list.html'), name='article-list'),
    path('<int:id>/', Article1DetailView.as_view(template='blog/article_detail.html'), name='article-detail'),
    path('create/', Article1CreateView.as_view(), name='article-create'),
    path('<int:id>/update/', Article1UpdateView.as_view(), name='article-update'),
]