#!/bin/bash
yum update -y && su ec2-user && aws s3 cp s3://rnitychoruk-git-like-bucket/db_app-master.zip ./ && unzip db_app-master.zip
cd db_app-master && pip3 install -r requirements.txt && cd src
touch /etc/systemd/system/db_app.service
echo "[Unit]
Description=db_app service

[Service]
ExecStart=./db_app-master/src/ && python3 -m app

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/db_app.service
sudo systemctl start db_app && sudo systemctl enable db_app