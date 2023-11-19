FROM nvidia/cuda:12.1.0-devel-ubuntu22.04 as dev-base

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV SHELL=/bin/bash

RUN mkdir data
WORKDIR /data

RUN apt update
RUN apt upgrade -y
RUN apt install wget unzip python3 python3-pip -y
RUN pip3 install setuptools
# Install Python dependencies (Worker Template)

# Yi model support in VLLM requires a source build
RUN wget https://github.com/vllm-project/vllm/archive/refs/heads/main.zip
RUN unzip main.zip -d vllm
WORKDIR vllm/vllm-main
ENV MAX_JOBS=16
RUN pip install -e .
WORKDIR /data
RUN rm main.zip

COPY handler.py /data/handler.py
COPY schema.py /data/schema.py
COPY config.py /data/config.py
COPY inference.py /data/inference.py
#COPY test_harness.py /data/test_harness.py
CMD [ "python3", "-m", "handler.py" ]
# CMD [ "python3", "test_harness.py" ]