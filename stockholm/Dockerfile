FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y --no-install-recommends \
	python3 \
	python3-pip \
	python3-venv \
	sudo \
	&& apt clean

COPY requirements.txt ./

RUN python3 -m venv /opt/venv && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

ENV PATH="/opt/venv/bin:$PATH"

COPY infection /root/infection

WORKDIR /app

CMD ["bash", "-c", "bash"]