FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    openjdk-17-jdk \
    unzip \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Mocking Ghidra for the test environment
RUN mkdir -p /opt/ghidra/support
RUN echo '#!/bin/bash\necho "MOCK GHIDRA HEADLESS EXECUTION"' > /opt/ghidra/support/analyzeHeadless
RUN chmod +x /opt/ghidra/support/analyzeHeadless

ENV GHIDRA_INSTALL_DIR=/opt/ghidra
WORKDIR /workspace
