FROM jfloff/alpine-python:3.6
MAINTAINER tomas.pazderka@oidf.org

RUN apk add openssl-dev libffi-dev git

ENV SRCDIR /usr/local/src
ENV INSTDIR oidf
ENV SUBDIR ${SRCDIR}/${INSTDIR}/oidc_cp_rplib

WORKDIR ${SRCDIR}

RUN git clone https://github.com/openid-certification/otest.git
RUN cd otest && python3 setup.py install && cd -
RUN git clone https://github.com/openid-certification/oidctest.git
RUN cd oidctest && python3 setup.py install && cd -

RUN mkdir pyoidc
COPY . ${SRCDIR}/pyoidc/
RUN cd pyoidc && python3 setup.py install && cd -

RUN oidc_setup.py ${SRCDIR}/oidctest ${INSTDIR}
COPY docker/rp_test/cert.pem ${SUBDIR}/certs/
COPY docker/rp_test/key.pem ${SUBDIR}/certs/
COPY docker/rp_test/conf.py ${SUBDIR}/

COPY docker/rp_test/run.sh ${SUBDIR}/

WORKDIR ${SUBDIR}
ENTRYPOINT ["./run.sh"]
