import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'k#p)dstl)w9z$ry1u@cy1shkw$pp0sjhu-ay-ym_fq_fv0a+25' #追加

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'reddit_clone',
        'USER': 'root',
        'HOST': '',
        'PORT': '',
    }
}

DEBUG = True