# -*- coding:utf-8 -*-

import os, sys
from django.views.debug import technical_404_response
from django.conf import settings
from django.http.response import HttpResponseForbidden


class BlockIpMiddleware(object):
    def process_request(self, request):
        if request.META['REMOTE_ADDR'] in getattr(settings, 'BLOCK_IPS', []):
            return HttpResponseForbidden('<h1>Forbidden</h1>')


class UserBasedExceptionMiddleware(object):
    def process_exception(self, request, exception):
        if request.user.is_superuser or request.META.get('REMOTE_ADDR') in settings.INTERNAL_IPS:
            return technical_404_response(request, *sys.exc_info())