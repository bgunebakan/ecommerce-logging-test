#!/bin/bash

set -e

# Sentry version
SENTRY_VERSION='23.12.0'

# Clone the Sentry self-hosted repository
echo "Cloning Sentry self-hosted repository..."
git clone --depth 1 --branch $SENTRY_VERSION https://github.com/getsentry/self-hosted.git sentry
cd sentry

# Check if Docker and Docker Compose are installed
if ! command -v docker &> /dev/null || ! command -v docker-compose &> /dev/null
then
    echo "Docker and Docker Compose are required but not installed. Please install them first."
    exit 1
fi

# Install Sentry
echo "Installing Sentry..."
./install.sh

echo "Sentry installation complete."
