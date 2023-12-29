#!/usr/bin/env bash

sudo apt update
sudo apt install mysql-server-5.7
sudo mysql_secure_installation
sudo systemctl enable mysql
sudo systemctl start mysql
sudo systemctl status mysql
mysql --version
