FROM ubuntu:xenial

RUN apt-get update \
  && apt-get install -y --no-install-recommends ca-certificates curl tar gzip python python-requests python-flask

# Install Spire Server
ARG SPIRE_VERSION=0.6.0
ARG SPIRE_RELEASE=https://github.com/spiffe/spire/releases/download/${SPIRE_VERSION}/spire-${SPIRE_VERSION}-linux-x86_64-glibc.tar.gz
ARG SPIRE_DIR=/opt/spire

RUN curl --silent --location $SPIRE_RELEASE | tar -xzf -
RUN mv spire-${SPIRE_VERSION} ${SPIRE_DIR}

# Configure Spire
WORKDIR ${SPIRE_DIR}
COPY server.conf conf/server/server.conf
COPY create-entries.sh .
COPY get-entries.sh .
COPY get-entries.py .
RUN chmod +x get-entries.sh
RUN chmod +x get-entries.py
EXPOSE  5000
CMD ["python", "get-entries.py", "-p 5000"]

