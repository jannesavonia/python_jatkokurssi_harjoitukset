FROM python
# ...
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get -y install gcc
RUN apt-get -y install mono-mcs
#RUN apt-get -y install python3
RUN rm -rf /var/lib/apt/lists/*