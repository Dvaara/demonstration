FROM spire-agent
RUN apt-get update \
  && apt-get install -y --no-install-recommends ca-certificates python python-requests python-flask python-cachetools

RUN mkdir /opt/back-end

COPY curl.security /opt/back-end
COPY example-1.0-jar-with-dependencies.jar /opt/back-end
COPY salary-introspection.py /opt/back-end
COPY sslCurl2.sh /opt/back-end

# Create user for backend workload
RUN useradd backend -u 1000
RUN chown -R backend /opt/back-end
RUN chmod +x /opt/back-end/salary-introspection.py
RUN chmod +x /opt/back-end/sslCurl2.sh
#CMD ["python", "/opt/back-end/salary-introspection.py"]