# -*- coding:utf-8 -*-
import numpy as np
from math import pi
import matplotlib.pyplot as plt


waveform_x=5                            # 波形图中选择显示多少个周期
sample_multiple=20                      # 采样频率/待采样信号频率
N=4096                                  # 采样点

Ac=1                                    # 载波振幅
Fc=922375*1000                          # 载波频率
Wc=2*Fc*pi                              # 载波角频率

As=1                                    # 信号振幅
As_dc=0                                 # 信号直流分量
Fs=250*1000                             # 信号频率
Ws=2*Fs*pi                              # 信号角频率

# 载波信号
f_sample=Fc*sample_multiple             # 采样频率
n=np.array([i for i in range(N)])
t=n/f_sample                            # 时域序列
f=n*(f_sample/N)                        # 频域序列

Uc=Ac*np.cos(Wc*t)                      
C1=np.fft.fft(Uc)       
cxf=np.abs(C1)                     
plt.figure(1) 
plt.subplot(2,1,1) 
print(len(t),len(Uc))
plt.plot(t,Uc,marker='.') 
plt.title(u'Carrier signal waveform') 
plt.axis([0, waveform_x/Fc, -Ac, Ac])
plt.subplot(2,1,2)
plt.plot(f[1:int(N/2)],cxf[1:int(N/2)])
plt.title(u'Carrier signal spectrum')
# plt.show() 
# exit()

# 调制信号
f_sample=Fs*sample_multiple             # 采样频率
n=np.array([i for i in range(N)])
t=n/f_sample                            # 时域序列
f=n*(f_sample/N)                        # 频域序列

mes=As_dc+As*np.cos(Ws*t)                     
C2=np.fft.fft(mes)                    
zxc=np.abs(C2)        
plt.figure(2)
plt.subplot(2,1,1) 
plt.plot(t,mes,marker='.')
plt.title('Modulating signal waveform')
plt.axis([0, waveform_x/Fs, -As+As_dc, As+As_dc])
plt.subplot(2,1,2)  
plt.plot(f[1:int(N/2)],zxc[1:int(N/2)]) 
plt.title('Modulating signal spectrum')
# plt.show() 
# exit()

# AM 已调信号
f_sample=Fc*sample_multiple             # 采样频率
N=int(f_sample/Fs*waveform_x)
n=np.array([i for i in range(N)])
t=n/f_sample                            # 时域序列
f=n*(f_sample/N)                        # 频域序列

Uam=(As_dc+As*np.cos(Ws*t))*(Ac*np.cos(Wc*t))
C3=np.fft.fft(Uam)                             
asd=np.abs(C3)
plt.figure(3)
plt.subplot(2,1,1)
plt.plot(t,Uam,marker='.') 
plt.grid()
plt.title('AM modulated signal waveform')
plt.axis([0, waveform_x/Fs, -2, 2])
plt.subplot(2,1,2)
plt.plot(f[1:int(N/2)],asd[1:int(N/2)])
plt.grid()
plt.title('AM modulated signal spectrum')
# plt.show()
# exit()

# AM 解调信号
f_sample=Fc*sample_multiple             # 采样频率
N=int(f_sample/Fs*waveform_x)
n=np.array([i for i in range(N)])
t=n/f_sample                            # 时域序列
f=n*(f_sample/N)                        # 频域序列
         
Dam=(As_dc+As*np.cos(Ws*t))*(Ac*np.cos(Wc*t))*(Ac*np.cos(Wc*t))
C4=np.fft.fft(Dam)                               
wqe=np.abs(C4)
plt.figure(4)
plt.subplot(2,1,1) 
plt.plot(t,Dam,marker='.') 
plt.grid()
plt.title('AM demodulation signal waveform')
plt.axis([0, waveform_x/Fs, -2, 2])
plt.subplot(2,1,2)
plt.plot(f[1:int(N/2)],wqe[1:int(N/2)])
plt.grid()
plt.title('AM demodulation signal spectrum')

plt.show()

