from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Company, Employee
from .serializers import CompanySerializer, EmployeeSerializer

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

#companies/{id}/employees/
    @action(detail=True, methods=['GET'])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            employee = Employee.objects.filter(company=company)
            emp_data = EmployeeSerializer(employee, many=True, context={"request":request})
            return Response(emp_data.data)
        except Exception as e:
            print(e)
            return Response({
                "message":"Not Found"
            })
        

        



class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


"""
EmployeeSerializer(<QuerySet [<Employee: Employee object (1)>, <Employee: Employee object (2)>]>, context={'request': <rest_framework.request.Request: GET '/api/v1/companies/1/employees/'>}, many=True):
    url = HyperlinkedIdentityField(view_name='employee-detail')
    employee_id = ReadOnlyField()
    name = CharField(max_length=100)
    email = CharField(max_length=60)
    address = CharField(max_length=100)
    phone = CharField(max_length=20)
    about = CharField(style={'base_template': 'textarea.html'})
    position = ChoiceField(choices=(('SoftwareDeveloper', 'SD'), ('Manager', 'Manager'), ('TeamLeader', 'TL')))
    company = HyperlinkedRelatedField(queryset=Company.objects.all(), view_name='company-detail')


"""