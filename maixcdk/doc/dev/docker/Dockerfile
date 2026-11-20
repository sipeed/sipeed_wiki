FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

EXPOSE 8888
EXPOSE 2333

RUN dpkg --add-architecture i386 \
    && apt-get -o APT::Retries=3 update -y

RUN apt-get update \
    && apt-get install -y software-properties-common \
    && add-apt-repository -y ppa:deadsnakes/ppa\
    && apt-get update \
	&& apt-get install build-essential vim \
        git libncurses5-dev zlib1g-dev gawk \
        libssl-dev unzip lib32z1 lib32z1-dev lib32stdc++6 libstdc++6 \
        ca-certificates file g++-multilib libc6:i386 locales \
        python3 python3-pip rsync shellcheck \
        libopencv-dev libopencv-contrib-dev \
        libsdl2-dev \
        python3.11 python3.11-venv python3.11-dev \
        unzip wget sudo -y \
    && rm /usr/bin/python3 \
    && ln -s /usr/bin/python3.11 /usr/bin/python3 \
    && python3 -m ensurepip --upgrade \
    && apt-get purge -yq \
    && apt-get autoremove -yq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/*

COPY requirements.txt /tmp/requirements.txt
COPY teedoc_requirements.txt /tmp/teedoc_requirements.txt

# RUN python3 -m pip install --upgrade pip
# RUN python3 -m pip install cmake teedoc
# RUN python3 -m pip install -r /tmp/requirements.txt
# RUN python3 -m pip install -r /tmp/teedoc_requirements.txt

RUN python3 -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN python3 -m pip install cmake teedoc -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN python3 -m pip install -r /tmp/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN python3 -m pip install -r /tmp/teedoc_requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN ln -s /usr/bin/python3 /usr/bin/python

COPY switch_user.sh /usr/local/bin/switch_user.sh
RUN chmod +x /usr/local/bin/switch_user.sh
ENTRYPOINT ["/usr/local/bin/switch_user.sh"]


