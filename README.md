# God is a fucking astronat

# build docker image
docker build -t server_b -f server_b.Dockerfile .

# run server_b docker image
docker run --rm -p 80:80 server_b

# run server_b
FLASK_APP=app.py flask run --host=0.0.0.0 --port=5000
