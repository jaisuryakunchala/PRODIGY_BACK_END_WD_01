PROJECT STRUCTURE:
user_api/
│
├── main.py
├── requirements.txt
└── README.md

Clone the Repositor
Create Virtual Environment (Optional but Recommended):
 "python -m venv venv"
Activate:
   windows: "venv\Scripts\activate"
   Linux / Mac: "source venv/bin/activate"

Install Dependencies: "pip install fastapi uvicorn pydantic[email]"
Running the Application: python -m uvicorn main:app --reload
server run at: "http://127.0.0.1:8000/"        
Swagger UI: "http://127.0.0.1:8000/docs"
ReDoc : "http://127.0.0.1:8000/redoc"
