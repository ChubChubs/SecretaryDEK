#!/bin/bash
# ************************************************************
# Program: Django Installation Script with Impyla & MySQLdb
# Developer: Pratik Patil, MasterBob
# Date: 16-04-2015
# Last Updated: 28-04-2015
# ************************************************************

if [ "`lsb_release -is`" == "Ubuntu" ] || [ "`lsb_release -is`" == "Debian" ] [ "`lsb_release -is`" == "Mint" ]
then
    sudo apt-get -y install python python-pip python-setuptools;
    sudo apt-get -y install python-dev git-core;


elif [ "`lsb_release -is`" == "CentOS" ] || [ "`lsb_release -is`" == "RedHat" ]
then
    sudo wget http://mirrors.nl.eu.kernel.org/fedora-epel/6/i386/epel-release-6-8.noarch.rpm
    sudo rpm -Uvh epel-release-6-8.noarch.rpm;
    sudo rm -f epel-release-6-8.noarch.rpm;
    sudo yum -y install epel-release python;

else
    echo "Unsupported Operating System";
    exit 1
fi

