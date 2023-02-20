FROM python:2.7-slim

# Add user to run the server
RUN useradd -ms /bin/bash serverb
USER serverb
WORKDIR /home/serverb
ENV PATH="/home/serverb/.local/bin:${PATH}"

# Installs all python requirements
COPY --chown=serverb:serverb server_b/requirements.txt .
RUN pip install --user -r requirements.txt

# Copy source files and start flask server
COPY server_b/ .

# Expose port 5000 for the SOAP server
EXPOSE 5000

# Start the SOAP server when the container starts
CMD ["python", "app.py"]
