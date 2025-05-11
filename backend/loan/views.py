from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import LoanSerializer
from loan.models import Qist
from django.db.models import Sum

# Create your views here.

@api_view(['GET'])
def home_content(request):

    qist=Qist.objects.all()
    qists_count=Qist.objects.count() 

    total_loan = 974000
    paid_loan = Qist.objects.aggregate(Sum('amount'))['amount__sum'] or 0 
    remaining_loan=total_loan-paid_loan
    paid_percentage = int((paid_loan / total_loan) * 100)
    unpaid_percentage = int(100 - paid_percentage) 
    
    
    return Response({
        'total_loan': total_loan,
        'paid_loan': paid_loan,
        'remaining_loan':remaining_loan,
        'paid_percentage':paid_percentage,
        'unpaid_percentage':unpaid_percentage,
        'qists_count':qists_count
    })




@api_view(['POST'])
def add_qist(request):
    serializer = LoanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)



@api_view(['GET'])
def get_all_qist(request):
    qist = Qist.objects.all().order_by('-id')
    serializer = LoanSerializer(qist, many=True)
    return Response(serializer.data)
