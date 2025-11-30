
# Official image!
FROM python:3.14-slim

# My Working Directory
WORKDIR /ep1_helloworld

# Copy the reqs. file
COPY requirements.txt .

# Pip install numpy!
RUN pip install -r requirements.txt

# Copy the code into the container
COPY main.py .

# Run python, execute main-py
CMD ["python", "main.py"]