# Compte rendu d'incident  Rollback Staging

1. Ce qui s'est passé : La mise en service de la version v0.9.0 a rendu le service indisponible (endpoint /health renvoyant une erreur HTTP 503).
2. Détection : Le script wait-healthy.sh a échoué après ses 12 tentatives de vérification en constatant le code HTTP 503 dans les logs de l'API.
3. Action immédiate : Exécution d'un rollback immédiat vers la version immuable v1.0.0 via IMAGE_TAG=v1.0.0 sans aucune recompilation de code.
4. Temps d'indisponibilité : Environ 1 minute (temps d'exécution du contrôle de santé et bascule du conteneur en 3 secondes).
5. Prévention future : Automatiser le rollback dans la chaîne de déploiement continu dès que le health check échoue en staging.
