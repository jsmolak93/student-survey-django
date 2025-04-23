# Completed By: Satya Subrahmanya Gautama Shastry Bulusu Venkata, John Smolak

# student-survey-django

# Student Survey App (Django Version) - SWE 645 Extra Credit

This project is a Python/Django reimplementation of Project #2 from SWE 645. It provides full CRUD operations for student surveys, backed by a MySQL database and deployed to a Kubernetes cluster using a CI/CD pipeline powered by Jenkins, Docker, and GitHub.

---

## Tech Stack

- **Backend**: Django (Python 3.10+)
- **Database**: MySQL (Amazon RDS)
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **CI/CD**: Jenkins + GitHub
- **Cloud Provider**: AWS EC2
- **Public IP Access**: Elastic IPs (for Rancher & Jenkins)

---

# Student Survey App (Django Version) - SWE 645 HW3 Extra Credit

This is the Python/Django reimplementation of our SWE 645 Homework 3 microservices project. It replaces the original Spring Boot backend with Django and retains MySQL as the database. The project is containerized using Docker and deployed through a CI/CD pipeline on Kubernetes via Rancher.

## Tech Stack
- **Python 3.10+**
- **Django 4.x**
- **MySQL (via Amazon RDS)**
- **Docker**
- **Kubernetes (Rancher-managed cluster)**
- **Jenkins (CI/CD pipeline)**
- **GitHub**

## Features
- Full CRUD for survey entries
- Django REST API (`/surveys`)
- Uses Django ORM for data persistence
- Connects to MySQL database hosted on RDS
- CI/CD pipeline builds and deploys Docker image to Kubernetes

## Endpoints (REST API)
| Method | Endpoint         | Description              |
|--------|------------------|--------------------------|
| GET    | `/surveys`       | List all surveys         |
| POST   | `/surveys`       | Create new survey        |
| GET    | `/surveys/{id}`  | Get survey by ID         |
| PUT    | `/surveys/{id}`  | Update survey            |
| DELETE | `/surveys/{id}`  | Delete survey            |

## Project Setup

1. Clone the repo:
   bash
   git clone https://github.com/YOUR_USERNAME/student-survey-django.git
   cd student-survey-django
