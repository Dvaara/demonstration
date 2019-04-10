#!/usr/bin/env bash

if [ -n "$1" ]; then
  CURL_ARG="$1"
else
  echo ERROR: URL is missing
  exit 1 # terminate and indicate error
fi

if [ -n "$2" ]; then
  CURL_DATA="$2"
else
  echo ERROR: Data is missing
  exit 1 # terminate and indicate error
fi

if [ -n "$3" ]; then
    HEADERS="$3"
else
   echo ERROR: Required headers missing
   exit 1 # terminate and indicate error
fi

if [ -n "$4" ]; then
    USERNAME="$4"
else
   USERNAME="backend"
fi

su -c "java -Djava.security.properties=curl.security -Dspiffe.endpoint.socket=/tmp/agent.sock -jar example-1.0-jar-with-dependencies.jar ${CURL_ARG} ${CURL_DATA} $HEADERS" ${USERNAME}
