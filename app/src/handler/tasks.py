from flask import Blueprint, jsonify, current_app, request
from app.src.services.task_service import TaskService
from app.src.schemas.task_schema import TaskSchema, UpdateTaskSchema
from app.src.utils.decorators import validate_with_schema

tasks_bp = Blueprint("tasks", __name__)

def get_service():
    return TaskService(current_app)

@tasks_bp.get("/")
def list_tasks():
    filters = request.args.to_dict()
    service = get_service()
    return service.fetch(filters)

@tasks_bp.post("/")
@validate_with_schema(TaskSchema) 
def create_task(data): 
    service = get_service()
    return jsonify(service.create(data)), 201

@tasks_bp.put("/<task_id>")
@validate_with_schema(UpdateTaskSchema) 
def update_task(task_id, data): 
    service = get_service()
    return jsonify(service.update(task_id, data))

@tasks_bp.delete("/<task_id>")
def delete_task(task_id):
    service = get_service()
    return jsonify(service.delete(task_id))
