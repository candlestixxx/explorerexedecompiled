# Use an official OpenJDK runtime as a parent image
FROM openjdk:17-jdk-slim

# Set environment variables for Ghidra
ENV GHIDRA_VERSION=11.0
ENV GHIDRA_RELEASE=20231222
ENV GHIDRA_ZIP=ghidra_11.0_PUBLIC_${GHIDRA_RELEASE}.zip
ENV GHIDRA_URL=https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_11.0_build/${GHIDRA_ZIP}

# Install necessary utilities
RUN apt-get update && \
    apt-get install -y wget unzip python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Download and extract Ghidra
WORKDIR /opt
RUN wget --quiet ${GHIDRA_URL} && \
    unzip -q ${GHIDRA_ZIP} && \
    rm ${GHIDRA_ZIP} && \
    mv ghidra_11.0_PUBLIC ghidra

# Set the working directory for analysis
WORKDIR /workspace

# Add Ghidra to PATH
ENV PATH="/opt/ghidra/support:${PATH}"

# Define the entrypoint (can be overridden to run analyzeHeadless)
ENTRYPOINT ["analyzeHeadless"]
