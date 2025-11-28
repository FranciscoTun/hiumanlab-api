from flask import Blueprint, jsonify, current_app, request
from app.src.services.project_service import ProjectService
from app.src.schemas.projetc_schema import ProjectSchema, UpdateProjectSchema
from app.src.utils.decorators import validate_with_schema

project_bp = Blueprint("projects", __name__)

def get_service():
    return ProjectService(current_app)

@project_bp.get("/")
def list_products():
    filters = request.args.to_dict()
    service = get_service()
    return service.fetch(filters)

@project_bp.post("/")
@validate_with_schema(ProjectSchema) 
def create_product(data): 
    service = get_service()
    return jsonify(service.create(data)), 201

@project_bp.put("/<product_id>")
@validate_with_schema(UpdateProjectSchema) 
def update_product(product_id, data): 
    service = get_service()
    return jsonify(service.update(product_id, data))

@project_bp.delete("/<product_id>")
def delete_task(product_id):
    service = get_service()
    return jsonify(service.delete(product_id))
