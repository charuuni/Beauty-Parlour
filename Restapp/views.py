from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import*
from django.views.decorators.csrf import csrf_exempt

from .serializers import ArticleSerializer
@csrf_exempt
def Article_list(request):
    return request.method
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def article_detail(request,pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# @csrf_exempt
# def Demo_list(request):
#     if request.method=='GET':
#         Demos=Demo.objects.all()
#         serializer=DemoSerializer(Demos,many=True)
#         return JsonResponse(serializer.data,safe=False)
#     elif request.method=='POST':
#         data=JSONParser().parse(request)
#         serializer=DemoSerializer(data=data)
#         if serializer.is_valid ():
#             serializer.save()
#             return JsonResponse(serializer.data,status=201)
#         return JsonResponse(serializer.errors,status=400)
