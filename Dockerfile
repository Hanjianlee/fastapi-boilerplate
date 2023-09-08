FROM {docker.source.host}/base-images/ubi-9-minimal/python3.9-runtime

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt -i {internally-hosted-package-url}

COPY ./src /fastapi

WORKDIR /fastapi

CMD ["python3", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]