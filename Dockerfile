
# Official image!
FROM python:3.14-slim

# My Working Directory
WORKDIR /ep1_helloworld

# Copy the code into the container
COPY main.py .

# Run python, execute main-py
CMD ["python", "main.py"]