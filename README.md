# UCore2
UCore V2-UCore第二版，完全使用python重构的UCore
## 快速开始
（这次大泽依然在仓库里扔了一枚一毛一样的UST工程）  
#### 0x01 准备本体：
1. 安装git和python  
`# apt-get update \`  
`&& apt-get install -y python3 git python3-pip`
2. git clone  
`git clone https://github.com/daze456/UCore2.git`
#### 0x02 准备音源：  
1. 从[这里](https://daze456.github.io/zew/data/ZeW_Bata_0.1.0.191225.7z)下载泽小白数据  
2. 解压缩到仓库下的voice文件夹
#### 0x03 准备引擎
1. 安装cmake  
`# apt-get update \`  
`&& apt-get install -y cmake build-essential`
2. 下载并编译RUCE  
`$ cd engine \`  
`&& git clone https://github.com/Rocaloid/RUCE.git \`    
`&& cd RUCE \`  
`&& ./configure \`  
`&& cd build && make \`  
`&& cd ../ && cd ../ && cd ../`  
3. 下载并编译wavtool  
`$ git clone https://github.com/m13253/wavtool-yawu.git \`    
`&& cd wavtool-yawu \`  
`&& ./configure \`  
`&& cd build && make \`  
`&& cp ./wavtool-yawu ../ && cd .. \`  
`&& cp ./wavtool-yawu ../wavtool/ && cd .. \`  
`&& rm -rf wavtool-yawu/`
##### 0x04 合成
`$ python3 ucore.py example.ust`  
输出文件为`output.wav`  

话说各位注意到那个`dockerfile`了吗？（可能有BUG，所以没公开）  
## 配置文件
配置文件:`cfg.ini`,跟UC1差不多  
`;UCore配置文件开始`  
`[ucore]`  
`;设置默认使用的声库`  
`oto=./voice/ZeW_Bata_0.1.0.191225`  
`;设置默认wavtool（工具1）`  
`tool=./wavtool/wavtool-yawu`  
`;设置默认resampler（工具2）`  
`resamp=./engine/RUCE-1.0.0-alpha2/RUCE_Win.sh`  
`;设置默认缓存文件夹`  
`cachedir=./cache`  
`;设置输出文件`  
`output=./output.wav`  
`;UCore配置文件结束`  
注：由于easyust存在~~特性~~BUG，所以在这里没有可选参数，而且参数以配置文件为准，请认真填写
## 使用方法
`$ python3 ucore.py <UST> [Singer] [output]`  
`UST：输入文件`  
`Singer：歌姬`  
`output：输出文件`
## 使用例：
1. 类似口袋歌姬的在线合成服务
2. 在游戏 OR 软件中使用UTAU的技术（类似VOCALOID SDK for Unity）
## 灵感
最初的设计灵感见[UC1.md](./UC1.md#开发灵感)  
然后，UC1开发出来没几天，我的SSD就挂（die）了  
后来硬盘拿去维修了，我就只能用我U盘里的Deepin Linux了。。。   
然而在Linux下我没法调教我家泽小白啊，于是我就用Python重构了我的UCore  
然后，就有了UC2  
话说UC1和UC2哪个快呢？  
还有个秘密，UC2是我做出的第一个Python程序，而且是边学python边做出来的（什么？你说easyust？这货只是UC2的附属产品）
## TODO
WebSocket，我已经在崔自己了  
（其实WebSocket已经涉及TCP连接了，大泽表示压力山大）  
（另外SV已经出网页版了，我压力更大）  