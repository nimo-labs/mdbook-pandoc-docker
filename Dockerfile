FROM debian:testing-slim

RUN apt-get update \
    && apt-get install -y \
    cargo texlive-latex-base texlive-latex-recommended texlive-fonts-extra pandoc \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && rm -rf /root/.cache

RUN cargo install mdbook mdbook-toc mdbook-pandoc

ENV PATH="${PATH}:/root/.cargo/bin"
WORKDIR /book

# RUN apt -y update
# RUN apt -y install  

CMD ["mdbook","build"]
