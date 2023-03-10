FROM ruby:2.6.7

# Set the working directory to /app
WORKDIR /app

# Install a newer version of Bundler
RUN gem install bundler

# Copy the Gemfile and Gemfile.lock into the container
COPY rest/Gemfile rest/Gemfile.lock ./

# Install dependencies
RUN bundle install

# Copy the rest of the application code into the container
COPY rest/ ./

ENV SOAP_CLIENT_URL=http://10.5.0.3:8000?wsdl

# Start the application
CMD ["ruby", "app.rb", "-o", "0.0.0.0", "-p", "5000"]
