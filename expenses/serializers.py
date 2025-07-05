from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ExpenseIncome

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class ExpenseIncomeSerializer(serializers.ModelSerializer):
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = ExpenseIncome
        fields = [
            'id', 'title', 'description', 'amount',
            'transaction_type', 'tax', 'tax_type',
            'total', 'created_at', 'updated_at'
        ]
