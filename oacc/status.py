import subprocess as sp
import json

# Simple wrapper around AWS ParallelCluster list-cluster command.


def get_status():
    output_data = sp.getoutput("pcluster list-clusters")
    json_data = json.loads(output_data)
    cluster_len = len(json_data["clusters"])

    if cluster_len == 0:
        status = "NO_ACTIVE_CLUSTERS"
    else:
        status = json_data["clusters"][0]["clusterStatus"]
    return status
