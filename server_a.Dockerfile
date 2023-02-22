FROM ruby:2.7.2

# Set the working directory to /app
WORKDIR /app

# Copy the Gemfile and Gemfile.lock into the container
COPY server_a/Gemfile server_a/Gemfile.lock ./

# Install dependencies
RUN bundle install

# Copy the rest of the application code into the container
COPY server_a/ ./

# Start the application
CMD ["ruby", "app.rb", "-o", "0.0.0.0", "-p", "5000"]
