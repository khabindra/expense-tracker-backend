from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import ExpenseIncome
from .serializers import ExpenseIncomeSerializer, RegisterSerializer
from .permissions import IsOwnerOrSuperUser

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExpenseIncomeViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseIncomeSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrSuperUser]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return ExpenseIncome.objects.all().order_by('-created_at')
        return ExpenseIncome.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
