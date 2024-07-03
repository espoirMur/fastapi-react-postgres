FROM python:3.12-slim-bullseye as base
LABEL maintainer="Espoir Murhabazi<espoir.mur [] gmail>"


# Never prompt the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 
ENV PYROOT /pyroot
ENV PYTHONUSERBASE $PYROOT

FROM base AS python-deps
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential\
        software-properties-common
RUN mkdir -p $PYROOT
COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv 
RUN PIP_USER=1 PYTHONUSERBASE=$PYROOT pipenv install --system 

FROM base AS runtime
WORKDIR ${WORKING_DIR}

COPY --from=python-deps $PYROOT/lib $PYROOT/lib
COPY --from=python-deps $PYROOT/bin $PYROOT/bin

RUN ls -la $PYROOT
RUN useradd --create-home es.py
RUN mkdir /home/es.py/fastapi
ENV WORKING_DIR=/home/es.py/fastapi

WORKDIR ${WORKING_DIR}

ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
ENV PATH="$PYROOT/bin:$PATH"
ENV PATH="$PYROOT/lib:$PATH"
ENV PYTHONPATH="${PYTHONPATH}:${WORKING_DIR}"
COPY ./api ${WORKING_DIR}/api


RUN chown -R es.py:es.py ${WORKING_DIR}
RUN chmod -R 755 ${WORKING_DIR}
USER es.py
EXPOSE 8000
# 
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
