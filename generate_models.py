#!/usr/bin/env python3
"""Script to generate Pydantic models from the KTalk API specification."""

import json
import re
from typing import Dict, Any, List, Optional

def snake_case(name: str) -> str:
    """Convert PascalCase to snake_case."""
    # Handle the case where we have dots in the name (like namespace.classname)
    parts = name.split('.')
    # Process the last part (the actual class name)
    class_name = parts[-1]
    # Insert underscores before uppercase letters that follow lowercase letters
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', class_name)
    # Insert underscores before uppercase letters that follow lowercase letters or digits
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1)
    # Convert to lowercase
    snake_case_name = s2.lower()
    # Replace the last part with the converted name
    parts[-1] = snake_case_name
    return '_'.join(parts)


def clean_field_name(name: str) -> str:
    """Clean field name to make it valid Python identifier."""
    # Replace special characters with underscore
    cleaned = re.sub(r'[^\w]', '_', name)
    # If it starts with a digit, prefix with underscore
    if cleaned and cleaned[0].isdigit():
        cleaned = f'field_{cleaned}'
    # If it's a Python keyword, add underscore
    keywords = {'class', 'def', 'return', 'import', 'for', 'in', 'if', 'else', 'elif', 'while', 'try', 'except', 'finally', 'with', 'as', 'is', 'not', 'and', 'or', 'from', 'global', 'nonlocal', 'lambda', 'yield', 'assert', 'break', 'continue', 'del', 'pass', 'raise', 'True', 'False', 'None'}
    if cleaned in keywords:
        cleaned = f'{cleaned}_'
    return cleaned


def get_python_type(json_schema_type: str, format: Optional[str] = None, ref: Optional[str] = None) -> str:
    """Convert JSON Schema type to Python type."""
    if ref:
        # Extract class name from reference and clean it
        class_name = ref.split('/')[-1]
        return class_name.replace('.', '_')
    
    if json_schema_type == 'string':
        if format == 'date-time':
            return 'datetime'
        elif format == 'date':
            return 'date'
        else:
            return 'str'
    elif json_schema_type == 'integer':
        return 'int'
    elif json_schema_type == 'number':
        return 'float'
    elif json_schema_type == 'boolean':
        return 'bool'
    elif json_schema_type == 'array':
        return 'List'
    elif json_schema_type == 'object':
        return 'Dict[str, Any]'
    else:
        return 'Any'


def generate_model(model_name: str, schema: Dict[str, Any], all_schemas: Dict[str, Any]) -> str:
    """Generate a Pydantic model from a JSON Schema."""
    from datetime import datetime, date
    from typing import Dict, Any, List, Optional
    
    # Clean model name to be a valid Python class name
    clean_model_name = model_name.replace('.', '_')
    
    properties = schema.get('properties', {})
    required = schema.get('required', [])
    
    # Start building the model
    model_lines = []
    model_lines.append(f'class {clean_model_name}(BaseModel):')
    model_lines.append('    """Generated model for {}."""'.format(model_name))
    
    if not properties:
        model_lines.append('    pass')
    else:
        for prop_name, prop_details in properties.items():
            prop_name_clean = clean_field_name(prop_name)
            
            # Determine type
            prop_type = 'Any'
            if '$ref' in prop_details:
                prop_type = get_python_type('', ref=prop_details['$ref'])
            elif 'type' in prop_details:
                if prop_details['type'] == 'array':
                    # Handle array types
                    items = prop_details.get('items', {})
                    if '$ref' in items:
                        item_type = get_python_type('', ref=items['$ref'])
                    else:
                        item_type = get_python_type(items.get('type'), items.get('format'))
                    
                    # Check if it's optional
                    if prop_name not in required:
                        prop_type = f'Optional[List[{item_type}]] = None'
                    else:
                        prop_type = f'List[{item_type}]'
                elif prop_details['type'] == 'object':
                    # Handle object types (inline objects)
                    if 'properties' in prop_details:
                        # This would require recursive generation, for now we'll use Dict
                        if prop_name not in required:
                            prop_type = 'Optional[Dict[str, Any]] = None'
                        else:
                            prop_type = 'Dict[str, Any]'
                    else:
                        if prop_name not in required:
                            prop_type = 'Optional[Dict[str, Any]] = None'
                        else:
                            prop_type = 'Dict[str, Any]'
                else:
                    # Handle primitive types
                    prop_type = get_python_type(prop_details['type'], prop_details.get('format'))
                    
                    if prop_name not in required:
                        prop_type = f'Optional[{prop_type}] = None'
            else:
                if prop_name not in required:
                    prop_type = 'Optional[Any] = None'
                else:
                    prop_type = 'Any'
            
            # Add field to model
            if 'description' in prop_details:
                model_lines.append(f'    {prop_name_clean}: {prop_type}  # {prop_details["description"]}')
            else:
                model_lines.append(f'    {prop_name_clean}: {prop_type}')
    
    model_lines.append('')
    return '\n'.join(model_lines)


def main():
    # Load the API specification
    with open('/workspace/talk.public.api-api.json', 'r', encoding='utf-8') as f:
        api_spec = json.load(f)
    
    # Get schemas
    schemas = api_spec.get('components', {}).get('schemas', {})
    
    # Generate models file
    models_content = []
    models_content.append('"""Auto-generated models from KTalk API specification."""')
    models_content.append('')
    models_content.append('from datetime import datetime, date')
    models_content.append('from typing import Dict, Any, List, Optional')
    models_content.append('from pydantic import BaseModel')
    models_content.append('')
    
    # Generate each model
    for model_name, schema in schemas.items():
        try:
            model_code = generate_model(model_name, schema, schemas)
            models_content.append(model_code)
        except Exception as e:
            print(f"Error generating model {model_name}: {e}")
            continue
    
    # Write models to file
    with open('/workspace/ktalk/models/generated_models.py', 'w', encoding='utf-8') as f:
        f.write('\n'.join(models_content))
    
    print(f"Generated {len(schemas)} models")


if __name__ == '__main__':
    main()