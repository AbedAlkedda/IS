# My Web Crawler

# run SOAP Server
pip install -r requirements.txt
python app.py

# run REST Server
bundle install
ruby app.rb

# list ips
docker inspect -f '{{.Name}} - {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -aq)

# run using docker-compose
docker-compose build && docker-compose up
