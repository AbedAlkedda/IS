FROM python:3.10.4 AS app

# Add user to run the server
RUN useradd -ms /bin/bash serverb
USER serverb
WORKDIR /home/serverb
ENV PATH="/home/serverb/.local/bin:${PATH}"

# Installs all python requirements, including the qaclient package built by the client-builder stage
COPY --chown=serverb:serverb server_b/requirements.txt .
RUN pip install --user -r requirements.txt

# Copy source files and start flask server
COPY server_b/ .
CMD ["flask", "run", "--host", "0.0.0.0"]
