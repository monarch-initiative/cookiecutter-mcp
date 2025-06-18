################################################################################
# {{ cookiecutter.package_name }}/main.py
# This module sets up the FastMCP CLI interface
################################################################################

from fastmcp import FastMCP
from {{ cookiecutter.package_name }}.tools import (
    # Import your tools here
    sample_tool_function,
)


def create_mcp():
    """Create a FastMCP instance with all tools registered."""
    # Create the FastMCP instance
    mcp = FastMCP("{{ cookiecutter.package_name }}")
    
    # Register all tools
    mcp.tool(sample_tool_function)
    
    return mcp


# Create the FastMCP instance at module level
mcp = create_mcp()


def main():
    """Main entry point for the application."""
    mcp.run()


if __name__ == "__main__":
    main()