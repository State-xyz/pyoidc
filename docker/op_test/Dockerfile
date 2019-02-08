FROM jfloff/alpine-python:3.6
MAINTAINER tomas.pazderka@oidf.org

RUN apk add openssl-dev libffi-dev git

ENV SRCDIR /usr/local/src
ENV INSTDIR oidf
ENV SUBDIR ${SRCDIR}/${INSTDIR}/oidc_op

WORKDIR ${SRCDIR}

RUN git clone https://github.com/openid-certification/otest.git
RUN cd otest && python3 setup.py install && cd -

RUN git clone https://github.com/openid-certification/oidctest.git
RUN cd oidctest && python3 setup.py install && cd -

RUN oidc_setup.py ${SRCDIR}/oidctest ${INSTDIR}
COPY docker/op_test/cert.pem ${SUBDIR}/certs/
COPY docker/op_test/key.pem ${SUBDIR}/certs/
COPY docker/op_test/config.py ${SUBDIR}/
COPY docker/op_test/tt_config.py ${SUBDIR}/
COPY docker/op_test/run.sh ${SUBDIR}/

COPY docker/op_test/https%3A%2F%2Fop%3A4433 ${SUBDIR}/entities/https%3A%2F%2Fop%3A4433
COPY docker/op_test/assigned_ports.json ${SUBDIR}/
COPY docker/op_test/my_jwks_60003.json ${SUBDIR}/static/jwks_60003.json

RUN mkdir pyoidc
COPY . ${SRCDIR}/pyoidc
RUN cd pyoidc && python3 setup.py install && cd -

WORKDIR ${SUBDIR}
ENTRYPOINT ["./run.sh"]
