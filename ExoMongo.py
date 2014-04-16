from mongoengine import *
from User import User, Avatar, Settings
from Facture import Facture

db = connect("coucou")

User.drop_collection()

avatar = Avatar(username="toto", phone="9876543210")
settings = Settings(languages=['fr', 'en'], timezone="Paris")
user = User(avatar=avatar, settings=settings)
user.save()

facture1 = Facture(montant=100.0, user=user)
facture1.save()
facture2 = Facture(montant=107.1, user=user)
facture2.save()
user.factures.append(facture1)
user.save()
user.factures.append(facture2)
user.save()

avatar = Avatar(username="titi", phone="0123456789")
settings = Settings(languages=['fr', 'en'], timezone="London")
user = User(avatar=avatar, settings=settings)
user.save()

print(User.objects.item_frequencies('settings.timezone'))


