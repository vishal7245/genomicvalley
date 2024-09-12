import reflex as rx

config = rx.Config(
    app_name="genomicvalley",
    db_url="sqlite:///reflex.db",
    frontend_port=3001,
    backend_port=8001,
    cors_allowed_origins=["*"],
)


# Create your app instance with this config
app = rx.App(config=config)
