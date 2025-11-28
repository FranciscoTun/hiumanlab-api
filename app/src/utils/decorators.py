from flask import request, jsonify
from functools import wraps
from pydantic import ValidationError

def validate_with_schema(schema):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                data_to_validate = request.json or {}
                validated_data = schema.model_validate(data_to_validate)
                data = validated_data.model_dump(exclude_none=True)

                if request.method == 'PUT' and not data:
                    return jsonify({"error": "No data provided for update"}), 400

                return f(data=data, *args, **kwargs)
            
            except ValidationError as e:
                return jsonify({"error": "Validation failed", "details": e.errors()}), 400
            except Exception as e:
                if request.method in ('POST', 'PUT') and not request.json:
                     return jsonify({"error": "Invalid JSON or empty body"}), 400
                return jsonify({"error": str(e)}), 500
        return wrapper
    return decorator
