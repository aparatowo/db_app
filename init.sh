#!/bin/bash
yum update -y && aws s3 cp s3://rnitychoruk-git-like-bucket/db_app-master.zip /home/ec2-user/ && cd /home/ec2-user/ && unzip db_app-master.zip
cd db_app-master && pip3 install -r requirements.txt && cd src
echo '[Unit]
Description=db_app service

[Service]
WorkingDirectory=/home/ec2-user/db_app-master/src/
ExecStart=python3 -m app
Restart=always

[Install]
WantedBy=multi-user.target' > /etc/systemd/system/db_app.service
systemctl enable db_app && systemctl start db_app