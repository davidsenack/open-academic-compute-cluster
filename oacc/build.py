import os
from . import oacc_messages
from . import status


def verification(action):

    oacc_messages.state_change_verify_msg(action)
    usr_verify_value = input("    Enter a value: ")
    if usr_verify_value == action:
        return True
        return False


def no_current_cluster():

    if status.get_status() == "NO_ACTIVE_CLUSTERS":
        return True
    else:
        oacc_messages.already_cluster()
        return False


def build_prep():

    os.chdir(os.path.dirname(__file__))
    os.mkdir("../tmp")


def terraform_run():

    # Changes to terraform directory, runs: initialize, format, validate, and
    # applies terraform configuration.

    os.chdir("../terraform")
    os.system("terraform init")
    os.system("terraform fmt")
    os.system("terraform validate")
    if os.system("terraform apply -auto-approve") == 0:
        return True
        return False


# TODO: Rewrite read_subnets()


def read_subnets():

    # Reads terraform generated subnet ids into local variables and returns
    # subnet ids. Deletes terraform generated subnet id files.

    with open("../tmp/public_subnet.id", "r") as file:
        public_subnet_id = file.read()
    with open("../tmp/private_subnet.id", "r") as file:
        private_subnet_id = file.read()
    os.system("rm -f ../tmp/*.id")
    return (public_subnet_id, private_subnet_id)


def write_config(public_subnet_id, private_subnet_id, aws_region, pconfig_yaml):

    # Writes subnet ids and user provided region to pcluster_config.yaml file.

    with open(pconfig_yaml, "r") as file:
        filedata = file.read()

    filedata = filedata.replace("public_subnet_id", public_subnet_id)
    filedata = filedata.replace("private_subnet_id", private_subnet_id)
    filedata = filedata.replace("aws_region", aws_region)

    with open("../configs/pcluster_config_tmp.yaml", "w") as file:
        file.write(filedata)


def pcluster_create():

    # Creates OACC Cluster with name "oacc" using AWS ParallelCluster and
    # pcluster_config.yaml file.

    os.system(
        "pcluster create-cluster --cluster-name oacc --cluster-configuration ../configs/pcluster_config_tmp.yaml"
    )
    oacc_messages.cluster_create_msg()
