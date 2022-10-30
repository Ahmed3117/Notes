### installaton :
* installation,remove guid:
	https://linuxhint.com/install-docker-on-pop_os/
### docker hub account :
	ahmedissa010951
	withALLAH
	ahmedibra010951@gmail.com
### Docker commands :

#### login to your account in docker hub :
	docker login docker.io
#### logout docker hub : 
	docker logut
#### pull image :
	docker pull ubuntu (now we have the image in our OS)
#### show pulled images :
	docker images
#### remove image :
	doker rmi image_name 
	or :
	docker rmi image_id
##### (you can get image id by running the command docker images , you also can use just a part of id like first 3 nums )
#### force remove image : (if image is running or under process)
	doker rmi image_name --force  (or use image id)
#### run a container : 
	docker run --name abu -it ubuntu 
##### (it => interactive), --name abu => means take an instance (container) from the image ubuntu with a name abu , --name abu => this part is optional . now we have a container with an id and a name, if we made another instance it will take another id. 
#### enter to an already made container to work on it :
	docker exec -it container_name bin/bash
#### stop the running container :
	docker stop container_id
#### show running containers : 
	docker ps
#### show all containers : 
	docker ps --all
#### remove container :
	docker rm container_id
#### remove all containers :
	docker rm -f $(docker ps -a -q)
#### force remove container :
	docker rm container_id --force
#### show errors in your containers :
	docker logs
#### docker run :
	docker run options image_name_in_dockerhub:image_version
		options:
			--name any_name_of_your_choice (this will be the name of this container. if not exist 
                         , it will be chosen randomly by docker)
			-p prt_to_run_at
			-d (means work in background until i stop you myself)
			-it (means after making the container,open it . if -it is not written, the container 
                         will be created but will not be opened)
			-e (for image that needs possibly password like mysql)
		image_version:
			choose an available version , if :image_version is not exist , the latest will be used 
	ex1 => docker run --name ngn -d -p 82:80 -it nginx:1.0
			>> 82 => the port where i need the ngn container to run
			>> 80 => the port that the image designed to be run on . you can get it by clicking 
                             the version you choosed in the docker hub , then look for EXPOSE 80 in the 
                              docker file for this image.
	(after running this command , you can run this container in the browser : 
                    http://localhost:82)
    ex2 => docker run --name mysql1 -d -p 8080:3306 mysql
#### Docker file examlpe : (suppose the file name is Dockerfile)
```txt
FROM nginx
COPY your_project_path /user/share/nginx/html
EXPOSE 80
```

#### run docker file :
	docker build -t myfirstapp -f Dockerfile   (Dockerfile is the docker file you named)
	or :
	docker build -t myfirstapp .   (. used if the name of the docker file is Dockerfile 
                                                                 because it is the default , so no need to write it.)
#### check if your image is created :
	docker images  (you should find your image .)
#### run your image (run a container of your image) :
	docker run -p 8080:80 myfirstapp  (now you can visite your project on browser using : 
                                                                      http://localhost:8080)
#### push your app to docker hubb:
* login to docker hub :
	docker login
* crete a repository in docker hub from this link :  (with the name test)
	https://hub.docker.com/repositories
* create a tag for your image
	docker tag myfirstapp test/myfirstapptag:1.0
		myfirstapp => image name 
		test => the name of your repository in docker hub
		myfirstapptag:1.0 => the name of the tag for your image (any name) and a version (any version)
* push the image to the docker hub :
	docker push ahmedissa010951/myfirstapptag:1.0
	or :
	docker push ahmedissa010951/test:myfirstapptag
-------
#### docker bind : (explaination is in the hand written file.)
	docker run --name mysqltest -v "$PWD/mysqlData":/var/lib/mysql -p 3306:3306 mysql
#### docker volume :(explaination is in the hand written file.)
	docker run --name mysqltest -v myVolume:/var/lib/mysql -p 3306:3306 mysql
#### show container details :
	docker inspect container_name
#### show volume details :
	docker volume ls
