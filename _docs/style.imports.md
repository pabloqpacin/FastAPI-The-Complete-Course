In Python, there are some widely accepted standards for how to structure and order imports, most notably defined in **PEP 8**, the Python style guide. Following these standards can help keep your code consistent, readable, and easier to maintain.

> [!IMPORTANT]
> [PEP 8 - Style Guide for Python Code (2001-2013)](https://peps.python.org/pep-0008/)

### Recommended Order for Imports (PEP 8)

Imports should be grouped into three distinct sections, separated by a blank line between them:
1. **Standard library imports**: These are Python’s built-in modules (e.g., `os`, `sys`, `typing`).
2. **Related third-party imports**: These are libraries installed via `pip` or any external sources (e.g., `fastapi`, `pydantic`, `sqlalchemy`, `passlib`).
3. **Local application or project-specific imports**: These are your own modules and files (e.g., `models`, `database`).

Within each section, imports should generally be alphabetized for better readability and consistency.

### Example with PEP 8 Standards Applied

```python
# 1. Standard library imports
from typing import Annotated

# 2. Third-party imports
from fastapi import APIRouter, Depends
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.orm import Session

# 3. Local application imports (modules you've written)
from database import SessionLocal
from models import Users
```

### Additional Guidelines:
- **Absolute imports**: Always prefer absolute imports over relative imports. For example, `from database import SessionLocal` is better than `from .database import SessionLocal`.
- **Group imports**: Avoid putting multiple imports on the same line. For example, `from fastapi import APIRouter, Depends` is acceptable since they are from the same module, but avoid `import os, sys`—split them into separate lines.
- **Blank lines**: Add blank lines between the three sections (standard, third-party, and local imports).

### Tools for Automating Import Formatting

You can use tools to automatically sort and format your imports according to PEP 8:

1. **`isort`**: A popular tool that automatically sorts imports into the correct order. You can install it with `pip install isort` and run it on your files.
   - Command to sort imports:
     ```bash
     isort your_file.py
     ```

2. **`black`**: Another widely-used tool for Python code formatting that integrates well with `isort`. It doesn't handle imports itself, but when combined with `isort`, it provides a consistent style.

By following these practices and automating with tools like `isort`, you'll have clean and well-organized imports in all your Python files.
