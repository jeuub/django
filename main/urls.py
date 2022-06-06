from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorsViewSet, QuizViewSet, GetQuizView, CategotiesViewSet, GetCategotiesView

router = DefaultRouter()
router.register('quiz', QuizViewSet, )
router.register('categories', CategotiesViewSet, )
router.register('authors', AuthorsViewSet, )


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/quiz/filter', GetQuizView.as_view()),
    path('api/categories/filter', GetCategotiesView.as_view()),
]
