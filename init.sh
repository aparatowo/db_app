#!/bin/bash
yum update -y
aws s3 cp s3://rnitychoruk-git-like-bucket/db_app-master.zip ./
unzip db_app-master.zip
cd db_app-master
pip3 install -r requirements.txt
cd src
python3 -m app
