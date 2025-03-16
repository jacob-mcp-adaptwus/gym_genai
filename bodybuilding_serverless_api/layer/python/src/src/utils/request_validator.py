from typing import Dict, Any
import json
from jsonschema import validate, ValidationError

# Schema definitions for different request types
SCHEMAS = {
    'create_plan': {
        'type': 'object',
        'required': ['goals', 'experience_level', 'available_days'],
        'properties': {
            'goals': {'type': 'array', 'items': {'type': 'string'}},
            'experience_level': {'type': 'string', 'enum': ['beginner', 'intermediate', 'advanced']},
            'available_days': {'type': 'array', 'items': {'type': 'string'}},
            'preferences': {'type': 'object'},
            'limitations': {'type': 'array', 'items': {'type': 'string'}}
        }
    },
    'update_plan': {
        'type': 'object',
        'required': ['plan_data'],
        'properties': {
            'plan_data': {'type': 'object'},
            'notes': {'type': 'string'}
        }
    },
    'chat_message': {
        'type': 'object',
        'required': ['message'],
        'properties': {
            'message': {'type': 'string'},
            'context': {'type': 'object'}
        }
    },
    'progress_update': {
        'type': 'object',
        'required': ['date', 'metrics'],
        'properties': {
            'date': {'type': 'string', 'format': 'date'},
            'metrics': {
                'type': 'object',
                'properties': {
                    'measurements': {'type': 'object'},
                    'workout_data': {'type': 'object'},
                    'nutrition_data': {'type': 'object'}
                }
            },
            'notes': {'type': 'string'}
        }
    }
}

def validate_request(body: Dict[str, Any], schema_type: str) -> None:
    if schema_type not in SCHEMAS:
        raise KeyError(f"Unknown schema type: {schema_type}")
        
    try:
        validate(instance=body, schema=SCHEMAS[schema_type])
    except ValidationError as e:
        raise ValidationError(f"Validation failed: {str(e)}") 