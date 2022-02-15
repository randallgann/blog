# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

ENV FLASK_APP flask_blog.py
ENV FLASK_CONFIG docker

WORKDIR /home/flasky

COPY requirements.txt requirements.txt

RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY app app
COPY migrations migrations
COPY flask_blog.py config.py boot.sh ./

# runtime config
EXPOSE 5000
#ENTRYPOINT ["python3"]
ENTRYPOINT ["./boot.sh"]
#ENTRYPOINT ["/bin/bash"]
#CMD ["python3"]