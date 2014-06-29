memory_searcher
===============

#Fonctionnement

## Indexation
Le script logic/add_folder.py ajoute tous les PDF présents dans les dossiers spécifiés en entrée dans une file de traitement Redis local.
Le script locig/process_jobs.py récupère le prochain PDF à traiter et lance l'extraction (jusqu'à ce que la file de traitement soit vide).

## Service
L'interface web se lance avec le script server.py. Le serveur webest alors disponible sur la machine local sur le port 5000.
