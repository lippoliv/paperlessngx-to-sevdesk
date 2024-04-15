FROM python:3.12.3-slim

MAINTAINER Oliver Lippert <oliver@lipperts-web.de>

ENV RUN_INTERVAL=300
ENV PAPERLESSNGX_URL=""
ENV PAPERLESSNGX_TOKEN=""
ENV PAPERLESSNGX_FILTER_TAG_ID=0
ENV PAPERLESSNGX_FILTER_DOCUMENT_TYPE_ID=0
ENV SEVDESK_TOKEN=""

VOLUME /app/workdir

COPY src /app

WORKDIR /app

RUN pip install pipenv
RUN pipenv sync

CMD pipenv run python main.py