FROM python:3.8

# define environment variable(s)
ENV HOST_OS=DEFAULT

WORKDIR .

COPY . .

RUN python3.8 -m pip install pip --upgrade
RUN python3 -m pip install \
        flask \
        psycopg2 \
        requests \
        praw \
        pandas \
        numpy \
        requests

CMD python3 -m src.scraper.scraper --host-os=$HOST_OS

## instructions:
# change dependencies above if needed
# change CMD line to run your main module; see how shu did it in `nlp.Dockerfile'
# `make scraper`
