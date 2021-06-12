FROM i386/ubuntu
WORKDIR '/bufferoverflow'
RUN apt-get update
# Install editors
RUN apt install -y vim nano
# Install build essentials
RUN apt install -y build-essential
# Install gdb
RUN apt install -y gdb
# Install pwntools
RUN apt install -y python3 python3-pip python3-dev
RUN apt install -y git libssl-dev libffi-dev
RUN pip3 install --upgrade pip
RUN export CRYPTOGRAPHY_DONT_BUILD_RUST=1 && pip3 install pwntools
# Set encoding
ENV PYTHONIOENCODING=utf8
# Copy binaries
COPY binaries ./binaries
COPY exploit-templates .
ENTRYPOINT ["/bin/bash"]