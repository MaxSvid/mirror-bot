FROM python:3.13-slim

LABEL mainainer="@mak_sjr"

# by default all operations are performed with root privileges. This is not good practice.
# docs I found in ru that explains why: https://habr.com/ru/post/448480/
# the next six lines are needed to create a non-root user for VPS
ARG UID=1000
ARG GID=1000
ENV UID=${UID}
ENV GID=${GID}

RUN useradd -m -u $UID docker_user
