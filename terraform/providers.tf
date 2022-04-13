# Terraform configurations must declare which providers 
# they require so that Terraform can install and use them. 

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

# Configure the AWS Provider for US East 2 (Ohio)
provider "aws" {
  region = "us-east-2"
}