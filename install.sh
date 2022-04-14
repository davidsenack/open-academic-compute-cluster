#!/bin/bash

mv open-academic-compute-cluster/ /opt
cd /opt/open-academic-compute-cluster/oacc
mv oacc.py oacc
chmod +x oacc
export PATH=$PATH:/opt/open-academic-compute-cluster/oacc