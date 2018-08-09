# -*- coding: utf-8 -*-
#  SXShop  ---  2018/5/17  ---  PyCharm
__author__ = 'lishunfeng'


# from __future__ import unicode_literals


from rest_framework.settings import api_settings
from rest_framework import exceptions
from rest_framework import status, viewsets
from rest_framework.response import Response

class mCreateModelMixin(object):
    """
    Create a model instance.
    """

    def handle_exception(self, exc):
        """
        Handle any exception that occurs, by returning an appropriate response,
        or re-raising the error.
        """
        if isinstance(exc, (exceptions.NotAuthenticated,
                            exceptions.AuthenticationFailed)):
            # WWW-Authenticate header for 401 responses, else coerce to 403
            auth_header = self.get_authenticate_header(self.request)
            if auth_header:
                exc.auth_header = auth_header
            else:
                exc.status_code = status.HTTP_403_FORBIDDEN
        exception_handler = self.settings.EXCEPTION_HANDLER
        context = self.get_exception_handler_context()
        response = exception_handler(exc, context)
        if response is None:
            self.raise_uncaught_exception(exc)
        response.exception = True
        response.data = {
            'msg': list(response.data.values())[0],
            'code': response.status_code,
            'data': {}
        }
        response.status_code = status.HTTP_200_OK
        return response

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
                "msg": "create success",
                "code": 200,
                "data": serializer.data
            }, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}



class mListModelMixin(object):

    def handle_exception(self, exc):
        """
        Handle any exception that occurs, by returning an appropriate response,
        or re-raising the error.
        """
        if isinstance(exc, (exceptions.NotAuthenticated,
                            exceptions.AuthenticationFailed)):
            # WWW-Authenticate header for 401 responses, else coerce to 403
            auth_header = self.get_authenticate_header(self.request)
            if auth_header:
                exc.auth_header = auth_header
            else:
                exc.status_code = status.HTTP_403_FORBIDDEN
        exception_handler = self.settings.EXCEPTION_HANDLER
        context = self.get_exception_handler_context()
        response = exception_handler(exc, context)
        if response is None:
            self.raise_uncaught_exception(exc)
        response.exception = True
        response.data = {
            'msg': list(response.data.values())[0],
            'code': response.status_code,
            'data': {}
        }
        response.status_code = status.HTTP_200_OK
        return response

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({
                "msg": "list success",
                "code": 200,
                "data": serializer.data
            })



class mRetrieveModelMixin(object):
    """
    Retrieve a model instance.
    """
    def handle_exception(self, exc):
        """
        Handle any exception that occurs, by returning an appropriate response,
        or re-raising the error.
        """
        if isinstance(exc, (exceptions.NotAuthenticated,
                            exceptions.AuthenticationFailed)):
            # WWW-Authenticate header for 401 responses, else coerce to 403
            auth_header = self.get_authenticate_header(self.request)
            if auth_header:
                exc.auth_header = auth_header
            else:
                exc.status_code = status.HTTP_403_FORBIDDEN
        exception_handler = self.settings.EXCEPTION_HANDLER
        context = self.get_exception_handler_context()
        response = exception_handler(exc, context)
        if response is None:
            self.raise_uncaught_exception(exc)
        response.exception = True
        response.data = {
            'msg': list(response.data.values())[0],
            'code': response.status_code,
            'data': {}
        }
        response.status_code = status.HTTP_200_OK
        return response

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
                "msg": "retrieve success",
                "code": 200,
                "data": serializer.data
            })


class mUpdateModelMixin(object):
    def handle_exception(self, exc):
        """
        Handle any exception that occurs, by returning an appropriate response,
        or re-raising the error.
        """
        if isinstance(exc, (exceptions.NotAuthenticated,
                            exceptions.AuthenticationFailed)):
            # WWW-Authenticate header for 401 responses, else coerce to 403
            auth_header = self.get_authenticate_header(self.request)
            if auth_header:
                exc.auth_header = auth_header
            else:
                exc.status_code = status.HTTP_403_FORBIDDEN
        exception_handler = self.settings.EXCEPTION_HANDLER
        context = self.get_exception_handler_context()
        response = exception_handler(exc, context)
        if response is None:
            self.raise_uncaught_exception(exc)
        response.exception = True
        response.data = {
            'msg': list(response.data.values())[0],
            'code': response.status_code,
            'data': {}
        }
        response.status_code = status.HTTP_200_OK
        return response
    """
    Update a model instance.
    """
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
            instance = self.get_object()
            serializer = self.get_serializer(instance)

        return Response({
                "msg": "update success",
                "code": 200,
                "data": serializer.data
            })

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class mDestroyModelMixin(object):
    def handle_exception(self, exc):
        """
        Handle any exception that occurs, by returning an appropriate response,
        or re-raising the error.
        """
        if isinstance(exc, (exceptions.NotAuthenticated,
                            exceptions.AuthenticationFailed)):
            # WWW-Authenticate header for 401 responses, else coerce to 403
            auth_header = self.get_authenticate_header(self.request)
            if auth_header:
                exc.auth_header = auth_header
            else:
                exc.status_code = status.HTTP_403_FORBIDDEN
        exception_handler = self.settings.EXCEPTION_HANDLER
        context = self.get_exception_handler_context()
        response = exception_handler(exc, context)
        if response is None:
            self.raise_uncaught_exception(exc)
        response.exception = True
        response.data = {
            'msg': list(response.data.values())[0],
            'code': response.status_code,
            'data': {}
        }
        response.status_code = status.HTTP_200_OK
        return response
    """
    Destroy a model instance.
    """
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        serializer = self.get_serializer(instance)
        return Response({
                "msg": "destroy success",
                "code": 200,
                "data": serializer.data
            },status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()



class CustomModelViewSet(viewsets.ModelViewSet):
    def handle_exception(self, exc):
        """
        Handle any exception that occurs, by returning an appropriate response,
        or re-raising the error.
        """
        if isinstance(exc, (exceptions.NotAuthenticated,
                            exceptions.AuthenticationFailed)):
            # WWW-Authenticate header for 401 responses, else coerce to 403
            auth_header = self.get_authenticate_header(self.request)
            if auth_header:
                exc.auth_header = auth_header
            else:
                exc.status_code = status.HTTP_403_FORBIDDEN
        exception_handler = self.settings.EXCEPTION_HANDLER
        context = self.get_exception_handler_context()
        response = exception_handler(exc, context)
        if response is None:
            self.raise_uncaught_exception(exc)
        response.exception = True
        response.data = {
            'msg': list(response.data.values())[0],
            'code': response.status_code,
            'data': {}
        }
        response.status_code = status.HTTP_200_OK
        return response

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                "msg": "create success",
                "code": 200,
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            {
                "msg": "retrieve success",
                "code": 200,
                "data": serializer.data
            }
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # refresh the instance from the database.
            instance = self.get_object()
            serializer = self.get_serializer(instance)

        return Response(
            {
                "msg": "update success",
                "code": 200,
                "data": serializer.data
            }
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        self.perform_destroy(instance)
        return Response(
            {
                "msg": "destroy success",
                "code": 200,
                "data": serializer.data
            }
        )
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({
                "msg": "list success",
                "code": 200,
                "data": serializer.data
            })