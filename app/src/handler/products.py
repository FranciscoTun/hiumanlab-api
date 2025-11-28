from flask import Blueprint, jsonify, current_app, request
from app.src.services.product_service import ProductService
from app.src.schemas.product_schema import ProductSchema, UpdateProductSchema
from app.src.utils.decorators import validate_with_schema

product_bp = Blueprint("products", __name__)

def get_service():
    return ProductService(current_app)

@product_bp.get("/")
def list_products():
    filters = request.args.to_dict()
    service = get_service()
    return service.fetch(filters)

@product_bp.post("/")
@validate_with_schema(ProductSchema) 
def create_product(data): 
    service = get_service()
    return jsonify(service.create(data)), 201

@product_bp.put("/<product_id>")
@validate_with_schema(UpdateProductSchema) 
def update_product(product_id, data): 
    service = get_service()
    return jsonify(service.update(product_id, data))

@product_bp.delete("/<product_id>")
def delete_task(product_id):
    service = get_service()
    return jsonify(service.delete(product_id))
