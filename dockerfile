FROM debian
RUN apt-get update \
&& apt-get install -y python3 git python3-pip cmake build-essential p7zip-full wget wine \
&& git clone https://github.com/daze456/UCore2.git \
&& cd UCore2 \
&& wget https://daze456.github.io/zew/data/ZeW_Bata_0.1.0.191225.7z \
&& 7z x ZeW_Bata_0.1.0.191225.7z -r -o./voice/ZeW_Bata_0.1.0.191225 \
&& rm -rf ZeW_Bata_0.1.0.191225.7z \
&& git clone https://github.com/m13253/wavtool-yawu.git \
&& cd wavtool-yawu \
&& ./configure \
&& cd build && make \
&& cp ./wavtool-yawu ../ && cd .. \
&& cp ./wavtool-yawu ../wavtool/ && cd .. \
&& rm -rf wavtool-yawu/ \
&& wget http://rocaloid.github.io/resources/binaries/RUCE-1.0.0-alpha2.zip \
&& unzip RUCE-1.0.0-alpha2.zip -d ./engine \
&& rm RUCE-1.0.0-alpha2.zip