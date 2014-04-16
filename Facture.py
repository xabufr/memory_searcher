from mongoengine import *


class Facture(Document):
    montant = FloatField(required=True)
