# Incident report — staging rollback exercise

Cause: l’image locale v0.9.0 renvoyait HTTP 503 sur /health (simulation via HEALTH_STATUS=503).
Detection: wait-healthy.sh a échoué après 12 essais ; premier log utile : GET /health 503 à 09:47:43 UTC.
Action: IMAGE_TAG est revenu à v1.0.0 ; Compose a recréé l’API et /health a répondu 200 à 09:49:09 UTC.
Downtime: environ 86 secondes entre le premier 503 et le premier 200 ; commande de rollback au vert en 6,7 secondes.
Prevention: bloquer toute promotion sans health check vert et garder une image précédente déjà validée.
