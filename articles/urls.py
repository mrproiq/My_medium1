from django.urls import path
from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticleCreateView,
    AddCommentView,
)

urlpatterns = [
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name = 'article_edit'),
    path('<int:pk>/', ArticleDetailView.as_view(), name = 'article_detail'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name = 'article_delete'),
    path('create/', ArticleCreateView.as_view(), name = 'article_create'),
    path('', ArticleListView.as_view(), name = 'article_list'),
    path('<int:pk>/comment/', AddCommentView.as_view(), name = 'add_comment'),
]