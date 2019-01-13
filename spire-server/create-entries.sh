#!/usr/bin/env bash
set -x
./spire-server entry create -parentID spiffe://example.org/host1 -spiffeID spiffe://example.org/back-end -selector unix:uid:1000 -ttl 120
./spire-server entry create -parentID spiffe://example.org/host4 -spiffeID spiffe://example.org/wso2-is -selector unix:uid:1002 -ttl 120
./spire-server entry create -parentID spiffe://example.org/host2 -spiffeID spiffe://example.org/front-end1 -selector unix:uid:1000 -ttl 120
./spire-server entry create -parentID spiffe://example.org/host2 -spiffeID spiffe://example.org/front-end2 -selector unix:uid:1001 -ttl 120
./spire-server entry create -parentID spiffe://example.org/host3 -spiffeID spiffe://example.org/proxy-service -selector unix:uid:1000 -ttl 120

//may be just consider the parentID as the load may be high with processID
//selct may be on the same type of work..
// starter of the process , load balancer or the own process that spawn processes different places where new processes can be started
inherent properties
how to believe the claim made by the process

