# FastAPI 

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.1-green)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange)

A FastAPI-based Todo application with user registration and authentication using JWT. Uses MySQL as the database.

---

## Setup Instructions

Follow these steps to set up the project locally.

---

### **Step 1: Set up environment and dependencies**

Copy and run the following commands step by step:

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file from example
cp .env.example .env

# 5. Edit .env with your configuration
# Example:
# DATABASE_URL="mysql+pymysql://USERNAME:PASSWORD@localhost:3306/DATABASE_NAME"
# SECRET_KEY=super
# ALGORITHM=HS256
# ACCESS_TOKEN_EXPIRE_MINUTES=30


---

### **Step 2: Run the FastAPI server
uvicorn main:app --reload
The API will be available at: http://localhost:8000
---

### **Step 3: Access API docs
FastAPI provides interactive API documentation at:
Swagger UI: http://localhost:8000/docs
Redoc: http://localhost:8000/redoc
