#!/usr/bin/env bash
set -x
./spire-server entry create -parentID spiffe://example.org/host1 -spiffeID spiffe://example.org/back-end -selector unix:uid:1000 -ttl 3600
./spire-server entry create -parentID spiffe://example.org/host4 -spiffeID spiffe://example.org/wso2-is -selector unix:uid:1002 -ttl 3600
./spire-server entry create -parentID spiffe://example.org/host2 -spiffeID spiffe://example.org/front-end1 -selector unix:uid:1000 -ttl 3600
./spire-server entry create -parentID spiffe://example.org/host2 -spiffeID spiffe://example.org/front-end2 -selector unix:uid:1001 -ttl 3600
./spire-server entry create -parentID spiffe://example.org/host3 -spiffeID spiffe://example.org/proxy-service -selector unix:uid:1000 -ttl 3600

