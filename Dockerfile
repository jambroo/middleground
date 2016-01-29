# https://tika.apache.org/1.11/configuring.html
# Check out bottom



FROM ubuntu:latest
MAINTAINER david@logicalspark.com

ENV TIKA_VERSION 1.11
ENV TIKA_SERVER_URL https://www.apache.org/dist/tika/tika-server-$TIKA_VERSION.jar

RUN     apt-get update \
        && apt-get install openjdk-7-jre-headless curl gdal-bin tesseract-ocr \
                tesseract-ocr-eng tesseract-ocr-ita tesseract-ocr-fra tesseract-ocr-spa tesseract-ocr-deu -y \
        && curl -sSL https://people.apache.org/keys/group/tika.asc -o /tmp/tika.asc \
        && gpg --import /tmp/tika.asc \
        && curl -sSL "$TIKA_SERVER_URL.asc" -o /tmp/tika-server-${TIKA_VERSION}.jar.asc \
        && NEAREST_TIKA_SERVER_URL=$(curl -sSL http://www.apache.org/dyn/closer.cgi/${TIKA_SERVER_URL#https://www.apache.org/dist/}\?asjson\=1 \
                | awk '/"path_info": / { pi=$2; }; /"preferred":/ { pref=$2; }; END { print pref " " pi; };' \
                | sed -r -e 's/^"//; s/",$//; s/" "//') \
        && echo "Nearest mirror: $NEAREST_TIKA_SERVER_URL" \
        && curl -sSL "$NEAREST_TIKA_SERVER_URL" -o /tika-server-${TIKA_VERSION}.jar \
        && gpg --verify /tmp/tika-server-${TIKA_VERSION}.jar.asc /tika-server-${TIKA_VERSION}.jar \
        && apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
        && mkdir -p /root/src/geotopic-mime && cd /root/src/geotopic-mime \
        && mkdir -p /root/org/apache/tika/mime \
        && cd /tmp/ && curl -O https://raw.githubusercontent.com/chrismattmann/geotopicparser-utils/master/mime/org/apache/tika/mime/custom-mimetypes.xml \
        && mv custom-mimetypes.xml /root/org/apache/tika/mime

RUN java -jar /tika-server-${TIKA_VERSION}.jar --help

EXPOSE 9998
#ENTRYPOINT java -classpath ~/src/geotopic-mime:. -jar /tika-server-${TIKA_VERSION}.jar -h 0.0.0.0
ENTRYPOINT ls
#java -classpath /root/src/geotopic-mime:/tika-server-${TIKA_VERSION}.jar org.apache.tika.server.TikaServerCli  -h 0.0.0.0
