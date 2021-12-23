from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, UpdateView
from rest_framework import authentication, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.response import Response


# UI 설정부분
from rest_framework.views import APIView

from accountapp.models import NewModel
from accountapp.permission import IsOwner
from accountapp.seriallizers import NewModelSerializer, UserSerializer, UserWithoutPasswordSerializer


def hello_world_template(request):
    return render(request, 'accountapp/hello_world.html')



# 로직 처리부분
@api_view(['GET', 'POST'])
def hello_world(request):

    if request.method == 'POST':
        input_data = request.data.get('input_data')

        new_model = NewModel()
        new_model.text = input_data
        new_model.save()

        #먹는 시리얼
        serializer = NewModelSerializer(new_model)


        return Response(serializer.data)

    new_model_list = NewModel.objects.all()
    seriallizer = NewModelSerializer(new_model_list,many=True)


    return Response(seriallizer.data)

def AccountCreateTemplate(request):
    return render(request, 'accountapp/create.html')


class AccountCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []


def AccountLoginView(request):
    return render(request, 'accountapp/login.html')


class AccountRetrieveTemplateView(TemplateView):
    template_name = 'accountapp/retrieve.html'



class AccountUpdateTemplateView(TemplateView):
    template_name = 'accountapp/update.html'




class AccountDestoryTemplateView(TemplateView):
    template_name= 'accountapp/destroy.html'

class AccountRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserWithoutPasswordSerializer
    permission_classes = [IsOwner]
    authentication_classes = [TokenAuthentication]


    def get(self,request,*args,**kwargs):
        instance = self.get_object() # 이거는User 이거 값 가져오는거 맞나요? 아 객체 예제로 치면 [user,ss,aa,] 그런 담고잇는 객체로 이해하면 되죠?
        serializer = self.get_serializer(instance)
        #여거 두개는 페이지의 값을 객체화 시켯군요

        result_dict = dict(serializer.data) #애는 그래서 임시로 만든 데이터 타입이라고 이해하면 되나요?
        #만약 지금 test6(다른사용자)가 test7(현재페이지) detail 정보를 열람할때 -> 열람하는 사람이 서버로 요청을 보내겠죠?
        #instance 는 test7이 되고 request.user는  test6이 되나요? 아 그렇군요 위에 잇는
        if request.user == instance :
            result_dict['is_page_owner'] = 'True'
        else:
            result_dict['is_page_owner'] = 'False'
        return Response(result_dict)

class AccountTokenRetrieveAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    http_method_names = ['get']

    def get(self,request,*args,**kwargs):
        serializer = UserWithoutPasswordSerializer(request.user)
        return Response(serializer.data)