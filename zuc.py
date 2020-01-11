#/usr/python3
# -*- coding:utf-8 -*-

import sys,configparser,os
import easyust.easyust as easyust

def wavtool(bin,output,input,stp,length,tempo,p,debug = 'no') :
    execmd = bin + ' ' + output + ' ' + input + ' ' + stp + ' ' + length + '@' + tempo + '+.0 ' + p
    if debug == 'yes' :
        print('wavtool：',bin)
        print('输出：',output)
        print('输入：',input)
        print('stp：',stp)
        print('长度：',length)
        print('节奏：',tempo)
        print('执行：',execmd)
    os.system(execmd)

def resamp(bin,output,input,note,vel,debug = 'no') :
    execmd = bin + ' ' + input + ' ' + output + ' ' + note + ' ' + vel
    if debug == 'yes' :
        print('resamper：',bin)
        print('输出：',output)
        print('输入：',input)
        print('音符：',note)
        print('速度：',vel)
        print('执行：',execmd)
    os.system(execmd)

def synth(bt1,bt2,output,oto,tmpd,stp,length,tempo,p1,note,vel,num,lyric,debug = 'no'):
    #重采样
    rin = oto + '/' + lyric + '.wav'
    rou = tmpd + '/' + num + '_' + lyric + '_' + note + '.wav'
    resamp(bt2,rou,rin,note,vel,debug)
    #合成
    wavtool(bt1,output,rou,stp,length,tempo,p1,debug)

def zucs(t1,t2,out,ust,oto,tmp,debug = 'no') :
    if debug == 'yes' :
        print('调试信息：')
        print('wavtool：', t1)
        print('resamper：',t2)
        print('UST：', ust)
        print('音源：', oto)
        print('输出文件：',out)
        print('临时文件：',tmp)
    print('正在转码。。。')
    cproject = easyust.cproject(ust,tmp + '/temp.ini')
    if debug == 'yes': print('easyust工程：',cproject[1])
    allnote = easyust.rallnote(cproject[1])
    notenum = easyust.rnallnote(cproject[1])
    for x in allnote:
        print(str(allnote.index(x)+1),'/',notenum)
        note = easyust.rnote(ust,x)
        if debug == 'yes': print('音符数据：',note)
        if note[2] == 'R': wavtool(t1,out,oto + "/R.wav",'0',note[0],note[1],'0 0',debug)
        else : synth(t1,t2,out,oto,tmp,'0',note[0],note[1],'10 139 35 101 101 101 0 0 0',note[4],note[3],x,note[2],debug)

if len(sys.argv) == 1:
    print ('用法：python3 zuc.py <ust> [singer] [output]')
else:
    #ust
    ust = os.path.abspath(sys.argv[1])
    #配置文件
    cfg = os.path.dirname(os.path.abspath(__file__)) + '/cfg.ini'
    #读取配置文件
    conf = configparser.ConfigParser()
    conf.read(cfg)
    #音源
    if len(sys.argv) == 3:
        singer = os.path.abspath(sys.argv[2])
    else:
        singer = os.path.abspath(conf.get('zuc','oto'))
    #工具1（wavtool）
    tool1 = os.path.abspath(conf.get('zuc','tool'))
    #工具2（resamper）
    tool2 = os.path.abspath(conf.get('zuc','resamp'))
    #缓存
    cache = os.path.abspath(conf.get('zuc','cachedir'))
    #输出
    if len(sys.argv) == 4:
        out = os.path.abspath(sys.argv[3])
    else:
        out = os.path.abspath(conf.get('zuc','output'))
    #显示系统信息
    print('系统信息：')
    print('配置文件：',cfg)
    print('输入UST：',ust)
    print('音源路径：',singer)
    print('工具1（wavtool）：',tool1)
    print('工具2（resamper）：',tool2)
    print('缓存：',cache)
    print('输出：',out)
    zucs(tool1,tool2,out,ust,singer,cache)