FROM jenkins/jenkins:lts

USER root

RUN apt-get update && apt-get install -y \
    rpm \
    build-essential \
    dpkg-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

USER jenkins
