FROM pjestrada/todobackend-base:latest
MAINTAINER Pablo Estrada <pjestadac@gmail.com>


# Copy application artifacts
COPY target /wheelhouse

# Install application
RUN . /appenv/bin/activate && \
    pip install --no-index -f /wheelhouse todobackend && \
rm -rf /wheelhouse
