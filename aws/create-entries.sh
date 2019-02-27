#!/usr/bin/env bash
set -x
 /opt/spire/spire-server register \
     -parentID spiffe://example.org/spire/agent/aws_iid_attestor​/441978600994/i-0e082661c907259c3 \
     -spiffeID spiffe://example.org/salary \
     -selector unix:uid:1000

 /opt/spire/spire-server register \
     -parentID spiffe://example.org/spire/agent/aws_iid_attestor​/441978600994/i-0e082661c907259c3 \
     -spiffeID spiffe://example.org/HRsystem \
     -selector unix:uid:1000