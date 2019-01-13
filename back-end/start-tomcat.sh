#!/usr/bin/env bash
export JAVA_OPTS="$JAVA_OPTS -Djava.security.properties=/opt/back-end/java.security"
export SPIFFE_ENDPOINT_SOCKET=/tmp/agent.sock
su -c "/opt/tomcat/bin/catalina.sh run" backend

