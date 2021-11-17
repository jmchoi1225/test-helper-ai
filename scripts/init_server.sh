#!/bin/bash

if [ -d /home/ubuntu/test-helper-ai ]
then
    echo "Directory /home/ubuntu/test-helper-ai exists. delete start!" 
    rm -rf /home/ubuntu/test-helper-ai
fi