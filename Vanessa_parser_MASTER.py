import os
import numpy as np
#import scipy
from collections import Counter


#create working directory on cluster. Change 'test_run' to desired name
folder_name='STACKS_denovo_SwPaAnKe'
print(folder_name)
os.system('mkdir ' + folder_name)
print('mkdir ' + folder_name)
os.system('cd ' + folder_name)
print('cd ' + folder_name)


#provide populations list as a pop_names=[list]
#available populations:
#'Chad': 152, 'Ethiopia': 134, 'Italy': 122, 'Benin': 106,
#'Spain': 98, 'South': 94, 'California': 80, 'Sichuan': 78, 
#'annabella': 68, 'Hawaii': 66, 'Namibia': 64, 'Senegal': 62, 
#'Gansu': 60, 'Kansas': 58, 'Algeria': 50, 'Israel': 50, 'Sonora': 50,
#'Greece': 46, 'Japan': 44, 'Morocco': 42, 'Chihuahua': 38, 'Turkey': 34,
#'Kenya': 34, 'Bulgaria': 32, 'Kazakhstan': 32, 'Tunisia': 32, 'Arizona': 32,
#'Java': 32, 'France': 30, 'Bali': 30, 'Romania': 28, 'Aguascalientes': 28, 
#'Poland': 26, 'Tadjikistan': 24, 'Serbia': 24, 'Qinghai': 24, 'COMMERCIAL': 24, 
#'Nuevo': 22, 'Baja': 22, 'Liaoning': 20, 'Andalusia': 20, 'Yunnan': 20, 'Zambia': 18,
#'Canarias': 18, 'Pakistan': 16, 'Texas': 16, 'Puebla': 16, 'Oklahoma': 16, 'Jalisco': 16,
#'Iran': 16, 'Arunachal': 16, 'Crete': 14, 'Sweden': 12, 'Oman': 12, 'Tanzania': 12, 
#'Wyoming': 12, 'Switzerland': 12, 'Kaliningrad': 12, 'Shanxi': 12, 'Dominican': 12, 
#'Malta': 10, 'Uzbekistan': 10, 'Tajikistan': 10, 'Portugal': 10, 'NY': 10, 'DF': 10, 
#'Austria': 8, 'Vietnam': 8, 'North': 8, 'Estonia': 6, 'Sicily': 6, 'Malawi': 6, 'Los': 6,
#'French': 6, 'Minnesota': 6, 'Khakassia': 6, 'Germany': 6, 'Albania': 6, 'Novosibirsk': 6, 
#'Western': 6, 'Illes': 4, 'Sardinia': 4, 'Bejaia': 4, 'India': 4, 'Bosnia': 4, 'Slovakia': 4, 
#'Tibet': 4, 'Azerbaijan': 4, 'United': 4, 'Oregon': 4, 'Nebraska': 4, 'Ontario': 4, 'Russia': 4, 
#'Egypt': 4, 'Hidalgo': 4, 'Virginia': 4, 'New': 4, 'Queenslad': 4, 'Cajamarca': 4, 'Merida': 4, 
#'Mali': 2, 'Annapurna': 2, 'Cuzco': 2, 'Trapani': 2, 'Akfadou': 2, 'Ukraine': 2, 'Martinique': 2, 
#'Tanzania?': 2, 'Belgium': 2, 'Queretaro': 2, 'Wisconsin': 2, 'Massachussets': 2, 'MA': 2, 'SD': 2, 
#'Finland': 2, 'Tenerife': 2, 'virginiensis': 2, 'Durango': 2, 'Cordoba': 2, 'Catamarca': 2, 'Okinawa': 2, 
#'Zhejiang': 2, 'Tlaxcala': 2, 'Czech': 2, 'Algeria?': 2, 'Sulawesi': 2, 'Meghalaya': 2, 'Canberra': 2, 'Vermont': 2

pop_names=['Sweden','Pakistan','Andalusia','Kenya']

#provide list of file names
txt = open("/proj/uppstore2017185/b2014034_nobackup/Dasha/RAD_Vanessa/2_STACKS_BWA/Vanessa_RAD_names_plain.txt").read()
split_file = txt.split('\n')

#create a list for selected file names
select_samples=[]

#select cardui (comment if not needed)
for i in split_file:
    line=i.split('_')
    if (line[1] == "cardui")|(line[1]=="Vcardui"):
#select individuals from chosen populations
        for j in pop_names:
            if line[2] == j:
                #print(i)
                select_samples+=[i]
print("Number of individuals selected:",len(select_samples))

#bonus: extend code to include selected number of individuals

#create popmap:
#Chad_14T188<tab>afr
#Chad_14T189<tab>afr

#select unique names (forward and reverse reads have the same sample name)
uni_set=set(select_samples)
#print(uni_set)

#create empty popmap file
mapfile = open(folder_name+"/tmppopmap", "w")

for i in uni_set:
    line=i.split('_')
    print(line[2]+"_"+line[0]+'\t'+line[2]) 
    mapfile.write(line[2]+"_"+line[0]+'\t'+line[2]+'\n')     
    
mapfile.close()
os.system('sort '+folder_name+'/tmppopmap'+'| uniq > '+folder_name+'/popmap')


#create folder for samples
os.system('mkdir '+folder_name+ '/samples')
print('mkdir '+folder_name+ '/samples')


#create soft links for files and rename them to STACKS convention:
    #Chad_14T189.1.fq.gz 
    #Chad_14T189.2.fq.gz

#for i in select_samples:
 #   print(i)
    #os.system('cd  '+folder_name+ '/samples')
    #print('cd '+folder_name+ '/samples')
    #os.system('cp /proj/uppstore2017185/b2014034/private/raw_data/Vanessa/Vcardui_RAD/RAD_DEMULTIPLEXED/'+i+' '+folder_name+ '/samples')
    #print('ln -s /proj/uppstore2017185/b2014034/private/raw_data/Vanessa/Vcardui_RAD/RAD_DEMULTIPLEXED/'+i+' '+folder_name+ '/samples')
  #  line=i.split('_')
   # if (line[5]=="R1")|(line[6]=="R1"):
    	#print("mv "+folder_name+ '/samples/'+i+" "+folder_name+ '/samples/'+line[2]+'_'+line[0]+'.1.fq.gz')
       # os.system('mv '+folder_name+ '/samples/'+i+' '+folder_name+ '/samples/'+line[2]+'_'+line[0]+'.1.fq.gz')
        
    #else:
	#print("mv "+folder_name+ '/samples/'+i+" "+folder_name+ '/samples/'+line[2]+'_'+line[0]+'.2.fq.gz')
        #print("mv "+i+" "+              line[2]+'_'+line[0]+'.2.fq.gz')
        #os.system('mv '+folder_name+ '/samples/'+i+' '+folder_name+ '/samples/'+line[2]+'_'+line[0]+'.2.fq.gz')

for i in select_samples:
#    print(i)
    os.system('cp /proj/uppstore2017185/b2014034/private/raw_data/Vanessa/Vcardui_RAD/RAD_DEMULTIPLEXED/'+i+' '+folder_name+ '/samples')
    line=i.split('_')
 #   print(len(line))
    flag = False
    if line[5]=="R1":
	flag=True
    elif len(line)>=7:
	if line[6]=="R1":
		#print(len(line))
		flag=True
    elif len(line)>=8:
        if line[7]=="R1":
                flag=True
    elif len(line)>=9:
        if line[8]=="R1":
                flag=True
    elif len(line)>=10:
        if line[9]=="R1":
                flag=True

    if (flag):
#	print('this is R1 read')
	#print("mv "+folder_name+ '/samples/'+i+" "+folder_name+ '/samples/'+line[2]+'_'+line[0]+'.1.fq.gz')
        os.system('mv '+folder_name+ '/samples/'+i+' '+folder_name+ '/samples/'+line[2]+'_'+line[0]+'.1.fq.gz')
    else:
	#print("mv "+folder_name+ '/samples/'+i+" "+folder_name+ '/samples/'+line[2]+'_'+line[0]+'.2.fq.gz')
        os.system('mv '+folder_name+ '/samples/'+i+' '+folder_name+ '/samples/'+line[2]+'_'+line[0]+'.2.fq.gz')
