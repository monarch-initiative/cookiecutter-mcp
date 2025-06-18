################################################################################
# {{ cookiecutter.package_name }}/tools.py
# This module contains tools that consume the generic API wrapper functions in
# {{ cookiecutter.package_name }}/api.py and constrain/transform them based on use cases
################################################################################
from typing import Any, Dict, List, Optional
from .api import fetch_records_paged


def sample_tool_function(
    parameter1: str,
    parameter2: int = 10
) -> List[Dict[str, Any]]:
    """
    Sample tool function to demonstrate how to create a tool for your MCP.
    
    Args:
        parameter1: Description of parameter1
        parameter2: Description of parameter2, with default value
        
    Returns:
        List[Dict[str, Any]]: List of records matching the criteria
    """
    # Example of how to use the API wrapper
    filter_criteria = {"field1": parameter1, "field2": {"$gt": parameter2}}
    
    records = fetch_records_paged(
        endpoint="your_endpoint",
        filter_criteria=filter_criteria,
        max_records=parameter2,
    )
    
    # Process records if needed
    processed_records = []
    for record in records:
        # Process each record
        processed_record = {
            "id": record.get("id"),
            "name": record.get("name"),
            # Add other fields as needed
        }
        processed_records.append(processed_record)
    
    return processed_records