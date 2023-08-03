from re import T
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

class CustomPagination(LimitOffsetPagination):
    def get_paginated_response(self, data):
        data['links'] = {'next': self.get_next_link(),
                         'previous': self.get_previous_link()}
        data['count'] = self.count
        return Response(data)
