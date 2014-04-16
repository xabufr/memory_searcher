from mongoengine import *
from Facture import Facture

class Avatar(EmbeddedDocument):
    username = StringField(required=True)
    phone = StringField()


class Settings(EmbeddedDocument):
    languages = ListField(StringField())
    timezone = StringField(required=False)


class User(Document):
    avatar = EmbeddedDocumentField(Avatar)
    settings = EmbeddedDocumentField(Settings)
    factures = ListField(ReferenceField(Facture))
