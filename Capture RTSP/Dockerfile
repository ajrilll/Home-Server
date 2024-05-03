FROM python:latest

WORKDIR /app

COPY . .

RUN pip install opencv-python
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

CMD ["python", "app.py"]
