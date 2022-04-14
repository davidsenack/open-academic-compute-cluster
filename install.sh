#!/bin/bash

# Install the Open Academic Compute Cluster
#
# Run "sudo bash ./open-academic-compute-cluster/install.sh"

sudo cp -r ./open-academic-compute-cluster/ /opt
cd /opt/open-academic-compute-cluster/oacc
cp oacc.py oacc
chmod +x oacc
export PATH=$PATH:/opt/open-academic-compute-cluster/oacc
cd ~ 