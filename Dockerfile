# Use Ubuntu 14.04
FROM ubuntu:14.04

# Install dependencies
RUN apt-get update
RUN apt-get install -y build-essential libevent-dev libffi-dev libmysqlclient-dev libssl-dev nginx supervisor wget git python-dev python-pip cmake
RUN apt-get install -y vim tmux

# Install PIP
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt

# Install OpenCV
RUN git clone --depth 1 --branch 3.1.0 https://github.com/Itseez/opencv.git
RUN cd ./opencv
RUN mkdir ./release
RUN cd release
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local ..
make
sudo make install

EXPOSE 80
CMD ["supervisord", "-n"]
