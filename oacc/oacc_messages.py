# General Messages


def cluster_create_msg():
    print(
        """
    Open Academic Compute Cluster (OACC) is being created.

    Please allow at least 10 minutes for creation process to finish.
    Logging in prior to completion of health checks is disabled
    by default.

    To check status use \"oacc status\"
    To login use \"oacc shell\".

    *Note: login disabled until cluster is finished building.

    """
    )


def state_change_verify_msg(action):
    print(
        """
    Preparing to {} Open Academic Compute Cluster.

    Please verify that you would like to continue.
    If you would like to continue please enter '{}'.

    """.format(
            action, action
        )
    )


# Error Messages


def state_change_canceled(action):
    print("{} cancelled.".format(action.capitalize()))


def invalid_argument():
    print("oacc: invalid argument provided.")


def create_not_compelete():
    print("oacc: cluster state invalid. Check state with 'oacc status'.")


def already_cluster():
    print("oacc: cluster build failed. Cluster already exists.")


def terraform_failed():
    print("oacc: terraform failed to build all neccessay infrastructure.")
