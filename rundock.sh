#!/bin/bash
#cd /root/dbd-test
apt-get install docker.io git-sh
git clone https://github.com/tamplier77/dbd-test
cd dbd-test
docker pull tamplier77/dbdtest
docker build -t myimage .
docker run -d --name test -p 0.0.0.0:5000:80 myimage


