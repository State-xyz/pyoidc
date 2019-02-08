FROM ubuntu:18.04
MAINTAINER hans.zandbelt@oidf.org

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y \
    git \
    ntp \
    curl \
    gnupg \
    apache2 \
    wget \
    libgconf-2-4 \
    libnss3-tools
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update && apt-get install -y nodejs google-chrome-stable

WORKDIR /root
RUN git clone https://github.com/openid-certification/oidc-provider-conformance-tests.git
WORKDIR /root/oidc-provider-conformance-tests
RUN npm install --production
WORKDIR /root
RUN git clone https://github.com/openid-certification/openid-client-conformance-tests.git
WORKDIR /root/openid-client-conformance-tests
RUN npm install --production

COPY run.sh /root/run.sh
RUN chmod 755 /root/run.sh

ENTRYPOINT /root/run.sh
