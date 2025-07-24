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

1. Navigate to your project directory:
   ```bash
   cd your_project_name
   ```
2. Install the package with uv:
   ```bash
   uv sync --dev --extras
   uv run [your_project_name]
   ```
3. Start developing your MCP tools in `src/your_package_name/tools.py`

4. After you publish to PyPI, you can skip steps 1-3 and do this:
   ```bash
   uvx [your_project_name]
   ```
