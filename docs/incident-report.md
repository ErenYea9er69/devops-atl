# Incident report — staging rollback exercise

Cause: à compléter après le déploiement de démonstration de l’image v0.9.0.
Detection: à compléter avec l’heure et la première erreur utile des journaux.
Action: remettre IMAGE_TAG=v1.0.0, relancer Compose et valider /health.
Downtime: à mesurer pendant l’exercice, du premier échec de santé au retour au vert.
Prevention: bloquer la promotion si le health check échoue et conserver une image précédente validée.
