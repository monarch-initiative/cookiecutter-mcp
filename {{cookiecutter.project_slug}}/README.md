# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Installation

Install the package with uv:

```bash
uv sync --dev
```

## Usage

You can run the MCP:

```bash
uv run {{ cookiecutter.project_slug|replace('_', '-') }}
```

Or install globally and run:

```bash
uvx {{ cookiecutter.project_slug|replace('_', '-') }}
```

Or import in your Python code:

```python
from {{ cookiecutter.package_name }}.main import create_mcp

mcp = create_mcp()
mcp.run()
```

## Development

### Local Setup

```bash
# Clone the repository
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}

# Install development dependencies
uv sync --dev
```


## License

{{ cookiecutter.license }}
