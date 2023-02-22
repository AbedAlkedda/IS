# God is a fucking astronat

# run server_b
pip install -r requirements.txt
python app.py

# run server_a
bundle install
ruby app.rb

# list ips
docker inspect -f '{{.Name}} - {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -aq)

