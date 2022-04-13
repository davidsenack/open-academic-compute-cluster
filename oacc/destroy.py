# OACC's destroy functionality. Includes functions to prepare the cluster for
# destruction, destroy AWS ParallelCluster, destroy Terraform infrastructure, # and clean up old state files.


import os
import build


def destroy_prep():
    os.chdir(os.path.dirname(__file__))
    os.chdir("../terraform")


def destroy_pcluster():
    os.system("pcluster delete-cluster --cluster-name oacc")


def destroy_terraform():
    os.system("terraform destroy -auto-approve")
    os.system("rm -f ../configs/pcluster_config_tmp.yaml")


def destroy_clean_up():
    os.system("rm -f terraform.tfstate")
    os.system("rm -f terraform.tfstate.backup")
    os.system("rm -rf ../tmp")
