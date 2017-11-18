#!/bin/bash
#cd /root/dbd-test
docker stop test
docker rm test
docker build -t myimage /root/dbd-test/
docker run -d --name test -p 192.168.142.128:5000:80 myimage


