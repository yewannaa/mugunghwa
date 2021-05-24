# from django.shortcuts import render

# # Create your views here.

# def post_list(request):
#     return render(request, 'blog/post_list.html', {})





from django.http import HttpResponse
from django.template import loader



def post_list(request):
    template = loader.get_template('blog/post_list.html')
    context = {
    }
    return HttpResponse(template.render(context, request))