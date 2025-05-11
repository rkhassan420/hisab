from .models import Qist
from rest_framework import serializers

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model=Qist
        fields='__all__'
