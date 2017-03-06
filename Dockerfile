FROM dit4c/dit4c-container-base
LABEL maintainer "Andrew Beers <andrew_beers@alumni.brown.edu>"

# All processing will happen from the home directory.
WORKDIR /home

# Install NeuroDebian
RUN wget -O- http://neuro.debian.net/lists/jessie.us-ca.full | sudo tee /etc/apt/sources.list.d/neurodebian.sources.list \
  sudo apt-key adv --recv-keys --keyserver hkp://pgp.mit.edu:80 0xA5D32F012649A5A9 \
  sudo apt-get update

# Install FSL with NeuroDebian
RUN sudo apt-get install fsl-5.0-complete

# Install ANTS
# WORKDIR /home
# RUN ANTS_URL="https://github.com/stnava/ANTs/releases/download/v2.1.0/Linux_Ubuntu14.04.tar.bz2" && \
#     curl -v -s -L $ANTS_URL | tar xz -C /tmp && \
#     mv /tmp/ANTS* /opt/ANTS

# Install Slicer
RUN SLICER_URL="http://download.slicer.org/bitstream/461634" && \
    curl -v -s -L $SLICER_URL | tar xz -C /tmp && \
    mv /tmp/Slicer* /opt/slicer

# Install FreeSurfer
RUN wget ftp://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/6.0.0/freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.0.tar.gz \
    tar -C /usr/local -xzvf freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.0.tar.gz \
    export FREESURFER_HOME=/usr/local/freesurfer \
    source $FREESURFER_HOME/SetUpFreeSurfer.sh

# Install required python packages.
RUN pip install qtim_tools nibabel pydicom

# Pull git repository with relevant python scripts.
RUN git clone https://github.com/QTIM-Lab/qtim_Docker/QTIM_Brains_PreProcessing/PreProcessing_Library ./PreProcessing_Library

# Install fsl from python package.






