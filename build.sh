# Run the docker compose file
set -a # automatically export all variables
source docker/.env
source docker/.env-local
set +a # stop automatically exporting

echo "Building Superset at tag $TAG"
docker compose -f docker-compose-image-tag.yml build 