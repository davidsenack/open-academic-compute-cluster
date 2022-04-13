# Help menu configuration file.


def oacc_help_menu():
    print(
        """
    Usage: oacc [options] (ex. "oacc build", or "oacc info")

    The available execution are listed below.
    Main commands:
        build           Build OACC cluster infrastructure
        shell           Log default user into shell on cluster head node
        destroy         Destroy OACC cluster infrastructure

    Other commands:
        help            Show help menu with command usage and options
        info            Show info about OACC
        status          Show status of cluster
        test            Run small-scale OACC test cluster
        version         Show OACC version
    """
    )
