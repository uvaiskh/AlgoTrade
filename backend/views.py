
from rest_framework import generics, status
from rest_framework.response import Response



class TestView(generics.ListAPIView):

    def list(self, request, *args, **kwargs):
        return Response({"status": True, "message": "Success", "data": {"Test paased"}}, status=status.HTTP_201_CREATED)