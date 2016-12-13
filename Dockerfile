FROM python:3.5

RUN pip3 install git+https://github.com/aparraga/braviarc.git

RUN pip install Flask

RUN pip install wakeonlan


COPY app.py app.py

CMD python app.py
