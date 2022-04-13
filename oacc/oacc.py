#!/bin/python3

from . import build
from . import destroy
from . import help
from . import status
from . import oacc_messages
from . import version
import os
import sys
from functools import partial


def oacc_build(config):

    # Gets AWS Region from user, runs terraform pipeline, if successful reads
    # subnet values from terraform output, writes subnet values to
    # pcluster_config.yaml, creates pcluster.

    desired_state = "build"
    aws_region = "us-east-2"

    if build.verification(desired_state) and build.no_current_cluster():
        build.build_prep()
        if build.terraform_run():
            subnets = build.read_subnets()
            build.write_config(subnets[0], subnets[1], aws_region, config)
            build.pcluster_create()
        else:
            destroy.destroy_prep()
            destroy.destroy_terraform()
            destroy.destroy_clean_up()
            oacc_messages.terraform_failed()
    else:
        oacc_messages.state_change_canceled(desired_state)


def oacc_destroy():

    # Responsible for cluster destruction. Go to terraform directory,
    # delete ParallelCluster, then delete Terraform resources.

    desired_state = "destroy"

    if build.verification(desired_state):
        destroy.destroy_prep()
        destroy.destroy_pcluster()
        destroy.destroy_terraform()
        destroy.destroy_clean_up()
    else:
        oacc_messages.state_change_canceled(desired_state)


def oacc_help():

    # Display OACC cli help menu.
    help.oacc_help_menu()


def oacc_info():

    # Display shortend version of OACC's README.md.
    os.chdir(os.path.dirname(__file__))
    with open("../README.md", "r") as file:
        print(file.read())


def oacc_shell():

    # If cluster exists, change to ../tmp directory and log default user
    # into pcluster shell; else show help message.

    if status.get_status() == "CREATE_COMPLETE":
        os.chdir(os.path.dirname(__file__))
        os.chdir("../tmp")
        os.system("pcluster ssh --cluster-name oacc -i oacc_key_pair.pem")
    else:
        oacc_messages.create_not_compelete()


def oacc_status():

    # Display OACC cluster's current status.
    print("oacc status: {}".format(status.get_status()))


def oacc_version():

    # Return OACC version
    print(version.current_version())


def main():

    # Main loop. Run command based on user input.

    # default configuration files relative path
    conf = "../configs/pcluster_config.yaml"
    test_conf = "../configs/pcluster_test_config.yaml"

    valid_args = {
        "build": partial(oacc_build, conf),
        "destroy": oacc_destroy,
        "help": oacc_help,
        "info": oacc_info,
        "status": oacc_status,
        "shell": oacc_shell,
        "test": partial(oacc_build, test_conf),
        "version": oacc_version,
    }

    if len(sys.argv) == 2:
        usr_arg = str(sys.argv[1])
        valid_args[usr_arg]()
    else:
        oacc_messages.invalid_argument()
        oacc_help()


if __name__ == "__main__":
    main()
