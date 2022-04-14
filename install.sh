#!/bin/bash

# Install the Open Academic Compute Cluster
#
# Run "bash ./open-academic-compute-cluster/install.sh"

PROG_DIR=~/.open-academic-compute-cluster/oacc

cp -r ./open-academic-compute-cluster/ ~/.open-academic-compute-cluster/
cp $PROG_DIR/oacc.py $PROG_DIR/oacc
chmod +x $PROG_DIR/oacc
echo "add oacc to path with: export PATH=\$PATH:~/.open-academic-compute-cluster/oacc"

# End
