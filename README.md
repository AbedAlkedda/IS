# God is a fucking astronat

# build docker image
docker build -t server_b -f server_b.Dockerfile .

# run server_b docker image
docker run --rm -p 80:80 server_b

# run server_a docker image
docker run --rm -p 4567:4567 server_a

# run server_b
python app.py

# run server_a
bundle install
ruby app.rb
