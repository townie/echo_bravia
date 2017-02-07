FROM python:3.5

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Bravia Keys
ENV BRAVIA_PIN 7793
ENV BRAVIA_IP 192.168.1.158
ENV BRAVIA_MAC FC:F1:52:4B:2B:2A


COPY app.py app.py
CMD python app.py
