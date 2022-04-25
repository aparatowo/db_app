#!/bin/bash
yum update -y && sudo amazon-linux-extras install docker && sudo service docker start && sudo usermod -a -G docker ec2-user
aws s3 cp s3://rnitychoruk-git-like-bucket/db_app-master.zip /home/ec2-user/ && cd /home/ec2-user/ && unzip db_app-master.zip && cd db_app-master
export AWS_DEFAULT_REGION="eu-north-1"
export AWS_REGION=$(aws ssm get-parameter --name REGION_AWS --query "Parameter.Value") && export DB_SECRET=$(aws ssm get-parameter --name DB_SECRET --query "Parameter.Value")
docker build -t app . && docker run -p 0.0.0.0:5000:5000 -e AWS_REGION=$AWS_REGION -e DB_SECRET=$DB_SECRET app