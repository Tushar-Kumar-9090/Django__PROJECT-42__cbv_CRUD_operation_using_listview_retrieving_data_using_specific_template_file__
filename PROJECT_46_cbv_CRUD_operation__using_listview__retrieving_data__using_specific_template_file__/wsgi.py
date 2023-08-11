"""
WSGI config for PROJECT_46_cbv_CRUD_operation__using_listview__retrieving_data__using_specific_template_file__ project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PROJECT_46_cbv_CRUD_operation__using_listview__retrieving_data__using_specific_template_file__.settings')

application = get_wsgi_application()
