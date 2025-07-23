from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.db import models
from django.db.models.functions import Lower
from .models import Song
from .serializers import SongSerializer

class SongListView(APIView):
    def get(self, request):
        items = Song.objects.all()

        # Filtering
        search_query = request.query_params.get('search', None)
        if search_query:
            items = items.filter(
                models.Q(title__icontains=search_query) |
                models.Q(artist__icontains=search_query) |
                models.Q(album__icontains=search_query)
            )

        # Sorting
        sort_by = request.query_params.get('ordering', 'id')
        valid_fields = ['title', 'artist', 'album', 'year', 'stream']
        if sort_by.lstrip('-') in valid_fields:
            if sort_by.lstrip('-') == 'title':
                items = items.annotate(lower_title=Lower('title')).order_by(f"{'-' if sort_by.startswith('-') else ''}lower_title")
            else:
                items = items.order_by(sort_by)

        # Pagination
        perpage = request.query_params.get('perpage', default=7)
        paginator = PageNumberPagination()
        paginator.page_size = int(perpage)
        paginated_items = paginator.paginate_queryset(items, request)
        serializer = SongSerializer(paginated_items, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SongDetailView(APIView):
    def get(self, request, pk):
        try:
            item = Song.objects.get(pk=pk)
            serializer = SongSerializer(item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Song.DoesNotExist:
            return Response({"detail": "Record Not Found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            item = Song.objects.get(pk=pk)
            serializer = SongSerializer(item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Song.DoesNotExist:
            return Response({"detail": "Record Not Found"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        try:
            item = Song.objects.get(pk=pk)
            serializer = SongSerializer(item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Song.DoesNotExist:
            return Response({"detail": "Record Not Found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            item = Song.objects.get(pk=pk)
            item.delete()
            return Response({"detail": "Record Successfully Deleted"}, status=status.HTTP_200_OK)
        except Song.DoesNotExist:
            return Response({"detail": "Record Not Found"}, status=status.HTTP_404_NOT_FOUND)