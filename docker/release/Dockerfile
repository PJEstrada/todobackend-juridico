FROM pjestrada/todobackend-base:latest
MAINTAINER Pablo Estrada <pjestadac@gmail.com>


# Copy apps artifacts
COPY target /wheelhouse
RUN chmod +x /

# Install application
RUN . /appenv/bin/activate && \
	pip install --no-index -f /wheelhouse todobackend && \
	rm -rf /wheelhouse


