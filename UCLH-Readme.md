
## Docker & Compose Settings
[docs](https://superset.apache.org/docs/installation/docker-compose)
> Note that docker/.env sets the default environment variables for all the docker images used by docker compose, and that docker/.env-local can be used to override those defaults. Also note that docker/.env-local is referenced in our .gitignore, preventing developers from risking committing potentially sensitive configuration to the repository.

Create a _docker/.env-local_ file with the following keys:
```
COMPOSE_PROJECT_NAME=EMAP-Insights

# Set this to a unique secure random value on production
DATABASE_PASSWORD=superset

SUPERSET_LOAD_EXAMPLES=false

# Make sure you set this to a unique secure random value on production
SUPERSET_SECRET_KEY=TEST_NON_DEV_SECRET