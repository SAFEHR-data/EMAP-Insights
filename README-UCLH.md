
## Docker & Compose Settings
[docs](https://superset.apache.org/docs/installation/docker-compose)
> Note that docker/.env sets the default environment variables for all the docker images used by docker compose, and that docker/.env-local can be used to override those defaults. Also note that docker/.env-local is referenced in our .gitignore, preventing developers from risking committing potentially sensitive configuration to the repository.

Create a _docker/.env-local_ file with the following keys:
```
COMPOSE_PROJECT_NAME=EMAP-Insights

HOST_NAME=<GAEXX>

# Set this to a unique secure random value on production
DATABASE_PASSWORD=superset

SUPERSET_LOAD_EXAMPLES=false

# Make sure you set this to a unique secure random value on production
# using something like `openssl rand -base64 42`
SUPERSET_SECRET_KEY=TEST_NON_DEV_SECRET


## Run

```bash

```

## Notes

See the details here for tag specification
https://superset.apache.org/docs/installation/docker-builds

e.g 
- 4.1.1 is lean ... 250MB ish
- 4.1.1-dev is not! (but includes postgres drivers and more) ... 1GB

A lean start ...
```bash
TAG=4.1.1 docker compose -f docker-compose-image-tag.yml up
```