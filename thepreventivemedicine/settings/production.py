
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEBUG = False
ALLOWED_HOSTS = [ '74.207.251.101','www.thepreventivemedicine.com', 'thepreventivemedicine.com']
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
