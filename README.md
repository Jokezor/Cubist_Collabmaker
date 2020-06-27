# Our-Connected-Future
Connecting collaborators and people with great ideas during a time of need.

# Now everything will run inside docker to handle ease of use with different packages and scalability


## To Run Docker on Ubuntu
1. Go to your terminal
2. Run `sudo apt install git`
3. Install docker through following these commands: https://www.hostinger.com/tutorials/how-to-install-docker-on-ubuntu
4. Run `sudo apt install docker-compose`
5. Change permissions to be able to run without sudo: https://docs.docker.com/engine/install/linux-postinstall/
6. Navigate to where you want to keep your repository ex: `cd Documents`
7. Create the folder: `mkdir Collabmaker`
8. Enter the folder: `cd Collabmaker`
9. Clone the repository: `git clone https://github.com/Collabmaker/Webserver.git`
10. Enter the repository root folder: `cd Webserver`
11. Run the setup Dockerfiles: `docker-compose -f docker-compose.yml up --build -d`


## To run Docker on Mac
1. Go to your terminal
2. Install homebrew: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`
3. Install Git: `brew install git`
4. Install Docker: https://docs.docker.com/get-docker/
5. Make sure Docker is running on your machine.
6. Navigate to where you want to keep your repository ex: `cd Documents`
7. Create the folder: `mkdir Collabmaker`
8. Enter the folder: `cd Collabmaker`
9. Clone the repository: `git clone https://github.com/Collabmaker/Webserver.git`
10. Enter the repository root folder: `cd Webserver`
11. Run the setup Dockerfiles: `docker-compose -f docker-compose.yml up --build -d`


Now docker will install python, postgresql etc in a container and then start the django webserver and the database.
The django webserver will be available at http://127.0.0.1:8000/ 

## Handy commands to run things with the created containers

#### See all running containers
`docker ps`

#### login to container, get processing_id from docker ps
`docker exec -t -i  <processing_id> bash`

#### stop all containers:
`docker kill $(docker ps -q)`

#### remove all containers
`docker rm $(docker ps -a -q)`

#### remove all docker images
`docker rmi $(docker images -q)`

#### remove all docker volumes
`docker volume ls -qf dangling=true | xargs  docker volume rm`

#### For docker to rebuild:
`docker-compose -f docker-compose.yml up --build -d`
 
#### See error messages:
`docker-compose logs -f`

#### Get Django shell
`docker-compose exec web python manage.py shell`

#### Import populate_db to populate database
`from Populate_db import populate`

#### See error messages in building container:
`docker-compose logs -f`

#### Can also specify the yml file
`docker-compose -f docker-compose.prod.yml logs -f`

#### Inspect a volume created
`docker volume inspect django-on-docker_postgres_data`

#### Apply migrations
`docker-compose exec web python manage.py migrate test_3`

#### Revert migrations
`docker-compose exec web python manage.py migrate test_3 zero`

#### Access database
`docker-compose exec db psql --username=hello_django --dbname=hello_django_dev`

#### Drop Database
`docker exec -it 3127fc56248f psql -U hello_django -d postgres -c "DROP DATABASE hello_django_dev;"`

#### Create Admin users:
`docker-compose exec web python manage.py createsuperuser`

#### Conversion from .shp file to postGIS table
`docker-compose exec web ogr2ogr -f "PostgreSQL" PG:"dbname=hello_django_dev user=hello_django password=hello_django" ne_10m_populated_places.shp -nln City -append`
