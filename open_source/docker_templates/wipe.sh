sudo docker rm -f $(docker ps -a -q)

# Delete every Docker image
sudo docker rmi -f $(docker images -q)
