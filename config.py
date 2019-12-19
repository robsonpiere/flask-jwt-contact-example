class Config:
    SECRET_KEY = b'Q\xa5\xb6\x0c\xdc\xe9\xba\xf8e\xb6\xec{\x0e\x95r\x88C\x82:\xb0\xc0\xd1\xf0x'
    SQLALCHEMY_DATABASE_URI = "sqlite:///C:\\database/contacts.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Development(Config):
    Debug=True

class Testing(Config):
    pass

config = {
    'development' : Development,
    'testing' : Testing
}