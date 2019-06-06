#!/bin/bash
while true
do
        clear
	echo "Waiting for tests to be added!"
        #This is an infinite loop, it will check the tests folder for the presence of an xml
        #if file is found a test is launched

        for file in tests/*; do
           echo "Launching test for $file\n"
           #gradlew -suiteFile=$file
           #echo "$(basename "$file")"
        done
        sleep 180s
done
