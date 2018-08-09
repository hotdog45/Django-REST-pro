"""
WSGI config for SXShop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
os.environ['PYTHON_EGG_CACHE'] = '/<a path>/.python-eggs/' #为了防止Permission denied的web请求访问错误。
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SXShop.settings")
application = get_wsgi_application()


# import os
# import sys
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SXShop.settings")
# try:
#     from django.core.management import execute_from_command_line
# except ImportError:
#     # The above import may fail for some other reason. Ensure that the
#     # issue is really that Django is missing to avoid masking other
#     # exceptions on Python 2.
#     try:
#         import django
#     except ImportError:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         )
#     raise
# execute_from_command_line(sys.argv)