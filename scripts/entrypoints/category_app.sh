#!/usr/bin/env bash

exec ./wait-for-it.sh $POSTGRES_HOST:$POSTGRES_PORT -- "$@"
