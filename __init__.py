from flask import Flask
from aurora.config import Config
from aurora.extensions import db

def create_app():
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static"
    )

    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        from aurora.models import seed_items_once
        db.create_all()
        seed_items_once()

    from aurora.routes.pages_routes import pages_bp
    from aurora.routes.auth_routes import auth_bp
    from aurora.routes.shop_routes import shop_bp
    from aurora.routes.payment_routes import payment_bp

    app.register_blueprint(pages_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(shop_bp)
    app.register_blueprint(payment_bp)

    return app
