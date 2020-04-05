from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView


# Create your views here.

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
