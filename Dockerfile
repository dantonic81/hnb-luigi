FROM axiom/docker-luigi:2.7.9-alpine

# Install build dependencies
RUN apk add --no-cache build-base postgresql-dev

# Copy the requirements.txt file containing the Python dependencies
COPY requirements.txt /tmp/requirements.txt

# Install the Python dependencies
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Clean up
RUN rm /tmp/requirements.txt