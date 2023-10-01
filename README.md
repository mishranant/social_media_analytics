# Social Media Analytics Platform

This is a microservice-based social media analytics platform built with Django and Python. It allows users to create, retrieve, and analyze social media posts. This README provides instructions for setting up and running the application, details about its infrastructure and scaling considerations, and information about assumptions and decisions made during development.

## Table of Contents

1. [Setup](#setup)
2. [Infrastructure and Scaling](#infrastructure-and-scaling)
3. [Assumptions and Decisions](#assumptions-and-decisions)

## Setup

To run this application locally, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/mishranant/social_media_analytics.git
   cd social_media_analytics

2. **Create a Virtual Environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt

4. **Migrate the Database:**

    ```bash
    python manage.py migrate

5. **Run the Development Server:**

    ```bash
    python manage.py runserver

6. **Access the Application:**

    Open your web browser and navigate to http://127.0.0.1:8000/ to access the application.

## Infrastructure and Scaling

Database: For simplicity, this project uses SQLite. In production, we will consider using a more robust database like PostgreSQL.

Scaling: To handle high request volumes, we have implemented caching. We will be considering load balancing, asynchronous processing, and horizontal scaling while deploying. We will utilize cloud services and containers for scalability.

## Assumptions and Decisions

Database Choice: SQLite is used for its simplicity in development.

Cache Framework: Django's built-in caching framework is used for caching frequently accessed data.

Deployment: We will consider using cloud platforms like AWS for deployment, ensuring high availability and scalability.

Security: Some basic form of input validation is already implemented.

Monitoring and Logging: Use tools like Prometheus and Grafana for monitoring and centralized logging for debugging.

Testing: Unit tests are implemented for the APIs. At later stages, more unit tests, integration tests, and load testing have to be added to ensure the application's reliability.