aws_region   = "us-east-1"
repo_name    = "3-tier-mod"
scan_on_push = true

ami_id            = "ami-00ca32bbc84273381"
instance_type     = "t2.micro"
instance_name     = "devops-ec2-instance"
key_name          = "deployer_key"
allowed_ssh_cidrs = ["0.0.0.0/0"]
name              = "devops-ec2"
tags = {
  Environment = "dev"
  Project     = "ECR-EC2-Deployment"
}
