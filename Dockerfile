FROM python:3.10-slim

ARG WORKDIR=.
ARG BUILD_ENVIRONMENT=requirements/base.txt

COPY . ${WORKDIR}
RUN pip install --upgrade pip
RUN pip install -r ${BUILD_ENVIRONMENT}
RUN pip wheel --wheel-dir ${WORKDIR}/wheels -r ${BUILD_ENVIRONMENT}

ENV PYTHONUNBUFFERED 1
RUN pip install --no-cache-dir --no-index --find-links=${WORKDIR}/wheels/ ${WORKDIR}/wheels/* \
	&& rm -rf ${WORKDIR}/wheel

ENTRYPOINT ["python", "-m", "main"]