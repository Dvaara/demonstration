FROM spire-agent

# Install Back-end application and configure Tomcat
#RUN rm -Rf /opt/tomcat/webapps/ROOT*
#COPY tasks-rest-api-1.0.war /opt/tomcat/webapps/ROOT.war
#COPY server.xml /opt/tomcat/conf/server.xml
#COPY web.xml /opt/tomcat/conf/web.xml
#COPY spiffe-filter-1.0.jar /opt/tomcat/lib/

RUN mkdir /opt/wso2-authz
COPY start-wso2.sh /opt/wso2-authz
COPY catalina-server.xml /opt/wso2-is/repository/conf/tomcat/catalina-server.xml
COPY log4j.properties /opt/wso2-is/repository/conf/log4j.properties
COPY identity.xml /opt/wso2-is/repository/conf/identity.xml
COPY authenticators.xml /opt/wso2-is/repository/conf/security/authenticators.xml
COPY org.dvaara.wso2.identity.oauth2.token.handler.clientauth.mutualtls-1.0.0.jar /opt/wso2-is/repository/components/dropins/
COPY oauth2.war /opt/wso2-is/repository/deployment/server/webapps/oauth2.war
RUN rm -rf /opt/wso2-is/repository/deployment/server/webapps/oauth2
RUN chmod +x /opt/wso2-authz/start-wso2.sh

COPY java.security /opt/wso2-authz

# Create user for wso2is workload
RUN groupadd --system -g 1002 wso2is && \
useradd --system --create-home --home-dir /home/wso2is --no-log-init -g 1002 -u 1002 wso2is
#RUN useradd wso2is -u 1002
RUN chown -R wso2is /opt/wso2-is
