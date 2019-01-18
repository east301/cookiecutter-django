#
#
#

# ================================================================================
# stage1
# ================================================================================

FROM python:3.7.2-alpine3.8 AS build

RUN apk add --no-cache gcc git libc-dev linux-headers

COPY . /opt/gpc_auth/src/
RUN cd /opt/gpc_auth/src && ./setup.py install


# ================================================================================
# stage2
# ================================================================================

FROM python:3.7.2-alpine3.8

COPY --from=build /usr/local /usr/local
RUN DJANGO_SETTINGS_MODULE=gpc_auth.settings.docker_setup gpc_auth collectstatic --noinput --link

CMD ["/bin/sh"]
