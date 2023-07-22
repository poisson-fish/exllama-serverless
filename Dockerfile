FROM runpod/pytorch:3.10-2.0.0-117

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN mkdir data
WORKDIR /data

# Fetch the model
# RUN git clone --progress https://huggingface.co/TheBloke/guanaco-65B-GPTQ
# model is now fetched by worker

# Install Python dependencies (Worker Template)
RUN pip install --upgrade pip && \
    pip install safetensors==0.3.1 sentencepiece ninja huggingface_hub runpod numpy
RUN git clone https://github.com/turboderp/exllama
RUN pip install -r exllama/requirements.txt

COPY handler.py /data/handler.py
COPY schema.py /data/schema.py
COPY config.py /data/config.py
COPY inference.py /data/inference.py
COPY __init.py__ /data/__init__.py

ENV PYTHONPATH=/data/exllama

CMD [ "python", "-m", "handler" ]
