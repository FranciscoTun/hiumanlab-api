from ..src.handler.tasks import tasks_bp
from ..src.handler.products import product_bp
from ..src.handler.projects import project_bp

def register_routes(app):
    app.register_blueprint(tasks_bp, url_prefix="/tasks")
    app.register_blueprint(product_bp, url_prefix="/products")
    app.register_blueprint(project_bp, url_prefix="/projects")
