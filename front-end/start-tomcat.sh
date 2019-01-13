#!/usr/bin/env bash

if [ -n "$1" ]; then
    USERNAME="$1"
else
   USERNAME="frontend1"
fi

export JAVA_OPTS="$JAVA_OPTS -Dtasks.service=https://backend:8443/tasks/ -Djava.security.properties=/opt/front-end/frontend.security "
export JAVA_OPTS="$JAVA_OPTS -Dusers.service=https://users-service:8443/users "
export SPIFFE_ENDPOINT_SOCKET=/tmp/agent.sock
su -c "/opt/tomcat/bin/catalina.sh run" ${USERNAME}
