memory_searcher
===============

#Fonctionnement

## Indexation
Le script logic/add_folder.py ajoute tous les PDF présents dans les dossiers spécifiés en entrée dans une file de traitement Redis local.

Le script logic/process_jobs.py récupère le prochain PDF à traiter et lance l'extraction (jusqu'à ce que la file de traitement soit vide).

L'extraction textuelle et des méta données se fait via Apache Tika. Les données sont ensuite stockées et indexées sur une base ElasticSearch.

## Service
L'interface web se lance avec le script server.py. Le serveur web est alors disponible sur la machine locale sur le port 5000.
