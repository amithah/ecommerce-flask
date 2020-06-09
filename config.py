import os
class Configuration(object):
    DEBUG=True
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))

    STATIC_DIR = os.path.join(APPLICATION_DIR, 'static')
    IMAGES_DIR = os.path.join(STATIC_DIR, 'images')
    





