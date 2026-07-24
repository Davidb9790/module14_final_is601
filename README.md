# 📦 Project Setup
   Clone
   git clone https://github.com/davidb9790/module14_is601.git cd module12_is601_v2

   Create Virtual Environment
   python -m venv venv source venv/bin/activate

   Install Dependencies
   pip install -r requirements.txt

   Running the Application
   python3 main.py

   API will be available at: http://localhost:8000
---
## Install Playwright browsers
   python -m playwright install


---

## Build Docker Image

      docker compose up --build
   
   If the DB for PgAdmin does not create the tables try:
      Docker compose down -v
      Docker compose up --build

---

#  CI/CD Pipeline (GitHub Actions)

   Your GitHub Actions workflow:

   Spins up PostgreSQL (or SQLite depending on your setup)

   Builds the FastAPI app

   Installs Playwright + browsers

   Runs all E2E tests

   If tests pass:

   Builds Docker image

   Logs into Docker Hub

   Pushes the image

   Required GitHub Secrets
   Add these in Settings → Secrets → Actions:

   DOCKERHUB_USERNAME
      Create a repository in Docker Hub: username is simple 
   DOCKERHUB_TOKEN
      Token must be created via Personal Access Tokens
      Generate new token
         Insert name of token
         Access Permissions
            Read & Write
   
   In Github: at the matching repository
   Settings> Secrets and Variables> Actions> New Repository Secret
      DOCKERHUB_USERNAME: Enter your username
      DOCKERHUB_TOKEN: Enter token created in Docker Hub


---

## Create and Activate a Virtual Environment

   (Optional but recommended)

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate.bat  # Windows
   ```
---

# 🧩 Running The Application
   To start the application locally, install the required dependencies and run the FastAPI server. Make sure you have Python and Docker installed. After installing dependencies, start the backend with uvicorn and open the front end in your browser. If you are using Docker, you can run the application using the provided Dockerfile or docker compose file.


---


# Running Tests Locally
T  his project includes unit tests, integration tests, and Playwright end to end tests. Unit and integration tests can be executed with pytest. End to end tests require Playwright and its browser dependencies. After installing Playwright, run the tests using the Playwright test command. All tests should pass before deployment.

# Docker Hub Repository
   The Docker image for this project is available on Docker Hub. The GitHub Actions pipeline builds the image and pushes it automatically after all tests pass. You can pull the image directly from the repository and run it using Docker.