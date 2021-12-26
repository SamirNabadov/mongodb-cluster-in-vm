#!/bin/bash

# Assignment of variables
project_dir=$(pwd)
SECONDS=0

# Installation and Configuration MongoDB Cluster
function deploy_mongo() {
    ansible-playbook $project_dir/cluster.yml -i inventory
    if [ $? -eq 0 ];
    then
        echo "MongoDB Cluster installation was successful!"
        echo "---------------------------------"
    else
        echo "Installation failed!"
        exit 1
    fi
}

# Test Connection to MongoDB with python application
function connect_mongo() {
    pip3 install pymongo
    cd ./python_demo && python3 mongodb.py
}

function main() {
    deploy_mongo
    echo "---------------------------------"
    connect_mongo
    echo "---------------------------------"
    echo "Time executed script: $(($SECONDS / 3600))hrs $((($SECONDS / 60) % 60))min $(($SECONDS % 60))sec"
}

main
