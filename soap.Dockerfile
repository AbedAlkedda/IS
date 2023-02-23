FROM python:2.7-slim

# Add user to run the server
RUN useradd -ms /bin/bash soap
USER soap
WORKDIR /home/soap
ENV PATH="/home/soap/.local/bin:${PATH}"

# Installs all python requirements
COPY --chown=soap:soap soap/requirements.txt .
RUN pip install --user -r requirements.txt

# Copy source files and start flask server
COPY soap/ .

# Start the SOAP server when the container starts
CMD ["python", "app.py"]
