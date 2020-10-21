FROM python:3.7-slim

COPY requirements.txt .
RUN pip3 install -r requirements.txt

WORKDIR /bin
COPY bot.py .

CMD python3 bot.py
