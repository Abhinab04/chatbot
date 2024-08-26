FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    gcc \
    portaudio19-dev \
    libasound2-dev \
    pulseaudio \
    pavucontrol \
    alsa-utils \
    espeak \
    jackd2 \
    libjack-jackd2-0 \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m user

RUN mkdir -p /run/user/1000/pulse && chown user:user /run/user/1000/pulse

USER user

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && pip install waitress

ENV PATH="/home/user/.local/bin:$PATH"

COPY . /app

WORKDIR /app

EXPOSE 5000

CMD ["bash", "-c", "pulseaudio --start --exit-idle-time=-1 && waitress-serve --port=5000 app:app"]
