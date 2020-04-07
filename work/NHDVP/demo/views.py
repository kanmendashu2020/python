from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from utils import models,ProjectPagination
from rest_framework import serializers
import json
from collections import OrderedDict


# Create your views here.


# 序列化指定类
class TSysUserSerializers(serializers.ModelSerializer):
    class Meta:
        # 序列化指定类
        model = models.TSysUser
        fields = "__all__"


class testDataView(APIView):

    def get(self, *args, **kwargs):
        try:
            # 查询条件
            ModelsObjects = models.TSysUser.objects.all()
            # 分页
            page_object = ProjectPagination.get_page_object(queryset=ModelsObjects, request=self.request, view=self)
            SerializerData = TSysUserSerializers(instance=page_object, many=True).data
            # 不分页
            # SerializerData = TSysUserSerializers(instance=ModelsObjects, many=True).data
            # 状态码自定义
            code = 200
        except:
            SerializerData = 0
            code = 400
        # 带状态码格式化
        ResultJson = {
            'code': code,
            'data': SerializerData,

        }
        # 序列化返回结果
        res = json.dumps(ResultJson, ensure_ascii=False)

        return HttpResponse(res)

# 返回html页面
class testHtmlView(APIView):
    # 方法名==请求方法：
    # http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
    def get(self,*args,**kwargs):
        return render(self.request, template_name='html/demo/test.html')
