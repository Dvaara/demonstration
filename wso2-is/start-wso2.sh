#!/usr/bin/env bash
#mkdir -p /opt/wso2-authz/.java/.systemPrefs
#mkdir /opt/wso2-authz/.java/.userPrefs
#chmod -R 755 ~/.java
# -Djava.util.prefs.syncInterval=10
export JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"
export JAVA_OPTS="$JAVA_OPTS -Djava.security.properties=/opt/wso2-authz/java.security"
export SPIFFE_ENDPOINT_SOCKET=/tmp/agent.sock
su -c "/opt/wso2-is/bin/wso2server.sh run" wso2is

