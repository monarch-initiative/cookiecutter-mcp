# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Installation

You can install the package from source:

```bash
pip install -e .
```

Or using uv:

```bash
uv pip install -e .
```

## Usage

You can use the CLI:

```bash
{{ cookiecutter.project_slug }}
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
uv pip install -e ".[dev]"
```


## License

{{ cookiecutter.license }}
