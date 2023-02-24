# My Web Crawler

# run SOAP Server. First go to soap dir and then
pip install -r requirements.txt
python app.py

# run REST Server. First go to rest dir and then
bundle install
ruby app.rb

# list ips
docker inspect -f '{{.Name}} - {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -aq)

# run using docker-compose
docker-compose build && docker-compose up

# Display the Page
visit http://10.5.0.2:80
