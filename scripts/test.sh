#!/bin/bash
#Activate virtual enviroment
source /appenv/bin/activate



# FOR BUILD: Download requirements to build cache
pip download -d /build -r requirements_test.txt --no-input
#Install application test requirements
pip install --no-index -f /build -r requirements_test.txt

#RUn test.sh arguments

exec $@