# Creates new VPC for cluster. Head node in public subnet,
# and compute nodes in private subnet. Up to 250 hosts in public
# subnet, and 4091 hosts in private subnet. A NAT gateway is used
# to communicate between the two subnets.

data "aws_region" "current" {}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "3.14.0"

  name = "oacc-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["${data.aws_region.current.name}a"]
  private_subnets = ["10.0.16.0/20"]
  public_subnets  = ["10.0.0.0/24"]

  enable_nat_gateway     = true
  single_nat_gateway     = true
  one_nat_gateway_per_az = false

  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    terraform = "true"
    oacc      = "true"
  }
}

# Write public and private subnet-id to files to ../tmp directory for python
# conversion to parallelcluster configuration file (yaml).

resource "local_file" "public_subnet_id" {
  content         = module.vpc.public_subnets[0]
  filename        = "../tmp/public_subnet.id"
  file_permission = 600
}

resource "local_file" "private_subnet_id" {
  content         = module.vpc.private_subnets[0]
  filename        = "../tmp/private_subnet.id"
  file_permission = 600
}