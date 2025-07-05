from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, ExpenseIncomeViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('expenses', ExpenseIncomeViewSet, basename='expenses')

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls
