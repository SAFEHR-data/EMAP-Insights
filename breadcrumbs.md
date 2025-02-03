# Running notes

## 2025-02-03 sqlite with superset

Create a local directory under the superset project repo called `./data`
Or better symlink here

Then edit superset_config.py
```
# Allow sqlite to be used 
# via https://github.com/apache/superset/issues/9748
# Superset configuration file
PREVENT_UNSAFE_DB_CONNECTIONS=False
```

Then edit the docker-compose.yml
```
x-superset-volumes: &superset-volumes
  # /app/pythonpath_docker will be appended to the PYTHONPATH in the final container
  - ./docker:/app/docker
  - ./superset:/app/superset
  - ./superset-frontend:/app/superset-frontend
  - superset_home:/app/superset_home
  - ./tests:/app/tests
  # https://github.com/apache/superset/issues/9748#issuecomment-2099107789
  - ./data:/var/mydata
```

Then restart your superset service
And add a new database connection: the four forward slashes are for an absolute path

```
sqlite:////var/mydata/bronze.db
```

## 2025-02-03 docker stuff
You don't need to bring down all the services when you make a change
docker compose will figure out what to stop/restart/build etc.

```
docker compose up -d --build <service-name>
```
here service name is *superset* for most stuff