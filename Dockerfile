FROM alpine

RUN <<EOF
mkdir /DOWNLOADS/
apk update
apk add wget
EOF

WORKDIR /DOWNLOADS/
