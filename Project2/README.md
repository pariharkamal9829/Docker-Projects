# Dockerizing a Python Script

This project involves containerizing a Python script that processes data from a CSV file using the **pandas** library. The goal is to make the script portable and executable in any environment using Docker.

## 🧰 Technologies Used
- Docker
- Python
- pandas

## 📂 Project Structure
```
Docker-Projects/
├── project2/
│   ├── Dockerfile
│   ├── process_data.py
│   ├── requirements.txt
│   └── data/
│        └── data.csv
```

## 📜 Step-by-Step Instructions

### 1. Clone the Repository
```bash
# Replace with your repository URL
git clone https://github.com/yourusername/docker-python-script.git
cd docker-python-script/project2
```

### 2. Python Script (process_data.py)

This script reads and processes a CSV file and prints a statistical summary.

```python
import pandas as pd

# Read the CSV file
df = pd.read_csv('data/data.csv')

# Print statistical summary
print(df.describe())
```

### 3. Create the CSV File

Ensure you have a `data.csv` file inside the `data/` directory.

Example `data.csv`:
```csv
name,age,salary
Alice,25,50000
Bob,30,60000
Charlie,35,70000
David,40,80000
Eve,45,90000
```

### 4. Create the requirements.txt File

```bash
pandas
```

### 5. Write the Dockerfile

```Dockerfile
# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy all files to the container
COPY . .

# Define the command to run the script
CMD ["python", "process_data.py"]
```

### 6. Build the Docker Image

```bash
docker build -t python-script .
```

### 7. Run the Docker Container

For **Linux/macOS**:
```bash
docker run -v $(pwd)/data:/app/data python-script
```

For **Windows (PowerShell)**:
```powershell
docker run -v ${PWD}/data:/app/data python-script
```

For **Windows (CMD)**:
```cmd
docker run -v %cd%\data:/app/data python-script
```

### 8. Expected Output

You should see a statistical summary like this:
```
            age       salary
count   5.000000     5.000000
mean   35.000000  70000.000000
std    7.905694  15811.388301
min   25.000000  50000.000000
25%   30.000000  60000.000000
50%   35.000000  70000.000000
75%   40.000000  80000.000000
max   45.000000  90000.000000
```

### 9. Stop and Clean Docker Containers/Images

To remove the container and image:

1. List running containers:
   ```bash
   docker ps -a
   ```

2. Remove a container:
   ```bash
   docker rm <container_id>
   ```

3. Remove the image:
   ```bash
   docker rmi python-script
   ```

## 📌 Troubleshooting

- If you face the error **"Unable to find image 'python-script:latest'"**, ensure you have built the Docker image with the correct tag.

- Check Docker connectivity with:
    ```bash
    docker run hello-world
    ```

## 📚 Resources

- [Docker Documentation](https://docs.docker.com/)
- [pandas Documentation](https://pandas.pydata.org/docs/)

## 📧 Contact
For any questions or suggestions, feel free to open an issue or reach out!

---
**Happy Coding! 🚀**

