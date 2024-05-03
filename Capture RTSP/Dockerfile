FROM python:latest

WORKDIR /app

COPY . .

RUN pip install websocket-client
RUN pip install pyTelegramBotAPI
RUN pip install opencv-python
RUN pip install pillow
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

CMD ["python", "app.py"]
