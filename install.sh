#!/bin/bash

# Install the Open Academic Compute Cluster
#
# Run "sudo bash ./open-academic-compute-cluster/install.sh"

PROG_DIR=/opt/open-academic-compute-cluster/

cp -r ./open-academic-compute-cluster/ /opt
cp $PROG_DIR/oacc/oacc.py $PROG_DIR/oacc/oacc
chmod +x $PROG_DIR/oacc/oacc
echo "add oacc to path with: export PATH=\$PATH:/opt/open-academic-compute-cluster/oacc"
