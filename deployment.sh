#!/bin/bash
sudo apt-get update
sudo apt-get install git python-dev python-pip -y
sudo pip install ansible
sudo pip install markupsafe
sudo git clone https://github.com/nadeemshahzad/project-crossover.git
sudo ansible-playbook -i "localhost," -c local project-crossover/deployment.yml

