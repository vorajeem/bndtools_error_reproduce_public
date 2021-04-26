#!/bin/sh

#Unknown what the purpose of this vultr.sh file is for.

sudo add-apt-repository -y ppa:webupd8team/java
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install -y python
sudo apt-get install -y python-dev
sudo apt-get install -y python-twisted
sudo apt-get install -y oracle-java8-set-default

