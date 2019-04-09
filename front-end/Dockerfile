FROM spire-agent
RUN apt-get update \
  && apt-get install -y --no-install-recommends ca-certificates python python-requests python-flask python-cachetools

RUN mkdir /opt/sslCurl
COPY sslCurl.jar /opt/sslCurl
COPY example-1.0-jar-with-dependencies.jar /opt/sslCurl
COPY curl.security /opt/sslCurl
COPY application /opt/sslCurl/application
COPY sslCurl.sh /opt/sslCurl
COPY sslCurl2.sh /opt/sslCurl
RUN chmod +x /opt/sslCurl/sslCurl.sh
RUN chmod +x /opt/sslCurl/sslCurl2.sh

#Create users for frontend workloads
RUN useradd frontend1 -u 1000
RUN useradd frontend2 -u 1001
RUN useradd frontend3 -u 1002

RUN chown -R frontend2 /opt/sslCurl/application
#CMD ["python", "/opt/sslCurl/application/employees-token.py"]