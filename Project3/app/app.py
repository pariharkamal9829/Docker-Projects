from flask import Flask
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host="db",
        user="root",
        password="example",
        database="test_db"
    )
    return connection

@app.route('/')
def home():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT 'Your Multi-Container App is Live!'")
    result = cursor.fetchone()
    connection.close()
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>🚀 Welcome to My Docker-Powered Web App 🚀</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                text-align: center;
                padding: 50px;
            }}
            h1 {{
                color: #3498db;
                font-size: 36px;
            }}
            p {{
                font-size: 20px;
                color: #333;
            }}
            .status {{
                margin-top: 20px;
                padding: 15px;
                background-color: #2ecc71;
                color: white;
                font-size: 18px;
                display: inline-block;
                border-radius: 5px;
            }}
        </style>
    </head>
    <body>
        <h1>🌟 Welcome to My Multi-Container App 🌟</h1>
        <p>This application is running inside Docker containers using Flask & MySQL.</p>
        <p>Deployed with <strong>Docker Compose</strong> for a seamless experience!</p>
        <div class="status">
            ✅ {result[0]}
        </div>
    </body>
    </html>
    """
    
    return html_content

if __name__ == "__main__":
    app.run(host='0.0.0.0')
