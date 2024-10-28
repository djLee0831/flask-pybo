from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\x11A\x9fpZ\x9e\x1fZ\x88\x82y\x02\xe6\xf2\x97\xfa'
