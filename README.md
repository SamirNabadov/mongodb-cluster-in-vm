MongoDB (NoSQL database)
================================


Install & Configure MongoDB Cluster in VM


Configured software and tools
------------
* MongoDB 4.4.10


Basic settings
------------
* Installing and Configuring MongoDB cluster
* Enabled Authorization
* Configured Keyfile Authentication and Replication
* Created admin user for database


Currently tested on these Operating Systems
* Linux/RHEL/CentOS 7


Requirements
------------
* Ansible 2.11.7
* Python 3.8
* OpenSSL


Dependencies
------------
* Copy Ansible control machine user's public SSH key (usually called id_rsa.pub) into the remote machine working directory
* Requires elevated root privileges
* Add hosts address and names for VMs : inventory
* Prepare variable file based on your requirements: mongo/defaults/main.yml


Running the Deployment
----------------------

On the Ansible Control Machine  

__To deploy__

`./scripts/deploy.sh`


Author Information
------------------

Samir Nabadov
