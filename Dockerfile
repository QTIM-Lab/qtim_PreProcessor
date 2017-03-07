FROM dit4c/dit4c-container-base:debian
LABEL maintainer "Andrew Beers <andrew_beers@alumni.brown.edu>"

# All processing will happen from the home directory.
WORKDIR /home

# Install NeuroDebian
RUN wget -O- http://neuro.debian.net/lists/jessie.us-ca.full | sudo tee /etc/apt/sources.list.d/neurodebian.sources.list
RUN sudo apt-key adv --recv-keys --keyserver hkp://pgp.mit.edu:80 0xA5D32F012649A5A9 
RUN sudo apt-get update

# Install FSL with NeuroDebian
RUN sudo DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes fsl-5.0-complete

# Install Slicer
RUN SLICER_URL="http://download.slicer.org/bitstream/461634" && \
    curl -v -s -L $SLICER_URL | tar xz -C /tmp && \
    mv /tmp/Slicer* /opt/slicer

# Install FreeSurfer
RUN bash
RUN wget ftp://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/6.0.0/freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.0.tar.gz
RUN tar -C /usr/local -xzvf freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.0.tar.gz
RUN ln -snf /bin/bash /bin/sh
ENV FREESURFER_HOME /usr/local/freesurfer 
RUN source $FREESURFER_HOME/SetUpFreeSurfer.sh

# Install required python packages.
RUN sudo DEBIAN_FRONTEND=noninteractive apt-get  -y --force-yes install python-pip python2.7-dev
RUN pip install qtim_tools nibabel pydicom

# Install ANTS
WORKDIR /home
RUN wget "https://github.com/stnava/ANTs/releases/download/v2.1.0/Linux_Debian_jessie_x64.tar.bz2"
RUN tar -C /usr/local -xjf Linux_Debian_jessie_x64.tar.bz2

# Pull git repository with relevant python scripts.
RUN git clone https://github.com/QTIM-Lab/qtim_PreProcessor /home/PreProcessing_Library






