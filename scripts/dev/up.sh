#! /usr/bin/env sh

docker-compose -f ./docker-compose.yml \
    -f ./docker-compose.override.yml \
    -f ./scripts/dev/docker-compose.dev.yml \
    up $@