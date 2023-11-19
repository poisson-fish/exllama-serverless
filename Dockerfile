FROM nvidia/cuda:12.1.0-devel-ubuntu22.04 AS dev

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN mkdir data
WORKDIR /data

RUN apt update && apt install wget unzip python3 python3-pip -y

# Install Python dependencies (Worker Template)
ENV CUDA_HOME=/usr/local/cuda-12.1

# Yi model support in VLLM requires a source build
RUN wget https://github.com/vllm-project/vllm/archive/refs/heads/main.zip
RUN unzip main.zip -d vllm
WORKDIR vllm/vllm-main
RUN pip install -e .
WORKDIR /data
RUN rm -rf main.zip

COPY handler.py /data/handler.py
COPY schema.py /data/schema.py
COPY config.py /data/config.py
COPY inference.py /data/inference.py
COPY __init.py__ /data/__init__.py
ENTRYPOINT [ "python3", "-m", "/data/handler.py" ]