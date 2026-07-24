FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    openjdk-17-jdk \
    unzip \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Install real Ghidra
RUN wget -q https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_11.0.3_build/ghidra_11.0.3_PUBLIC_20240410.zip -O /tmp/ghidra.zip && \
    unzip -q /tmp/ghidra.zip -d /opt && \
    mv /opt/ghidra_11.0.3_PUBLIC /opt/ghidra && \
    rm /tmp/ghidra.zip

ENV GHIDRA_INSTALL_DIR=/opt/ghidra
ENV PATH="${GHIDRA_INSTALL_DIR}/support:${PATH}"
WORKDIR /workspace
