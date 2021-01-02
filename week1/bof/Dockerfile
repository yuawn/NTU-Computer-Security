FROM ubuntu:18.04
MAINTAINER yuawn
RUN apt-get update
RUN apt-get install xinetd -y
RUN useradd -m bof
RUN chmod 774 /tmp
RUN chmod -R 774 /var/tmp
RUN chmod -R 774 /dev
RUN chmod -R 774 /run
RUN chmod 1733 /tmp /var/tmp /dev/shm
RUN chown -R root:root /home/bof
CMD ["/usr/sbin/xinetd","-dontfork"]