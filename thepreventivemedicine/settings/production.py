
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEBUG = True
ALLOWED_HOSTS = ['www.thepreventivemedicine.com', 'thepreventivemedicine.com']
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_ROOT  = os.path.join(BASE_DIR, 'media')
