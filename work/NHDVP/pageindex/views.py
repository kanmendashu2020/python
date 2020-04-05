from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination


# Create your views here.

class MyPage(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'size'
    max_page_size = 5
    page_query_param = 'page'

class testView(APIView):
    def get(self, *args, **kwargs):
        # 返回非json数据
        # a = 9
        # return JsonResponse(a,safe=False)
        # 返回json类型数据
        # a = {'data': 9}
        # return JsonResponse(a)
        # 返回页面
        return render(self.request, template_name='pageindex/test.html')
