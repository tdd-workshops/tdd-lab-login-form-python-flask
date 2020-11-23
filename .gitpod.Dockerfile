FROM gitpod/workspace-full:latest

USER gitpod

RUN python3 -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt
