
## Docker & Compose Settings

> Note that docker/.env sets the default environment variables for all the docker images used by docker compose, and that docker/.env-local can be used to override those defaults. Also note that docker/.env-local is referenced in our .gitignore, preventing developers from risking committing potentially sensitive configuration to the repository.

via [docs](https://superset.apache.org/docs/installation/docker-compose)

## Environment Variables

You **must** copy `docker/.env.example` to `docker/.env`

```bash
cp docker/.env.example docker/.env
```

Then make local edits to `docker/.env-local` file which overrides values from `docker/.env`.

For example, create a _docker/.env-local_ file with the following keys:
```
# Must be lowercase with only alphanumeric characters, hyphens, and underscores
COMPOSE_PROJECT_NAME=emap-insights

# Provide the name of the host machine (also HOSTNAME)
HOST_NAME=<GAEXX>

# Set this to a unique secure random value on production
DATABASE_PASSWORD=superset

SUPERSET_LOAD_EXAMPLES=yes

# Make sure you set this to a unique secure random value on production
# using something like `openssl rand -base64 42`
SUPERSET_SECRET_KEY=TEST_NON_DEV_SECRET

# Specify the Superset image tag to use
TAG=4.1.1
```

## Build or run
The shell scripts simply specify the tag, and then call docker compose with the appropriate docker-compose.yml file.

```bash
./build.sh
```

```bash
./up.sh
```

is a quick way of writing
```bash
TAG=4.1.1 docker compose -f docker-compose-image-tag.yml up
```

## Add DuckDb databases
You can now do this from the UI.
It's simplest to use a sqlalchemy connection string.
You must the database into `./data/duckdb` (which is a mounted volume).

```
duckdb:////var/data/duckdb/camino-gold.db
```


## Notes

- See the details here for tag specification: https://superset.apache.org/docs/installation/docker-builds
  - e.g 4.1.1 is lean ... 250MB ish, 4.1.1-dev is not! (but includes postgres drivers and more) ... 1GB
- You may get warnings during initiaton about flask migrations. 

```bash
superset_init         | ERROR [flask_migrate] Error: Can't locate revision identified by '74ad1125881c'
```
These can probably be ignored but you can always delete the `emap-insights_db_data` volume if you want to be sure.

```bash
docker compose down
docker volume rm emap-insights_db_data
```


