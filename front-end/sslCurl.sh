#!/usr/bin/env bash

if [ -n "$1" ]; then
  CURL_ARG="$1"
else
  echo ERROR: URL is missing
  exit 1 # terminate and indicate error
fi

if [ -n "$2" ]; then
    USERNAME="$2"
else
   USERNAME="frontend2"
fi

su -c "java -Djava.security.properties=/opt/sslCurl/curl.security -Dspiffe.endpoint.socket=/tmp/agent.sock -jar sslCurl.jar ${CURL_ARG}" ${USERNAME}
