from django.http import HttpResponse
from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = '我的第一个网页!'
    context['hello2'] = 'Apple'
    return render(request, 'hello.html', context)



# def render(request, file_name, value_dict):
#     with open(dir + file_name) as f:
#         str_file = f.read()
#
#         struct = decode(str_file)
#         for key in value_dict.keys():
#             value = value_dict[key]
#             if find(struct, key)==True: