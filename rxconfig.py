import reflex as rx

config = rx.Config(
    app_name="genomicvalley",
    db_url="sqlite:///reflex.db",
    frontend_port=3000,
    backend_port=8000,
)

# Enable the use of X-Forwarded-For header
config.api.use_xforwarded_for = True

# Create your app instance with this config
app = rx.App(config=config)
