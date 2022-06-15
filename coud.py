import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from cloud_meta import CloudMeta


class Cloud(metaclass=CloudMeta):

    def __init__(self):
        self.__firebase_sdk = credentials.Certificate('logger-bd28c-firebase-adminsdk-ima1q-97aabfd0dc.json')
        firebase_admin.initialize_app(self.__firebase_sdk, {'databaseURL':
                                                            'https://logger-bd28c-default-rtdb.firebaseio.com'})
        self.__ref = db.reference('/Logs')

    def msg(self, mensaje: str):
        self.__ref.push({'Mensaje': mensaje})
        return "Guardado"

    def success(self):
        self.__ref.push({'Tipo': 'Success'})
        return "Advertencia"

    def warning(self):
        self.__ref.push({'Tipo': 'Advertencia'})
        return "Advertencia"

    def error(self):
        self.__ref.push({'Tipo': 'Error'})
        return "Error"
