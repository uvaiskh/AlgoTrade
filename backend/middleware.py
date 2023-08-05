import json
import traceback

import jwt
from django.urls import resolve
import re

from .models import *
# from common import constants
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from conf import SUPER_USER_PASSWORD, SUPER_USER_NAME, ACCESS_TOKEN_SECRET
from common.constants import UrlNames



class AuthMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        super().__init__(get_response)
        self.get_response = get_response

    def process_request(self, request):

        request.Language = request.headers.get('Accept-Language', 'en')
        exclusion_list = [UrlNames.Login, UrlNames.Test, UrlNames.Tokens, UrlNames.Orders]
        try:
            url_obj = resolve(request.path)
            url_name = url_obj.url_name
        except:
            return JsonResponse({'status': 'false', 'message': "Not Found"}, status=404)
        if url_name not in exclusion_list:
            try:
    
                method = request.method
                token = request.headers.get('Authorization')
                payload = jwt.decode(token, ACCESS_TOKEN_SECRET, algorithms=["HS256"])
                user_type = payload['user_type']
                user_id = payload['id']
                request.userId = user_id
                request.userType = user_type
                request.isSuperUser = False
                # if bool(BlackListedTokens.objects.filter(token=token)):
                #     return JsonResponse({'status': False, 'message': "Token is Invalid/Expired"}, status=403)
                # if url_name in [UrlNames.Profile, UrlNames.ChangePassword, UrlNames.EditProfile, UrlNames.ChangeEmail, UrlNames.ConfirmEmail]:
                #     return self.get_response(request)

                # if url_name == UrlNames.Logout:
                #     request.Token = token
                #     return self.get_response(request)

                # user_data = Users.objects.get(id=user_id)
                # if user_data.__dict__.get('is_super_user'):
                #     request.isSuperUser = True
                #     return self.get_response(request)
                    
                # role_id = user_data.role_id.id
                # feature_ids = list(RoleFeatures.objects.filter(role_id=role_id).values_list('feature_id', flat=True))


                # request.functionalFeatures = [value for name, value in vars(FunctionalFeatures).items() if not name.startswith("__") if value in feature_ids]
                
                # if not bool(FeaturePermissions.objects.select_related('permission_id')
                #                     .filter(feature_id__in=feature_ids, permission_id__url_name=url_name,
                #                             permission_id__method=method)):
                #     return JsonResponse({'status': False, 'message': "Permission Denied"}, status=403)

                # else:
                    # return self.get_response(request)
                return self.get_response(request)
            except (jwt.ExpiredSignatureError, jwt.DecodeError, jwt.InvalidTokenError) as e:
                return JsonResponse({'status': False, 'message': "Token is Invalid/Expired"}, status=403)
            except Exception as e:
                print(e, traceback.format_exc())
                return JsonResponse({'status': False, 'message': "Invalid User"}, status=403)
        else:
            return self.get_response(request)
