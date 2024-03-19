# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 17:13:00 2021

@authors: cesar fernandez ramirez & alessandro pilloni
"""

#%%

##############################################################################   
#
#   Libraries
#
##############################################################################   

import numpy as np
import matplotlib.pyplot as plt

###########################################################
#   JPAC color style
###########################################################

jpac_blue   = "#1F77B4"; jpac_red    = "#D61D28";
jpac_green  = "#2CA02C"; jpac_orange = "#FF7F0E";
jpac_purple = "#9467BD"; jpac_brown  = "#8C564B";
jpac_pink   = "#E377C2"; jpac_gold   = "#BCBD22";
jpac_aqua   = "#17BECF"; jpac_grey   = "#7F7F7F";

jpac_color = [jpac_blue, jpac_red, jpac_green, 
              jpac_orange, jpac_purple, jpac_brown,
              jpac_pink, jpac_gold, jpac_aqua, jpac_grey, 'black' ];

jpac_axes = jpac_color[10]

##############################################################################   
#
#   Functions
#
##############################################################################   

def plotstate(i,j,x,y,deltax,deltay,color,ancho,tamano_letra,line_style,nombre):
    subfig[i,j].hlines(y,x-deltax,x+deltax,colors=color, lw=ancho, linestyles=line_style)
    subfig[i,j].text(x-deltax,y+deltay,nombre,fontsize=tamano_letra)
    return

##############################################################################   
#
#   States
#
##############################################################################   

##############################################################################   
#   Nonexotic charmonia before 2003
##############################################################################   

charmonia_pre2003_spin_noexo = [1, 1, 2, 3, 3, 3, 3, 3, 5, 6, 3, 8 ]
charmonia_pre2003_mass_noexo = [2983.9,  3637.5,  3414.71, 3096.9, 
                                3686.10, 3773.7,  4039.,   4191.,
                                3525.38, 3510.67, 4421.,   3556.17 ]
charmonia_pre2003_names_noexo = [ r'$\eta_{c}$',   r'$\eta_{c}(2S)$',
                                  r'$\chi_{c0}$',  r'$J/\psi$',
                                  r'$\psi(2S)$',   r'$\psi(3770)$',
                                  r'$\psi(4040)$', r'$\psi(4160)$',
                                  r'$h_c$',        r'$\chi_{c1}$',
                                  r'$\psi(4415)$', r'$\chi_{c2}$']

##############################################################################   
#   Nonexotic charmonia after 2003
##############################################################################   

charmonia_post2003_spin_noexo = [2, 7, 8 ]
charmonia_post2003_mass_noexo = [3862., 3824, 3922.5]
charmonia_post2003_names_noexo = [r'$\chi_{c0}(3860)$',r'$\psi_2(3823)$',r'$\chi_{c2}(3930)$']

##############################################################################   
#   Exotic charmonia after 2003
##############################################################################   

charmonia_post2003_spin_exo = [6, 6,6,2,3, 3, 3, 2, 3, 2]
charmonia_post2003_mass_exo = [3871.65,4146.8,4274,4704.,4368.,4630.,4220.,3922,4390, 4506. ]
charmonia_post2003_names_exo = [r'$X(3872)$',r'$X(4140)$',r'$\chi_{c1}(4274)$',
                                r'$\chi_{c0}(4700)$',r'$\psi(4360)$',r'$\psi(4660)$',
                                r'$Y(4230)$',r'$X(3915)$',r'$Y(4390)$',r'$\chi_{c0}(4500)$']

##############################################################################   
#   Tcc
##############################################################################   

tcc_spin = [0]
tcc_mass = [3870.01]
tcc_names = [r'$T_{cc}$']

##############################################################################   
#   Di-J/psi
##############################################################################   

dijpsi_spin = [0]
dijpsi_mass = [6900]
dijpsi_names = [r'$X(6900)$']

##############################################################################   
#   Z
##############################################################################   

zc_spin  = [10, 11, 11, 11, 11, 9, 9]
zc_mass  = [4239., 3887.1,4196., 4478., 4020., 4051, 4248]
zc_names = [r'$R_{c0}(4240)$',r'$T_{c\bar{c}1}(3900)$',r'$T_{c\bar{c}1}(4200)$',r'$T_{c\bar{c}1}(4430)$',r'$T_{c\bar{c}1}(4020)$',
            r'$T_{c\bar{c}1}(4050)$',r'$T_{c\bar{c}1}(4250)$']

##############################################################################   
#   Zcs
##############################################################################   

zcs_spin  = [12, 12,12]
zcs_mass  = [4220.,4003.,3985]
zcs_names = [r'$Z_{cs}(4220)$',r'$Z_{cs}(4000)$',r'$Z_{cs}(3985)$']

##############################################################################   
#   Pentaquarks
##############################################################################   

pc_spin  = [13, 13, 13, 13]
pc_mass  = [4312., 4380,4440., 4457.]
pc_names = [r'$P_{c\bar{c}}(4312)$',r'$P_{c\bar{c}}(4380)$',r'$P_{c\bar{c}}(4440)$',r'$P_{c\bar{c}}(4457)$']


#%%

##############################################################################   
#
#    [Figure 0] Spectra review
#
##############################################################################   

##############################################################################   
#   Preparing axes and figure
##############################################################################   

espines = ['$?^{??}$','$0^{-+}$','$0^{++}$','$1^{--}$','$1^{-+}$',
           '$1^{+-}$','$1^{++}$','$2^{--}$','$2^{++}$',
           '$?^{??}$','$0^{--}$','$1^{+-}$','$Z_{cs}$',r'$P_{c\bar{c}}$']
espines_num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
xlim_dw, xlim_up = -1.5, 16.5

fig, subfig = plt.subplots(2,2,figsize=(15,10))

deltax = 0.35; deltay = 30; label_size = 18; tamano_letra = 13;
for i in np.arange(2):
    for j in np.arange(2):
        subfig[i,j].axis('off')

left, width = 0.15, 0.8; bottom, height = 0.2, 0.7;
rect_histy = [left, bottom, width, height]
subfig[0,0] = plt.axes(rect_histy)
subfig[0,0].spines['top'].set_visible(False)
subfig[0,0].spines['right'].set_visible(False)
subfig[0,0].set_xlim((xlim_dw, xlim_up))
subfig[0,0].set_ylim((2900.,4900.))
subfig[0,0].text(-2.3,4940,r'MeV',color='k',fontsize=label_size+2)
subfig[0,0].set_xticks(espines_num)
subfig[0,0].set_xticklabels(espines,fontsize=label_size)
subfig[0,0].tick_params(direction='in', top=False, right=False,left=True,size=5,labelleft=True,labelbottom=True,labelsize=label_size)

##############################################################################   
#   Thresholds
##############################################################################   

thr_start, thr_stop = -1.5, 12.5
subfig[0,0].hlines(1865.*2,thr_start,thr_stop,colors=jpac_color[9], lw=1., linestyles='dashed',zorder=0)
subfig[0,0].hlines(1865.+2007.,thr_start,thr_stop,colors=jpac_color[9], lw=1., linestyles='dashed',zorder=0)
subfig[0,0].hlines(1865.+2422.1,thr_start,thr_stop,colors=jpac_color[9], lw=1., linestyles='dashed',zorder=0)
subfig[0,0].hlines(2007.+2007.,thr_start,thr_stop,colors=jpac_color[9], lw=1., linestyles='dashed',zorder=0)
#subfig[0,0].hlines(3097.+139.,thr_start,thr_stop,colors=jpac_color[9], lw=1., linestyles='dashed',zorder=0)

x_pos_name, name_shift = -1.2, 20;
subfig[0,0].text(x_pos_name,1865.*2+name_shift,r'$DD$',color=jpac_color[9],fontsize=tamano_letra)
subfig[0,0].text(x_pos_name,1865.+2007.+name_shift,r'$DD^*$',color=jpac_color[9],fontsize=tamano_letra)
subfig[0,0].text(x_pos_name,1865.+2422.1+name_shift,r'$DD_{1}$',color=jpac_color[9],fontsize=tamano_letra)
subfig[0,0].text(x_pos_name,2007.+2007.+name_shift,r'$D^*D^*$',color=jpac_color[9],fontsize=tamano_letra)

thr_start, thr_stop = 12.5, 16.5
subfig[0,0].hlines(2453.+1865.,thr_start,thr_stop,colors=jpac_color[9], lw=1., linestyles='dashed',zorder=0)
subfig[0,0].hlines(3097.+939.,thr_start,thr_stop,colors=jpac_color[9], lw=1., linestyles='dashed',zorder=0)
subfig[0,0].hlines(2453.+2007.,thr_start,thr_stop,colors=jpac_color[9], lw=1., linestyles='dashed',zorder=0)
subfig[0,0].hlines(2517.5+1865.,thr_start,thr_stop,colors=jpac_color[9], lw=1., linestyles='dashed',zorder=0)

x_pos_name, name_shift = 15.7, 20;
subfig[0,0].text(x_pos_name,3097.+939.+name_shift,r'$J/\psi p$',color=jpac_color[9],fontsize=tamano_letra)
subfig[0,0].text(x_pos_name,2453+1865-3.*name_shift,r'$\Sigma_c D$',color=jpac_color[9],fontsize=tamano_letra)
subfig[0,0].text(x_pos_name,2453.+2007.+name_shift,r'$\Sigma_c D^*$',color=jpac_color[9],fontsize=tamano_letra)
subfig[0,0].text(x_pos_name,2517.5+1865.+name_shift,r'$\Sigma^*_c D$',color=jpac_color[9],fontsize=tamano_letra)

##############################################################################   
#   Nonexotic charmonia before 2003
##############################################################################   

tamano = len(charmonia_pre2003_spin_noexo);
color = jpac_color[2]; ancho = 3.; 
for i in range(tamano):
    nombre = charmonia_pre2003_names_noexo[i]
    y = charmonia_pre2003_mass_noexo[i]
    x = charmonia_pre2003_spin_noexo[i]    
    if nombre ==r'$\psi(4160)$':
        plotstate(0,0,x,y,deltax,-60,color,ancho,tamano_letra,'solid',nombre) 
#        subfig[0,0].text(x,y-50,nombre,fontsize=tamano_letra)
    elif nombre ==r'$\psi(4040)$':          
        plotstate(0,0,x,y,deltax,-60,color,ancho,tamano_letra,'solid',nombre) 
    else:
        plotstate(0,0,x,y,deltax,deltay,color,ancho,tamano_letra,'solid',nombre)

##############################################################################   
#   Nonexotic charmonia after 2003
##############################################################################   

tamano = len(charmonia_post2003_spin_noexo);
color = jpac_color[2]; ancho = 3.; 
for i in range(tamano):
    nombre = charmonia_post2003_names_noexo[i]
    y = charmonia_post2003_mass_noexo[i]
    x = charmonia_post2003_spin_noexo[i]  
    if nombre==r'$\chi_{c0}(3860)$':
        plotstate(0,0,x,y,deltax,deltay,color,ancho,tamano_letra,'solid',' ')
        subfig[0,0].text(x-0.7,y-50.,nombre,fontsize=tamano_letra)        
    else:    
        plotstate(0,0,x,y,deltax,deltay,color,ancho,tamano_letra,'solid',nombre)
        
##############################################################################   
#   Exotic charmonia after 2003
##############################################################################   

tamano = len(charmonia_post2003_spin_exo);
color = jpac_color[3]; ancho = 3.; 
for i in range(tamano):
    nombre = charmonia_post2003_names_exo[i]
    y = charmonia_post2003_mass_exo[i]
    x = charmonia_post2003_spin_exo[i]
    if nombre==r'$\psi(4360)$':
        plotstate(0,0,x,y,deltax,-55.,color,ancho,tamano_letra,'solid',nombre)        
    elif nombre==r'$Y(4230)$':   
        plotstate(0,0,x,y,deltax,0.,color,ancho,tamano_letra,'solid',' ') 
        subfig[0,0].text(x+0.35,y-10,nombre,fontsize=tamano_letra)
    elif nombre==r'$Y(4390)$':   
        plotstate(0,0,x,y,deltax,0.,color,ancho,tamano_letra,'solid',' ') 
        subfig[0,0].text(x+0.35,y-10,nombre,fontsize=tamano_letra)
    else:
        plotstate(0,0,x,y,deltax,deltay,color,ancho,tamano_letra,'solid',nombre)
    
##############################################################################   
#   Tcc
##############################################################################   

tamano = len(tcc_spin);
color = jpac_color[10]; ancho = 3.5; 
for i in range(tamano):
    nombre = tcc_names[i]
    y = tcc_mass[i]
    x = tcc_spin[i]        
    plotstate(0,0,x,y,deltax,deltay,color,ancho,tamano_letra,'solid',nombre)

##############################################################################   
#   Di-J/psi
##############################################################################   

color = jpac_color[1]; ancho = 4.0; 
nombre = dijpsi_names[0]
y = dijpsi_mass[0]
x = dijpsi_spin[0]
plotstate(0,0,x,4890.,deltax,deltay,color,ancho,tamano_letra,'solid',' ')
subfig[0,0].text(x+deltax/2.,4820,nombre,fontsize=tamano_letra)
subfig[0,0].arrow(x,4790., 0.,100., width=0.05,color=color,
                  shape='full',length_includes_head=True,
                  head_width=0.2,head_length=50.,overhang=0.2)

##############################################################################   
#   Z
##############################################################################   

tamano = len(zc_spin);
color = jpac_color[3]; ancho = 3.; 
for i in range(tamano):
    nombre = zc_names[i]
    y = zc_mass[i]
    x = zc_spin[i]        
    if nombre==r'$T_{c\bar{c}1}(4200)$' or nombre==r'$T_{c\bar{c}1}(4250)$':
        plotstate(0,0,x,y,deltax,-60,color,ancho,tamano_letra,'solid',nombre) 
    else:
        plotstate(0,0,x,y,deltax,deltay,color,ancho,tamano_letra,'solid',nombre)

##############################################################################   
#   Zcs
##############################################################################   

tamano = len(zcs_spin);
color = jpac_color[4]; ancho = 3.; 
for i in range(tamano):
    nombre = zcs_names[i]
    y = zcs_mass[i]
    x = zcs_spin[i]
    if nombre ==r'$Z_{cs}(3985)$':
        plotstate(0,0,x,y,deltax,-50,color,ancho,tamano_letra,'solid',' ')  
        subfig[0,0].text(x+deltax+0.1,y-50,nombre,fontsize=tamano_letra)
    else:
        plotstate(0,0,x,y,deltax,-50,color,ancho,tamano_letra,'solid',' ') 
        subfig[0,0].text(x+deltax+0.1,y,nombre,fontsize=tamano_letra)

##############################################################################   
#   Pentaquarks
##############################################################################   

tamano = len(pc_spin);
color = jpac_color[0]; ancho = 3.; 
for i in range(tamano):
    nombre = pc_names[i]
    y = pc_mass[i]
    x = pc_spin[i]  
    if nombre ==r'$P_{c\bar{c}}(4457)$':
        plotstate(0,0,x,y,deltax,50,color,ancho,tamano_letra,'solid',nombre)   
    else:
        plotstate(0,0,x,y,deltax,-50,color,ancho,tamano_letra,'solid',' ') 
        subfig[0,0].text(x+deltax+0.1,y-20,nombre,fontsize=tamano_letra)
   
##############################################################################   
#   legend
##############################################################################   

subfig[0,0].scatter(6.,3250., s=30,marker='s', facecolors=jpac_color[2], edgecolors=jpac_color[2], linewidths=2., zorder=2, label=r'$c\bar{c}$')
subfig[0,0].scatter(6.,3250., s=30,marker='s', facecolors=jpac_color[3], edgecolors=jpac_color[3], linewidths=2., zorder=2, label=r'$c\bar{c}q\bar{q}$')
subfig[0,0].scatter(6.,3250., s=30,marker='s', facecolors=jpac_color[4], edgecolors=jpac_color[4],linewidths=2., zorder=2, label=r'$c\bar{c}q\bar{s}$')
subfig[0,0].scatter(6.,3250., s=30,marker='s', facecolors=jpac_color[10],edgecolors=jpac_color[10],linewidths=2., zorder=2, label=r'$cc\bar{q}\bar{q}$')
subfig[0,0].scatter(6.,3250., s=30,marker='s', facecolors=jpac_color[1], edgecolors=jpac_color[1], linewidths=2., zorder=2, label=r'$cc\bar{c}\bar{c}$')
subfig[0,0].scatter(6.,3250., s=30,marker='s', facecolors=jpac_color[0], edgecolors=jpac_color[0], linewidths=2., zorder=2, label=r'$c\bar{c}qqq$')
handles, labels = plt.gca().get_legend_handles_labels()
order = [0, 1, 2, 3, 4, 5]
subfig[0,0].legend([handles[idx] for idx in order],[labels[idx] for idx in order],loc='upper right',ncol=6,frameon=True,fontsize=tamano_letra)
subfig[0,0].scatter(6.,3250.,s=100,marker='s',facecolors='white',edgecolors='white',linewidths=0.,zorder=3)

##############################################################################   
#   lower x axis
##############################################################################  
 
left, width = 0.15, 0.8; bottom, height = 0.1, 0.05;
rect_histy = [left, bottom, width, height]
subfig[1,1] = plt.axes(rect_histy)
subfig[1,1].spines['top'].set_visible(False)
subfig[1,1].spines['right'].set_visible(False)
subfig[1,1].spines['left'].set_visible(False)
subfig[1,1].spines['bottom'].set_visible(False)
subfig[1,1].tick_params(direction='in', top=False, right=False,left=False,size=0.,labelleft=False,labelbottom=False,labelsize=label_size)
subfig[1,1].set_xlim((xlim_dw, xlim_up))
subfig[1,1].set_ylim((0.,1.))

subfig[1,1].text(3.5,0.25,r'$I=0$',fontsize=label_size)
subfig[1,1].hlines( 0.8,-0.4, 8.4, colors=jpac_color[10], lw=1., linestyles='solid')
subfig[1,1].vlines(-0.4, 0.8, 1.0, colors=jpac_color[10], lw=1., linestyles='solid')
subfig[1,1].vlines( 8.4, 0.8, 1.0, colors=jpac_color[10], lw=1., linestyles='solid')

subfig[1,1].text(9.75,0.25,r'$I=1$',fontsize=label_size)
subfig[1,1].hlines( 0.8, 8.6, 11.4, colors=jpac_color[10], lw=1., linestyles='solid')
subfig[1,1].vlines( 8.6, 0.8,  1.0, colors=jpac_color[10], lw=1., linestyles='solid')
subfig[1,1].vlines(11.4, 0.8,  1.0, colors=jpac_color[10], lw=1., linestyles='solid')

subfig[1,1].text(12.15,0.25,r'$I=1/2$',fontsize=label_size)
subfig[1,1].hlines( 0.8, 11.6, 13.6, colors=jpac_color[10], lw=1., linestyles='solid')
subfig[1,1].vlines(11.6,  0.8,  1.0, colors=jpac_color[10], lw=1., linestyles='solid')
subfig[1,1].vlines(13.6,  0.8,  1.0, colors=jpac_color[10], lw=1., linestyles='solid')

##############################################################################   
#   JPAC logo
##############################################################################   

left, width = 0.82, 0.12; bottom, height = 0.21, 0.12;
rect_histy = [left, bottom, width, height]
subfig[0,1] = plt.axes(rect_histy)
subfig[0,1].axis('off')
file_jpac_logo = "JPAClogo.png"
jpac_logo = plt.imread(file_jpac_logo)
subfig[0,1].imshow(jpac_logo)

##############################################################################   
#   show & save
##############################################################################   

plt.show()    
fig.savefig("exotics_review.pdf", bbox_inches='tight')
fig.savefig("exotics_review.png", bbox_inches='tight')

#%%

##############################################################################   
#
#    [Figure 1] Spectra TC
#
##############################################################################   

##############################################################################   
#   Preparing axes and figure
##############################################################################   

espines = ['$?^{??}$','$0^{-+}$','$0^{++}$','$1^{--}$','$1^{-+}$',
           '$1^{+-}$','$1^{++}$','$2^{--}$','$2^{++}$',
           '$?^{??}$','$0^{--}$','$1^{+-}$','$Z_{cs}$']
espines_num = [0,1,2,3,4,5,6,7,8,9,10,11,12]

fig, subfig = plt.subplots(2,2,figsize=(15,10))

deltax = 0.35; deltay = 30; label_size = 18; tamano_letra = 13;
for i in np.arange(2):
    for j in np.arange(2):
        subfig[i,j].axis('off')

left, width = 0.15, 0.8; bottom, height = 0.2, 0.7;
rect_histy = [left, bottom, width, height]
subfig[0,0] = plt.axes(rect_histy)
subfig[0,0].spines['top'].set_visible(False)
subfig[0,0].spines['right'].set_visible(False)
subfig[0,0].set_xlim((-1.5,14.5))
subfig[0,0].set_ylim((2900.,4900.))
subfig[0,0].text(-2.,4950,r'MeV',color='k',fontsize=label_size)
subfig[0,0].set_xticks(espines_num)
subfig[0,0].set_xticklabels(espines,fontsize=label_size)
subfig[0,0].tick_params(direction='in', top=False, right=False,left=True,size=5,labelleft=True,labelbottom=True,labelsize=label_size)

##############################################################################   
#   Thresholds
##############################################################################   

thr_start, thr_stop = -1.5, 13.5
subfig[0,0].hlines(1865.*2,thr_start,thr_stop,colors=jpac_color[9], lw=1., linestyles='dashed',zorder=0)
subfig[0,0].hlines(1865.+2007.,thr_start,thr_stop,colors=jpac_color[9], lw=1., linestyles='dashed',zorder=0)
subfig[0,0].hlines(1865.+2422.1,thr_start,thr_stop,colors=jpac_color[9], lw=1., linestyles='dashed',zorder=0)
subfig[0,0].hlines(2007.+2007.,thr_start,thr_stop,colors=jpac_color[9], lw=1., linestyles='dashed',zorder=0)

x_pos_name, name_shift = -1.2, 10;
subfig[0,0].text(x_pos_name,1865.*2+name_shift,r'$DD$',color=jpac_color[9],fontsize=tamano_letra)
subfig[0,0].text(x_pos_name,1865.+2007.+name_shift,r'$DD^*$',color=jpac_color[9],fontsize=tamano_letra)
subfig[0,0].text(x_pos_name,1865.+2422.1+name_shift,r'$DD_{1}$',color=jpac_color[9],fontsize=tamano_letra)
subfig[0,0].text(x_pos_name,2007.+2007.+name_shift,r'$D^*D^*$',color=jpac_color[9],fontsize=tamano_letra)

##############################################################################   
#   Nonexotic charmonia before 2003
##############################################################################   

tamano = len(charmonia_pre2003_spin_noexo);
color = jpac_color[2]; ancho = 3.; 
for i in range(tamano):
    nombre = charmonia_pre2003_names_noexo[i]
    y = charmonia_pre2003_mass_noexo[i]
    x = charmonia_pre2003_spin_noexo[i]    
    if nombre ==r'$\psi(4160)$':
        plotstate(0,0,x,y,deltax,-60,color,ancho,tamano_letra,'solid',nombre) 
#        subfig[0,0].text(x,y-50,nombre,fontsize=tamano_letra)
    elif nombre ==r'$\psi(4040)$':          
        plotstate(0,0,x,y,deltax,-60,color,ancho,tamano_letra,'solid',nombre) 
    else:
        plotstate(0,0,x,y,deltax,deltay,color,ancho,tamano_letra,'solid',nombre)

##############################################################################   
#   Nonexotic charmonia after 2003
##############################################################################   

tamano = len(charmonia_post2003_spin_noexo);
color = jpac_color[2]; ancho = 3.; 
for i in range(tamano):
    nombre = charmonia_post2003_names_noexo[i]
    y = charmonia_post2003_mass_noexo[i]
    x = charmonia_post2003_spin_noexo[i]  
    if nombre==r'$\chi_{c0}(3860)$':
        plotstate(0,0,x,y,deltax,deltay,color,ancho,tamano_letra,'solid',' ')
        subfig[0,0].text(x-0.7,y-50.,nombre,fontsize=tamano_letra)        
    else:    
        plotstate(0,0,x,y,deltax,deltay,color,ancho,tamano_letra,'solid',nombre)
        
##############################################################################   
#   Exotic charmonia after 2003
##############################################################################   

tamano = len(charmonia_post2003_spin_exo);
color = jpac_color[3]; ancho = 3.; 
for i in range(tamano):
    nombre = charmonia_post2003_names_exo[i]
    y = charmonia_post2003_mass_exo[i]
    x = charmonia_post2003_spin_exo[i]
    if nombre==r'$\psi(4360)$':
        plotstate(0,0,x,y,deltax,-55.,color,ancho,tamano_letra,'solid',nombre)        
    elif nombre==r'$Y(4230)$':   
        plotstate(0,0,x,y,deltax,0.,color,ancho,tamano_letra,'solid',' ') 
        subfig[0,0].text(x+0.35,y-10,nombre,fontsize=tamano_letra)
    elif nombre==r'$Y(4390)$':   
        plotstate(0,0,x,y,deltax,0.,color,ancho,tamano_letra,'solid',' ') 
        subfig[0,0].text(x+0.35,y-10,nombre,fontsize=tamano_letra)
    else:
        plotstate(0,0,x,y,deltax,deltay,color,ancho,tamano_letra,'solid',nombre)
    
##############################################################################   
#   Tcc
##############################################################################   

tamano = len(tcc_spin);
color = jpac_color[10]; ancho = 3.5; 
for i in range(tamano):
    nombre = tcc_names[i]
    y = tcc_mass[i]
    x = tcc_spin[i]        
    plotstate(0,0,x,y,deltax,deltay,color,ancho,tamano_letra,'solid',nombre)

##############################################################################   
#   Di-J/psi
##############################################################################   

color = jpac_color[1]; ancho = 4.0; 
nombre = dijpsi_names[0]
y = dijpsi_mass[0]
x = dijpsi_spin[0]
plotstate(0,0,x,4890.,deltax,deltay,color,ancho,tamano_letra,'solid',' ')
subfig[0,0].text(x+deltax/2.,4820,nombre,fontsize=tamano_letra)
subfig[0,0].arrow(x,4790., 0.,100., width=0.05,color=color,
                  shape='full',length_includes_head=True,
                  head_width=0.2,head_length=50.,overhang=0.2)

##############################################################################   
#   Zc
##############################################################################   

tamano = len(zc_spin);
color = jpac_color[3]; ancho = 3.; 
for i in range(tamano):
    nombre = zc_names[i]
    y = zc_mass[i]
    x = zc_spin[i]        
    if nombre==r'$T_{c\bar{c}1}(4200)$' or nombre==r'$T_{c\bar{c}1}(4250)$':
        plotstate(0,0,x,y,deltax,-60,color,ancho,tamano_letra,'solid',nombre) 
    else:
        plotstate(0,0,x,y,deltax,deltay,color,ancho,tamano_letra,'solid',nombre)

##############################################################################   
#   Zcs
##############################################################################   

tamano = len(zcs_spin);
color = jpac_color[4]; ancho = 3.; 
for i in range(tamano):
    nombre = zcs_names[i]
    y = zcs_mass[i]
    x = zcs_spin[i]
    if nombre ==r'$Z_{cs}(3985)$':
        plotstate(0,0,x,y,deltax,-50,color,ancho,tamano_letra,'solid',' ')  
        subfig[0,0].text(x+deltax+0.1,y-50,nombre,fontsize=tamano_letra)
    else:
        plotstate(0,0,x,y,deltax,-50,color,ancho,tamano_letra,'solid',' ') 
        subfig[0,0].text(x+deltax+0.1,y,nombre,fontsize=tamano_letra)

##############################################################################   
#   legend
##############################################################################   

subfig[0,0].scatter(6.,3250., s=30,marker='s', facecolors=jpac_color[2], edgecolors=jpac_color[2], linewidths=2., zorder=2, label=r'$c\bar{c}$')
subfig[0,0].scatter(6.,3250., s=30,marker='s', facecolors=jpac_color[3], edgecolors=jpac_color[3], linewidths=2., zorder=2, label=r'$c\bar{c}q\bar{q}$')
subfig[0,0].scatter(6.,3250., s=30,marker='s', facecolors=jpac_color[4], edgecolors=jpac_color[4],linewidths=2., zorder=2, label=r'$c\bar{c}q\bar{s}$')
subfig[0,0].scatter(6.,3250., s=30,marker='s', facecolors=jpac_color[10],edgecolors=jpac_color[10],linewidths=2., zorder=2, label=r'$cc\bar{q}\bar{q}$')
subfig[0,0].scatter(6.,3250., s=30,marker='s', facecolors=jpac_color[1], edgecolors=jpac_color[1], linewidths=2., zorder=2, label=r'$cc\bar{c}\bar{c}$')
handles, labels = plt.gca().get_legend_handles_labels()
order = [0, 1, 2, 3, 4]
subfig[0,0].legend([handles[idx] for idx in order],[labels[idx] for idx in order],loc='upper right',ncol=6,frameon=True,fontsize=tamano_letra)
subfig[0,0].scatter(6.,3250.,s=100,marker='s',facecolors='white',edgecolors='white',linewidths=0.,zorder=3)

##############################################################################   
#   lower x axis
##############################################################################  
 
left, width = 0.15, 0.8; bottom, height = 0.1, 0.05;
rect_histy = [left, bottom, width, height]
subfig[1,1] = plt.axes(rect_histy)
subfig[1,1].spines['top'].set_visible(False)
subfig[1,1].spines['right'].set_visible(False)
subfig[1,1].spines['left'].set_visible(False)
subfig[1,1].spines['bottom'].set_visible(False)
subfig[1,1].tick_params(direction='in', top=False, right=False,left=False,size=0.,labelleft=False,labelbottom=False,labelsize=label_size)

subfig[1,1].set_xlim((-1.5,13.5))
subfig[1,1].set_ylim((0.,1.))

subfig[1,1].text(3.5,0.25,r'$I=0$',fontsize=label_size)
subfig[1,1].hlines( 0.8,-0.4, 7.7, colors=jpac_color[10], lw=1., linestyles='solid')
subfig[1,1].vlines(-0.4, 0.8, 1.0, colors=jpac_color[10], lw=1., linestyles='solid')
subfig[1,1].vlines( 7.7, 0.8, 1.0, colors=jpac_color[10], lw=1., linestyles='solid')

subfig[1,1].text(8.75,0.25,r'$I=1$',fontsize=label_size)
subfig[1,1].hlines( 0.8, 7.8, 10.5, colors=jpac_color[10], lw=1., linestyles='solid')
subfig[1,1].vlines( 7.8, 0.8,  1.0, colors=jpac_color[10], lw=1., linestyles='solid')
subfig[1,1].vlines(10.5, 0.8,  1.0, colors=jpac_color[10], lw=1., linestyles='solid')

##############################################################################   
#   JPAC logo
##############################################################################   

left, width = 0.82, 0.12; bottom, height = 0.21, 0.12;
rect_histy = [left, bottom, width, height]
subfig[0,1] = plt.axes(rect_histy)
subfig[0,1].axis('off')
file_jpac_logo = "JPAClogo.png"
jpac_logo = plt.imread(file_jpac_logo)
subfig[0,1].imshow(jpac_logo)

##############################################################################   
#   show & save
##############################################################################   

plt.show()    
fig.savefig("exotics_tc.pdf", bbox_inches='tight')
fig.savefig("exotics_tc.png", bbox_inches='tight')

#%%

###########################################################
#
#    [Figure 2] Spectra pre 2003
#
###########################################################

##############################################################################   
#   Preparing axes and figure
##############################################################################   

espines = ['$0^{-+}$','$0^{++}$','$1^{--}$','$1^{-+}$',
           '$1^{+-}$','$1^{++}$','$2^{--}$','$2^{++}$']
espines_num = [1,2,3,4,5,6,7,8]

fig, subfig = plt.subplots(2,2,figsize=(15,10))

deltax = 0.35; deltay = 30; label_size = 18; tamano_letra = 13;
for i in np.arange(2):
    for j in np.arange(2):
        subfig[i,j].axis('off')

left, width = 0.15, 0.8; bottom, height = 0.2, 0.7;
rect_histy = [left, bottom, width, height]
subfig[0,0] = plt.axes(rect_histy)
subfig[0,0].spines['top'].set_visible(False)
subfig[0,0].spines['right'].set_visible(False)
subfig[0,0].set_xlim((-1.5,14.5))
subfig[0,0].set_ylim((2900.,4900.))
subfig[0,0].text(-2.,4950,r'MeV',color='k',fontsize=label_size)
subfig[0,0].set_xticks(espines_num)
subfig[0,0].set_xticklabels(espines,fontsize=label_size)
subfig[0,0].tick_params(direction='in', top=False, right=False,left=True,size=5,labelleft=True,labelbottom=True,labelsize=label_size)

##############################################################################   
#   Thresholds
##############################################################################   

thr_start, thr_stop = -1.5, 13.5
subfig[0,0].hlines(1865.*2,thr_start,thr_stop,colors=jpac_color[9], lw=1., linestyles='dashed',zorder=0)
subfig[0,0].hlines(1865.+2007.,thr_start,thr_stop,colors=jpac_color[9], lw=1., linestyles='dashed',zorder=0)
subfig[0,0].hlines(1865.+2422.1,thr_start,thr_stop,colors=jpac_color[9], lw=1., linestyles='dashed',zorder=0)
subfig[0,0].hlines(2007.+2007.,thr_start,thr_stop,colors=jpac_color[9], lw=1., linestyles='dashed',zorder=0)

x_pos_name, name_shift = -1.2, 10;
subfig[0,0].text(x_pos_name,1865.*2+name_shift,r'$DD$',color=jpac_color[9],fontsize=tamano_letra)
subfig[0,0].text(x_pos_name,1865.+2007.+name_shift,r'$DD^*$',color=jpac_color[9],fontsize=tamano_letra)
subfig[0,0].text(x_pos_name,1865.+2422.1+name_shift,r'$DD_{1}$',color=jpac_color[9],fontsize=tamano_letra)
subfig[0,0].text(x_pos_name,2007.+2007.+name_shift,r'$D^*D^*$',color=jpac_color[9],fontsize=tamano_letra)

##############################################################################   
#   Nonexotic charmonia before 2003
##############################################################################   

tamano = len(charmonia_pre2003_spin_noexo);
color = jpac_color[2]; ancho = 3.; 
for i in range(tamano):
    nombre = charmonia_pre2003_names_noexo[i]
    y = charmonia_pre2003_mass_noexo[i]
    x = charmonia_pre2003_spin_noexo[i]    
    if nombre ==r'$\psi(4160)$':
        plotstate(0,0,x,y,deltax,-60,color,ancho,tamano_letra,'solid',nombre) 
#        subfig[0,0].text(x,y-50,nombre,fontsize=tamano_letra)
    elif nombre ==r'$\psi(4040)$':          
        plotstate(0,0,x,y,deltax,-60,color,ancho,tamano_letra,'solid',nombre) 
    else:
        plotstate(0,0,x,y,deltax,deltay,color,ancho,tamano_letra,'solid',nombre)

##############################################################################   
#   legend
##############################################################################   

subfig[0,0].scatter(6.,3250., s=30,marker='s', facecolors=jpac_color[2], edgecolors=jpac_color[2], linewidths=2., zorder=2, label=r'$c\bar{c}$')
handles, labels = plt.gca().get_legend_handles_labels()
order = [0 ]
subfig[0,0].legend([handles[idx] for idx in order],[labels[idx] for idx in order],loc='upper left',ncol=6,frameon=True,fontsize=tamano_letra)
subfig[0,0].scatter(6.,3250.,s=100,marker='s',facecolors='white',edgecolors='white',linewidths=0.,zorder=3)

##############################################################################   
#   lower x axis
##############################################################################  
 
left, width = 0.15, 0.8; bottom, height = 0.1, 0.05;
rect_histy = [left, bottom, width, height]
subfig[1,1] = plt.axes(rect_histy)
subfig[1,1].spines['top'].set_visible(False)
subfig[1,1].spines['right'].set_visible(False)
subfig[1,1].spines['left'].set_visible(False)
subfig[1,1].spines['bottom'].set_visible(False)
subfig[1,1].tick_params(direction='in', top=False, right=False,left=False,size=0.,labelleft=False,labelbottom=False,labelsize=label_size)

subfig[1,1].set_xlim((-1.5,13.5))
subfig[1,1].set_ylim((0.,1.))

subfig[1,1].text(3.5,0.25,r'$I=0$',fontsize=label_size)
subfig[1,1].hlines( 0.8,-0.4, 7.7, colors=jpac_color[10], lw=1., linestyles='solid')
subfig[1,1].vlines(-0.4, 0.8, 1.0, colors=jpac_color[10], lw=1., linestyles='solid')
subfig[1,1].vlines( 7.7, 0.8, 1.0, colors=jpac_color[10], lw=1., linestyles='solid')

##############################################################################   
#   JPAC logo
##############################################################################   

left, width = 0.82, 0.12; bottom, height = 0.21, 0.12;
rect_histy = [left, bottom, width, height]
subfig[0,1] = plt.axes(rect_histy)
subfig[0,1].axis('off')
file_jpac_logo = "JPAClogo.png"
jpac_logo = plt.imread(file_jpac_logo)
subfig[0,1].imshow(jpac_logo)

##############################################################################   
#   show & save
##############################################################################   

plt.show()    
fig.savefig("charmonia_pre2003.pdf", bbox_inches='tight')
fig.savefig("charmonia_pre2003.png", bbox_inches='tight')



