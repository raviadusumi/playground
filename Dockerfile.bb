FROM artprod.dev.bloomberg.com/dpkg-python-development-base:3.9

RUN apt-get -y --force-yes install python3.9-hostinfo
RUN pip3.9 install pytest

WORKDIR /workdir

# Copy the current directory contents into the container at /app
ADD . /workdir

# Install any needed packages specified in requirements.txt

CMD [ "python3.9", "-m" , "pytest" ]
