# ADD pg_hba.conf /var/lib/postgresql/data/
# ADD postgresql.conf /var/lib/postgresql/data/
# syntax=docker/dockerfile:1

FROM postgres:16.1-alpine as jobgre


COPY db_script.sql /docker-entrypoint-initdb.d/