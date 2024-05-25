FROM sonarqube:8.9-community

# Instalar curl y zstd, y luego realizar las operaciones necesarias
RUN set -eux; \
    apk add --no-cache --virtual .build-deps zstd curl; \
    rm -f /tmp/libz.tar; \
    curl -LfsS https://archive.archlinux.org/packages/z/zlib/zlib-1%3A1.2.12-2-x86_64.pkg.tar.zst -o /tmp/libz.tar.zst; \
    mkdir /tmp/libz; \
    zstd -d /tmp/libz.tar.zst --output-dir-flat /tmp; \
    tar -xf /tmp/libz.tar -C /tmp/libz; \
    mv /tmp/libz/usr/lib/libz.so* /usr/glibc-compat/lib; \
    apk del --purge .build-deps; \
    rm -rf /tmp/*.apk /tmp/libz* /var/cache/apk/*;

