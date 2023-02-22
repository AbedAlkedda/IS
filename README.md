# God is a fucking astronat

# build docker image
docker build -t server_b -f server_b.Dockerfile .

# run server_b docker image
docker run --rm -p 80:80 server_b
docker build -t soap -f soap.Dockerfile . && docker run --rm -p 8000:8000 soap

# run server_a docker image
docker run --rm -p 5000:5000 server_a
docker build -t rest -f rest.Dockerfile . && docker run --rm -p 5000:5000 rest

# run server_b
python app.py

# run server_a
bundle install
ruby app.rb

# list ips
docker inspect -f '{{.Name}} - {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -aq)