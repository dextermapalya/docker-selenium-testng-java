## How to setup gradle using multi stage docker file


#### Install Docker, Docker-compose and Docker-machine

For docker-machine point your browser to https://github.com/docker/machine/releases/

copy the code relevant to your OS

	 $ curl -L https://github.com/docker/machine/releases/download/v0.16.1/docker-machine-`uname -s`-`uname -m` >/tmp/docker-machine && chmod +x /tmp/docker-machine &&  sudo cp /tmp/docker-machine /usr/local/bin/docker-machine


#### Clone this docker-android project

          $ git clone https://github.com/dexterm/testng-selenium-gradle-chrome-firefox.git

#### Build a docker image
          $ docker build -t testng -f Dockerfile.multi .
By using the dot at the end of the command, docker will look for the Dockerfile.multi in the current,           

Verify the creation of docker image
          $ docker images
You should see the recently created image called testng          


#### Launch a container using the testng image
          $ docker run -it -v $PWD:/usr/app testng

This will launch an interactive container, you will be transported into the container automatically

