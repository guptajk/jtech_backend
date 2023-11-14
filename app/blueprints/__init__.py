from app import app
from app.apis.urls import user_bp

default_url_prefix = "/api/v1"
app.register_blueprint(
    user_bp,
    url_prefix=default_url_prefix + "/users",
)