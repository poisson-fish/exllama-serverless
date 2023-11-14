FROM runpod/pytorch:2.0.1-py3.10-cuda11.8.0-devel-ubuntu22.04

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN mkdir data
WORKDIR /data

# Install Python dependencies (Worker Template)
# Yi model support in VLLM requires a source build
RUN git clone https://github.com/vllm-project/vllm.git
WORKDIR vllm
RUN pip install -e .
RUN pip install runpod

COPY handler.py /data/handler.py
COPY schema.py /data/schema.py
COPY config.py /data/config.py
COPY inference.py /data/inference.py
COPY __init.py__ /data/__init__.py

CMD [ "python", "-m", "handler" ]
