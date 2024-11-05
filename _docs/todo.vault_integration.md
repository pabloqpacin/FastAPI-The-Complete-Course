Integrating HashiCorp Vault for dynamic secrets management with your FastAPI + PostgreSQL project can help secure your database credentials by generating secrets on demand instead of storing static credentials in your `.env` file. Here’s a basic approach to integrating Vault for dynamic PostgreSQL credentials with FastAPI:

### 1. **Set Up Vault for Dynamic Secrets**

Assuming Vault is already installed and configured, follow these steps:

#### Enable the Database Secrets Engine in Vault
First, enable Vault's database secrets engine to allow dynamic credential management for PostgreSQL:

```sh
vault secrets enable database
```

#### Configure the Database Secrets Engine for PostgreSQL
You’ll need to connect Vault to PostgreSQL by providing it with a privileged user that can create new roles. Run the following command to set up the connection (replace placeholders with actual values):

```sh
vault write database/config/my-postgresql-database \
    plugin_name=postgresql-database-plugin \
    allowed_roles="fastapi-role" \
    connection_url="postgresql://{{username}}:{{password}}@postgresql:5432/fastapi" \
    username="vault_admin" \
    password="your_admin_password"
```

This configuration allows Vault to connect to PostgreSQL using the `vault_admin` user and manage roles with the `fastapi-role` role.

#### Define a Role for FastAPI
Next, create a role in Vault that generates PostgreSQL credentials with specific privileges:

```sh
vault write database/roles/fastapi-role \
    db_name=my-postgresql-database \
    creation_statements="CREATE ROLE \"{{name}}\" WITH LOGIN PASSWORD '{{password}}' VALID UNTIL '{{expiration}}'; GRANT SELECT ON ALL TABLES IN SCHEMA public TO \"{{name}}\";" \
    default_ttl="1h" \
    max_ttl="24h"
```

In this setup:
- Vault will generate a new role with a 1-hour default TTL, so credentials expire after an hour.
- The new role has permissions granted as specified in `creation_statements`.

### 2. **Fetch Dynamic Secrets in FastAPI**

To access Vault from within FastAPI, you can use Vault’s REST API or the official Python client (`hvac`). Here’s how to retrieve credentials dynamically within FastAPI.

#### Install the `hvac` Client Library

```sh
pip install hvac
```

#### FastAPI Integration with Vault
Now, use `hvac` to interact with Vault and retrieve dynamic credentials:

```python
import hvac
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI

app = FastAPI()

def get_db_credentials():
    # Initialize the Vault client
    client = hvac.Client(url=os.getenv("VAULT_ADDR"))
    client.token = os.getenv("VAULT_TOKEN")
    
    # Fetch dynamic database credentials
    credentials = client.secrets.database.generate_credentials("fastapi-role")
    username = credentials["data"]["username"]
    password = credentials["data"]["password"]
    
    return username, password

def get_database_url():
    username, password = get_db_credentials()
    return f"postgresql://{username}:{password}@postgresql:5432/fastapi"

# Set up SQLAlchemy with dynamic credentials
SQLALCHEMY_DATABASE_URL = get_database_url()
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.get("/")
def read_root():
    db = SessionLocal()
    # Perform database operations
    db.close()
    return {"msg": "Connected to database with dynamic secrets!"}
```

In this setup:
- **`get_db_credentials()`**: Fetches a new set of credentials from Vault.
- **`get_database_url()`**: Builds the database URL using the dynamic credentials.
- **SQLAlchemy Engine**: Each time the app runs, it pulls new, temporary credentials from Vault, reducing the risk of leaked secrets.

### 3. **Environment Variables**

Set up environment variables in `.env.example` for the Vault integration:

```plaintext
VAULT_ADDR=http://127.0.0.1:8200   # Vault server address
VAULT_TOKEN=s.xxxxxxx              # A Vault token with permissions for the `fastapi-role`
```

> **Note:** Avoid hardcoding the Vault token directly into your code; use environment variables instead.

### 4. **Docker Compose Integration**

In your `docker-compose.yml`, add environment variables for `VAULT_ADDR` and `VAULT_TOKEN`:

```yaml
services:
  fastapi:
    build:
      context: .
    environment:
      VAULT_ADDR: ${VAULT_ADDR}
      VAULT_TOKEN: ${VAULT_TOKEN}
    # Other settings...
```

This configuration will securely pull secrets from Vault on demand and use them within FastAPI, giving you a dynamic and secure way to manage database credentials.
