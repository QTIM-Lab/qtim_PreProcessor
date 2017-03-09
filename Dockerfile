FROM dit4c/dit4c-container-base:debian
LABEL maintainer "Andrew Beers <andrew_beers@alumni.brown.edu>"

# All processing will happen from the home directory.
WORKDIR /home

# Install NeuroDebian
RUN wget -O- http://neuro.debian.net/lists/jessie.us-ca.full | sudo tee /etc/apt/sources.list.d/neurodebian.sources.list && \
  apt-key adv --recv-keys --keyserver hkp://pgp.mit.edu:80 0xA5D32F012649A5A9 && \
  apt-get update

# Install FSL with NeuroDebian
RUN sudo DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes fsl-5.0-complete

# Install Slicer
RUN SLICER_URL="http://download.slicer.org/bitstream/461634" && \
    curl -v -s -L $SLICER_URL | tar xz -C /tmp && \
    mv /tmp/Slicer* /opt/slicer

# Install FreeSurfer
RUN bash && \
  wget ftp://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/6.0.0/freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.0.tar.gz && \
  tar -C /usr/local -xzvf freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.0.tar.gz && \
  rm freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.0.tar.gz

# Install ANTS
WORKDIR /home
RUN wget "https://github.com/stnava/ANTs/releases/download/v2.1.0/Linux_Debian_jessie_x64.tar.bz2" && \
  sudo DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes bzip2 && \
  tar -C /usr/local -xjf Linux_Debian_jessie_x64.tar.bz2 && \
  rm Linux_Debian_jessie_x64.tar.bz2

# Install required python packages.
RUN sudo DEBIAN_FRONTEND=noninteractive apt-get -y --force-yes install python-pip python2.7-dev && \
  pip install qtim_tools nibabel pydicom

# Pull git repository with relevant python scripts.
RUN echo UPDATING_GIT
RUN git clone https://github.com/QTIM-Lab/qtim_PreProcessor /home/qtim_PreProcessor

# Environmental Variables
ENV FSLDIR /usr/share/fsl/5.0
ENV FREESURFER_HOME /usr/local/freesurfer 
ENV PATH "$PATH:/opt/slicer"
ENV PATH "$PATH:${FSLDIR}/bin"
ENV PATH "$PATH:/usr/local/debian_jessie"

# FreeSurfer License
RUN mv /home/qtim_PreProcessor/PreProcessing_Library/Scripts/FreeSurfer_Resources/license.txt /usr/local/freesurfer

# Startup Scripts
RUN echo "source $FREESURFER_HOME/SetUpFreeSurfer.sh" >> ~/.bashrc
RUN echo "source ${FSLDIR}/etc/fslconf/fsl.sh" >> ~/.bashrc

# Commands at startup.
# ENTRYPOINT /bin/bash
CMD /bin/bash -c "source /root/.bashrc && cd /home/data && python pipeline_script.py"