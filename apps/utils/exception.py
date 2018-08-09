# -*- coding: utf-8 -*-
#  SXShop  ---  2018/5/17  ---  PyCharm
__author__ = 'lishunfeng'

from rest_framework.views import exception_handler
from rest_framework import exceptions, status
from rest_framework.request import Request
from rest_framework.response import Response
from django.db import connection, models, transaction
from django.http import Http404
from django.utils import six
from django.core.exceptions import PermissionDenied


# def custom_exception_handler(exc, context):
#     # Call REST framework's default exception handler first,
#     # to get the standard error response.
#     response = exception_handler(exc, context)
#
#     # Now add the HTTP status code to the response.
#     if response is not None:
#         response.data['code'] = response.status_code
#         if exc is not None:
#             response.data['msg'] = ""
#     return response

def custom_exception_handler(exc, context):

    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        if isinstance(exc.detail, (list)):
            # data = exc.detail
            data = {'msg': exc.detail[0]}
        elif  isinstance(exc.detail, ( dict)):
            for k, v in exc.detail.items():
                if isinstance(v, (list)):
                    data = {'msg': v[0]}
                else:
                    data = {'msg': v}
        else:
            data = {'msg': exc.detail}

        set_rollback()
        data['code'] = exc.status_code
        data['data'] = {}
        return Response(data, status=exc.status_code, headers=headers)

    elif isinstance(exc, Http404):
        # msg = _('Not found.')
        data = {'msg': 'Not found.'}

        set_rollback()
        data['code'] = 404
        data['data'] = context
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    elif isinstance(exc, PermissionDenied):
        # msg = _('Permission denied.')
        # data = {'msg': six.text_type(msg)}
        data = {'msg': '没有权限'}
        set_rollback()
        data['code'] = exc.status_code
        data['data'] = {}
        return Response(data, status=status.HTTP_403_FORBIDDEN)
    return None

def set_rollback():
    atomic_requests = connection.settings_dict.get('ATOMIC_REQUESTS', False)
    if atomic_requests and connection.in_atomic_block:
        transaction.set_rollback(True)