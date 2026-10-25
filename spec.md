# Service Specification — Lab 3

Author: Abdrakhmanova Adel
Version: 2

## 1. Purpose

The purpose of this service is to demonstrate a stateless REST API
implemented in Python using Flask.

In Laboratory Work 3 the service is containerized using Docker
and deployed in multiple replicas using Kubernetes.

## 2. Endpoints

| ID | Method | Path | Input | Output | Response Codes |
|---|---|---|---|---|---|
| R1 | POST | /echo | {"message": "string"} | {"reply": "string"} | 200, 400 |
| R2 | GET | /time | none | {"time": "string", "served_by": "string"} | 200 |

### R1 — Echo

The client sends:

{"message": "hello"}

The service returns:

{"reply": "hello"}

If the message field is missing or is not a string,
HTTP 400 is returned.

### R2 — Current Time

Returns the current server time and the hostname
of the container or Kubernetes pod that processed the request.

Example:

{
  "time": "2026-10-25 23:30:00",
  "served_by": "my-api-12345"
}

## 3. Constraints

- The service uses HTTP.
- JSON is used for data exchange.
- Python 3 and Flask are used.
- The application listens on port 5000.
- The application listens on 0.0.0.0 inside the container.
- Docker is used for containerization.
- Kubernetes is used for deployment and scaling.
- The application is stateless.
- Queue processing from Laboratory Work 2 is outside the scope of Lab 3.

## 4. Non-functional Requirements

- N1: /echo should respond within 200 ms under normal local execution.
- N2: /time should respond within 200 ms under normal local execution.
- N3: Kubernetes must maintain 3 running replicas during normal operation.
- N4: after deleting one pod, Kubernetes must automatically create a replacement.
- N5: the deployment must be scalable from 3 to 5 replicas.

## 5. Assumptions

- A1: Docker Desktop is installed and running.
- A2: minikube and kubectl are installed.
- A3: at least 8 GB of RAM is available.
- A4: all replicas run the same Docker image.