Flask App (Docker + AWS EC2)

Flask application containerized using Docker and deployed on AWS EC2.
Accessible via public IP and served using Gunicorn.

Live Demo

http://

Preview




 Key Highlights

Flask app served with Gunicorn

Dockerized and deployed on AWS EC2

Public access via port 80

/health endpoint for service check

.dockerignore used to optimize image

Architecture
User → Browser → EC2 → Docker → Gunicorn → Flask
Tech Stack

Flask (Python)

Gunicorn

Docker

AWS EC2

Git & GitHub

Run Locally
docker build -t flask-app .
docker run -d -p 80:80 flask-app

API

/ → UI

/health → returns:

{
  "status": "UP"
}
Project Structure
flask-app-ecs/
├── app.py
├── run.py
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
Deployment (EC2)

Launch EC2 (Ubuntu)

Install Docker

Clone repo

Build Docker image

Run container (-p 80:80)

Allow HTTP (port 80) in security group

What this demonstrates

Docker-based application deployment

Running Flask with a production WSGI server (Gunicorn)

Basic AWS EC2 networking (public IP, security groups)

Debugging issues related to SSH, ports, and permissions

Next Steps

CI/CD pipeline (GitHub Actions)

ECS deployment

Reverse proxy (Nginx)

Logging and monitoring

Author

Satyanarayana K V

