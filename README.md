# MCP (Model Context Protocol) Cookiecutter

A cookiecutter template for creating new Model Context Protocol (MCP) projects based on the FastMCP framework. This template helps you get started with building MCPs quickly, providing the necessary structure and tools.

## Usage

### Creating a New MCP Project

```bash
# Create from GitHub template
cookiecutter https://github.com/monarch-initiative/cookiecutter-mcp.git
```

Or if you have a local copy:

```bash
cookiecutter cookiecutter-mcp
```

### Next Steps

After creating your project:

1. Initialize a git repository (this happens automatically)
2. Create a virtual environment
3. Install the package in development mode with uv:
   ```bash
   uv pip install -e ".[dev]"
   ```
4. Start developing your MCP tools in `src/your_package_name/tools.py`
