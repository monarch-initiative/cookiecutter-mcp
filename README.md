# MCP (Model Context Protocol) Cookiecutter

A cookiecutter template for creating new Model Context Protocol (MCP) projects based on the FastMCP framework. This template helps you get started with building MCPs quickly, providing the necessary structure and tools.

## What is an MCP?

Model Context Protocols (MCPs) are structured interfaces that help Large Language Models (LLMs) interact with specific data sources or APIs. They provide the LLM with the necessary context and tools to access and manipulate data in a controlled way.

The FastMCP framework makes it easy to create MCPs by providing a standardized approach to defining tools that LLMs can use.

## Features

- Preconfigured project structure for FastMCP-based projects
- Includes API interaction patterns using requests
- Setup for unit testing with pytest
- Uses uv by default for dependency management
- Follows modern Python packaging practices

## Usage

### Prerequisites

- Python 3.11+
- [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html)

### Creating a New MCP Project

```bash
# Create from GitHub template
cookiecutter gh:organization/cookiecutter-mcp
```

Or if you have a local copy:

```bash
cookiecutter cookiecutter-mcp
```

You'll be prompted to enter several values to configure your project:

- `project_name`: The name of your MCP project
- `project_slug`: Used for directory and GitHub repository name (auto-generated)
- `package_name`: Python package name (auto-generated)
- `project_description`: Short description of your MCP
- `database_name`: Name of the database/API your MCP will interact with
- `api_base_url`: Base URL for the API
- `author_name`: Your name
- `author_email`: Your email
- `github_username`: Your GitHub username
- `version`: Initial version (default: 0.1.0)
- `python_version`: Minimum Python version (default: >=3.11)
- `license`: Choose a license for your project

### Next Steps

After creating your project:

1. Initialize a git repository (this happens automatically)
2. Create a virtual environment
3. Install the package in development mode with uv:
   ```bash
   uv pip install -e ".[dev]"
   ```
4. Start developing your MCP tools in `src/your_package_name/tools.py`

## Project Structure

```
your-mcp-project/
├── README.md
├── pyproject.toml
├── src/
│   └── your_package_name/
│       ├── __init__.py
│       ├── __main__.py
│       ├── api.py
│       ├── main.py
│       └── tools.py
├── tests/
│   ├── __init__.py
│   └── test_api.py
└── uv.lock
```

## Developing Your MCP

### Understanding the Structure

- `api.py`: Contains the base API client for interacting with your data source
- `tools.py`: Define FastMCP tools that wrap API functions for specific use cases
- `main.py`: Sets up the FastMCP instance and registers all tools

### Adding a New Tool

1. Define your tool function in `tools.py`:

```python
def my_new_tool(param1: str, param2: int = 10) -> List[Dict[str, Any]]:
    """
    Tool description that explains what it does.
    
    Args:
        param1: Description of param1
        param2: Description of param2, with default value
        
    Returns:
        List[Dict[str, Any]]: Description of return value
    """
    # Implementation
    return results
```

2. Register your tool in `main.py`:

```python
from your_package.tools import my_new_tool

# Add to the existing tools
mcp.tool(my_new_tool)
```

## Contributing

Contributions to improve the cookiecutter template are welcome! Here's how to contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

MIT