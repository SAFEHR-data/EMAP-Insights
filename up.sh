# Run the docker compose file
set -a # automatically export all variables
source docker/.env-local
set +a # stop automatically exporting

echo "Starting Superset at tag $TAG"
docker compose -f docker-compose-image-tag.yml up