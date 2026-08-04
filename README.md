## MODULE 14
   This project extends the existing FastAPI calculator application by implementing a new calculation feature: Modulus (%).
   The feature includes backend logic, database integration, UI updates, and full test coverage (unit, integration, and Playwright E2E).
   A complete CI/CD pipeline builds, tests, scans, and deploys the application to Docker Hub.

## 🔧 Implemented Feature: Modulus (%) Operation
   ✔ Backend
      Added modulus logic to the calculation service
      Updated FastAPI route to support the new operation
      Updated Pydantic schemas to validate modulus input
      Stored modulus results in PostgreSQL
      Included error handling for invalid input (non‑numeric values, empty fields)

   ✔ Front-End
      Added “Modulus %” to the operation dropdown
      Updated dashboard UI to display modulus results
      Added error and success alerts
      Updated history table to show modulus calculations
      Client-side validation for malformed input

   ✔ Testing
      Unit Tests: modulus logic, input parsing, error handling
      Integration Tests: FastAPI route, DB persistence, history retrieval
      E2E Tests (Playwright):
      modulus with two numbers
      modulus with three numbers
      invalid input
      history updates

      all other operations (addition, subtraction, multiplication, division)

   ✔ Database Migrations
      This feature did not require schema changes, so no Alembic migrations were needed.

# 📦 Project Setup
   Clone
   git clone https://github.com/davidb9790/module14_is601.git
   cd module14_is601


#   Create Virtual Environment
   python3 -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate.bat  # Windows

---
## Install Dependencies
   pip install -r requirements.txt

## Start FastAPI
   uvicorn app.main:app --reload
   
   API will be available at:
   http://localhost:8000

## Database Setup
   docker compose up --build

   If PgAdmin tables do not appear:
      docker compose down -v
      docker compose up --build


## Running Test Locally
   Unit Test
      pytest tests/unit

   Integration Test
      pytest tests/integration/

   E2E Test
      Install browsers first:
      python -m playwright install

      pytest tests/e2e/


---

#  CI/CD Pipeline (GitHub Actions)

   The GitHub Actions workflow for this project provides a full CI/CD pipeline that automatically tests, builds, scans, and deploys the application.

   What the pipeline does
   Spins up a PostgreSQL service for testing

   Installs project dependencies

   Installs Playwright and required browsers

   Starts the FastAPI application

   Runs all unit, integration, and E2E tests

   If all tests pass:

   Builds the Docker image

   Logs into Docker Hub

   Pushes the image to the Docker Hub repository

   Runs a Trivy security scan on the built image

   🔐 Required GitHub Secrets
   Add these under:

   GitHub → Repository → Settings → Secrets and Variables → Actions

   DOCKERHUB_USERNAME
      Your Docker Hub username
      Must match the account that owns the repository

   DOCKERHUB_TOKEN
      Create this in Docker Hub under
      Account Settings → Security → Personal Access Tokens
      Steps:
         Generate a new token
         Give it Read & Write permissions
         Copy the token and save it as the GitHub secret
 

   Adding the secrets in GitHub
      Go to your repository
      Open Settings → Secrets and Variables → Actions
      Click New Repository Secret

   Add:

   DOCKERHUB_USERNAME
   DOCKERHUB_TOKEN

   Once these are set, the pipeline will automatically:
   run tests on every push or pull request to main
   build and push the Docker image only when tests pass


---
