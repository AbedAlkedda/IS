FROM ruby:2.7.2

# Set the working directory to /app
WORKDIR /app

# Copy the Gemfile and Gemfile.lock into the container
COPY rest/Gemfile rest/Gemfile.lock ./

# Install dependencies
RUN bundle install

# Copy the rest of the application code into the container
COPY rest/ ./

RUN docker inspect -f '{{.Name}} - {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -aq)

ENV SOAP_CLIENT_URL=http://10.5.0.3:8000?wsdl

# Start the application
CMD ["ruby", "app.rb", "-o", "0.0.0.0", "-p", "5000"]