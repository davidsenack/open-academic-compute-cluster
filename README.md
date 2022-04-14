# The Open Academic Compute Cluster (OACC)

<br>

## About The Project

The Open Academic Compute Cluster (OACC) is a project aiming to provide affordable cloud-based cluster computing resources for academics with limited availability, funding, and access to such resources. Based on the College of Charleston’s High Performance Compute Cluster, OACC is suitable for a wide array of academic workloads. Built on Amazon Web Services and AWS ParallelCluster via customizable Terraform configuration files,  and automated with Python, OACC is simple to install, configure, scale, and run.   

<br>
<br>

## Getting Started

OACC is currently only available on GNU/Linux. Ensure that your system is up to date, and you have the gnupg, software-properites-common, curl, and unzip packages installed.

<br>

### Prerequisites:

OACC requires the aws-cli, parallelcluster, and terrform packages to be installed. For futher information check the included documentation links.

* AWS Command Line Interface (aws-cli)

  ```sh
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    unzip awscliv2.zip
    sudo ./aws/install
  ```

* Configure the AWS CLI

  ```sh
    aws configure
    AWS Access Key ID: {Your Access Key ID}
    AWS Secret Access Key: {Your AWS Secret Access Key}
    Default region name: {Your default region name}
    Default output format: {Your default output format}
  ```

  https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

* AWS ParallelCluster (pcluster)
  ```sh
    python3 -m pip install "aws-parallelcluster" --upgrade --user
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
    chmod ug+x ~/.nvm/nvm.sh
    source ~/.nvm/nvm.sh
    nvm install --lts
    export PATH=$PATH:/home/ubuntu/.local/bin
  ```

  https://docs.aws.amazon.com/parallelcluster/latest/ug/install-v3-pip.html

* Terraform (terraform)

  ```sh
    sudo apt-get update && sudo apt-get install -y gnupg software-properties-common curl
    curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
    sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
    sudo apt-get update && sudo apt-get install terraform
  ```

  https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started

<br>

### Installation

1. Clone the repository.

   ```sh
   git clone https://github.com/davidsenack/open-academic-compute-cluster.git
   ```
3. Run the included installation script.

   ```sh
   bash ./open-academic-compute-cluster/install.sh
   ```
4. Add install path to your $PATH variable.

   ```sh
   export PATH=$PATH:~/.open-academic-compute-cluster/oacc
   ```

5. Verify successful installation.

   ```sh
   oacc help
   ```

<br>

## Usage

* General Usage Guidelines:

    ```sh
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
    ```

* To run your first OACC Test Cluster, simply run :

    ```sh
    oacc test
    ```
* When you see the CREATE_IN_PROGRESS message, check your cluster status with:

    ```sh
    oacc status
    ```
* After about 10 minutes your cluster should be ready. Try opening a shell with:

    ```sh
    oacc shell
    ```
* When you are finished with your cluster, simply type:

    ```sh
    oacc destroy
    ```

* That's it! It's really that simple. Now when you're ready to build the actual cluster, simply enter the command:

    ```sh
    oacc build
    ```

    and follow the steps above. Happy (super)computing!


<br>

## License

Distributed under the MIT License. See `LICENSE` for more information.

<br>

## Contact

David Senack - david.senack(at)gmail.com

Project Link: https://github.com/davidsenack/open-academic-compute-cluster