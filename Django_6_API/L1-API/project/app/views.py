from django.http import JsonResponse
from app.models import WatchList,StreamPlatform
from app.serializers import WatchListSerializer,StreamPlatformSerialize
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

def movie_list(request):
    movie_lists = WatchList.objects.all()
    serialized = WatchListSerializer(movie_lists, many = True)
    print(serialized.data)
    print("-----------------")
    print(movie_lists)
    return JsonResponse(serialized.data, safe=False)

def movie_detail(request,pk):
    movie = WatchList.objects.get(pk=pk)
    print(movie)
    serialized = WatchListSerializer(movie)
    print("================================")
    print(serialized.data)
    return JsonResponse(serialized.data , safe=False)


@api_view(['GET', 'POST'])
def stream_list(request):
    if request.method == "GET":
        stream_lists = StreamPlatform.objects.all()
        serialized = StreamPlatformSerialize(stream_lists, many=True)
        return Response(serialized.data)

    elif request.method == "POST":
        back_end_data = request.data  # Ese backend se data la raha hai :
        serialized =  StreamPlatformSerialize(data = back_end_data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


def stream_detail(request,pk):
    stream_details = StreamPlatform.objects.get(pk = pk)
    print(stream_details)
    serialized = StreamPlatformSerialize(stream_details)
    print("+++++++++++++++++++++++++++")
    print(serialized.data)
    return JsonResponse(serialized.data)