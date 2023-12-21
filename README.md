# E-commerce Logging Test

This guide provides step-by-step instructions on how to deploy and configure e-commerce logging system.

## Prerequisites

Make sure you have Docker and Docker Compose installed on your system.

## Deployment Steps

### Step 1: Environment Configuration

Copy the sample environment file to create your own `.env` file:

```bash
cp .env.sample .env
```

Edit the `.env` file with your specific variables.

### Step 2: Running the Application

Run the following command to build and start the application.

```bash
docker-compose up --build -d
```

The application will create 5 replicas, which will use ports 5001-5005.

### Step 3: Testing the Web Interface

Once the application is running, you can test the web interface by navigating to:

```
http://127.0.0.1:5001/
```

This will open the application in your web browser.

### Step 4: Installing the Logging System

Run the logging system installation script:

```bash
./install_logging.sh
```

This script will install Sentry on your system. During the installation, you will be prompted to answer questions and create a user. Please follow the instructions.

### Step 5: Run Sentry
Run the following command to run sentry containers.

```bash
cd sentry
docker compose up -d
```

### Step 6: Sentry Configuration

After installing Sentry, follow the instructions for Sentry configurations to properly set it up for your application's logging needs.
Get help from Sentry docs. https://docs.sentry.io/product/sentry-basics/integrate-backend/