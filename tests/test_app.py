from app import app


def test_home_returns_service_name():
    response = app.test_client().get("/")

    assert response.status_code == 200
    assert response.json["service"] == "Campus Tasks"


def test_health_returns_success_by_default():
    response = app.test_client().get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"
