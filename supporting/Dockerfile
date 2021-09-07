USER root

#RUN wget -q -O /tmp/mrutter.asc "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xe298a3a825c0d65dfd57cbb651716619e084dab9" && \
#    sudo apt-key add /tmp/mrutter.asc && \
#    sudo apt-get update 

RUN sudo DEBIAN_FRONTEND=noninteractive apt install -y vnc4server expect openbox tightvncserver tigervnc-standalone-server tigervnc-xorg-extension tigervnc-viewer xrdp
RUN sudo apt install -y build-essential libcairo2-dev libjpeg-turbo8-dev libpng-dev libtool-bin libossp-uuid-dev libvncserver-dev freerdp2-dev libssh2-1-dev libtelnet-dev libwebsockets-dev libpulse-dev libvorbis-dev libwebp-dev libssl-dev libpango1.0-dev libswscale-dev libavcodec-dev libavutil-dev libavformat-dev
RUN cd /opt && wget http://mirror.cc.columbia.edu/pub/software/apache/guacamole/1.2.0/source/guacamole-server-1.2.0.tar.gz && tar -xvf guacamole-server-1.2.0.tar.gz && cd guacamole-server-1.2.0 && ./configure --with-init-dir=/etc/init.d && sudo make && sudo make install && sudo ldconfig
RUN sudo apt install -y default-jdk tomcat8 tomcat8-admin tomcat8-common tomcat8-user && cd /tmp && wget https://downloads.apache.org/guacamole/1.2.0/binary/guacamole-1.2.0.war && sudo mv guacamole-1.2.0.war /var/lib/tomcat8/webapps/guacamole.war
RUN sudo apt install -y fluxbox

#Install pycharm
RUN cd /opt/ && \
    curl -#SfLOJ https://download.jetbrains.com/python/pycharm-community-2021.2.1.tar.gz && \
    tar -xzf pycharm-community-2021.2.1.tar.gz -C /opt/ && \
    rm pycharm-community-2021.2.1.tar.gz


# Pull required code
RUN mkdir /tmp/thedip && \
    cd /tmp/thedip && \
    git clone https://github.com/vaibhav-dhawan/domino-guacamole-pycharm.git
    
RUN sudo mkdir /etc/guacamole/ && \
    cp /tmp/gittex/domino-guacamole-pycharm/supporting/user-mapping.xml /etc/guacamole/user-mapping.xml && \
    mkdir /var/opt/workspaces/pycharm && \
    cp /tmp/gittex/domino-guacamole-pycharm/supporting/start.sh /var/opt/workspaces/pycharm/start.sh && \
    cp /tmp/gittex/domino-guacamole-pycharm/supporting/rdp.sh /var/opt/workspaces/pycharm/rdp.sh && \
    chmod a+x /var/opt/workspaces/pycharm/*.sh && \
    cp /tmp/gittex/domino-guacamole-pycharm/supporting/guacamole.properties /etc/guacamole/ 
 
    
RUN cd /tmp/gittex/domino-guacamole-pycharm && pip install .