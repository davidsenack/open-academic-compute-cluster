# This file creates an AWS key pair using RSA 4096 bit encryption
# and saves local .pem file to ../keys directory.

resource "tls_private_key" "oacc_key_pair" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "oacc_public_key" {
  key_name   = "oacc_key_pair"
  public_key = tls_private_key.oacc_key_pair.public_key_openssh
}

resource "local_sensitive_file" "oacc_pem_file" {
  content         = tls_private_key.oacc_key_pair.private_key_pem
  filename        = "../tmp/oacc_key_pair.pem"
  file_permission = "0400"
}