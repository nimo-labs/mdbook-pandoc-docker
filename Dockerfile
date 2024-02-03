FROM debian:testing-slim

RUN apt update \
    && apt install -y \
    texlive-latex-base texlive-latex-recommended texlive-fonts-extra pandoc \
    && apt autoremove -y \
    && apt clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && rm -rf /root/.cache

COPY bin/mdreport.py /usr/local/bin
WORKDIR /book

CMD ["mdreport.py","build"]
