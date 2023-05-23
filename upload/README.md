
To run some shit and mount the data to be used to predicts stuff

#docker
docker pull leschultz/cmg:tagname
docker run -v $(pwd):/mnt leschultz/cmg:tagname /bin/python3 predict.py

#podman
podman pull docker.io/leschultz/cmg/tagname
podman run -v $(pwd):/mnt <image serial number> /bin/python3 predict.py
