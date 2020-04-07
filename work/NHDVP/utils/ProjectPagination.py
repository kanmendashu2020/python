# -*- coding: utf-8 -*-
# @Time : 2020/4/7 11:18
# @Author : lzf
# @File : ProjectPagination.py
# @Software: PyCharm
# @Description: 分页查询工具

from rest_framework.pagination import PageNumberPagination


# 分页
# 教程：https://www.cnblogs.com/welan/p/9952801.html
class ProjectPage(PageNumberPagination):
    # 每页默认的个数
    page_size = 10
    page_size_query_param = 'size'
    max_page_size = 100
    # 页数参数名
    page_query_param = 'page'

def get_page_object(queryset, request, view):
    page = ProjectPage()
    page_objects = page.paginate_queryset(queryset=queryset, request=request, view=view)
    return page_objects


