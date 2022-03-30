#!/bin/bash
yum update -y && sudo amazon-linux-extras install docker && sudo service docker start && sudo usermod -a -G docker ec2-user
aws s3 cp s3://rnitychoruk-git-like-bucket/db_app-master.zip /home/ec2-user/ && cd /home/ec2-user/ && unzip db_app-master.zip && cd db_app-master
docker run -env AWS_REGION=$(aws ssm get-parameters --names REGION_AWS --with-decryption) -env DB_SECRET=$(aws ssm get-parameters --names DB_SECRET --with-decryption) .