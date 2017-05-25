import urllib
import calendar
import os

T_start = raw_input("enter starting year and month (separated by a comma):").split(',')
T_stop  = raw_input("enter ending year and month (separated by a comma):").split(',')
print 'time range %s to %s' % (T_start, T_stop)

fid = open('merra_data_api.dat','r')
filelist = fid.readlines()
urlhd    = filelist[0][0:-1]   #                                            'http://goldsmr3.sci.gsfc.nasa.gov/daac-bin/OTF/HTTP_services.cgi?' 
name     = filelist[1][0:-1]   #                                            'FILENAME=%2Fdata%2Fs4pa%2FMERRA%2FMAI3CPASM.5.2.0%2Fxxxx%2Fxx%2FMERRA300.prod.assim.inst3_3d_asm_Cp.xxxxxxxx.hdf&'
format   = filelist[2][0:-1]   # lat lon region default: -90~90. -180~180 , 'FORMAT=SERGLw&BBOX=-90%2C-180%2C90%2C180&'
label    = filelist[3][0:-1]   # changes according to the file name,        'MERRAxxx.prod.assim.inst3_3d_asm_Cp.xxxxxxxx.SUB.hdf&'
flag     = filelist[4][0:-1]   #                                            '1&SHORTNAME=MAI3CPASM&SERVICE=SUBSET_LATS4D&'
layer    = filelist[5][0:-1]   # default = 37 layers [1000:-25:700:-50:100:70:50:-10:10 7 5 4 3 2 1] hPa, ''LAYERS=LAYER_1000%2C975%2C...2%2C1'
version  = filelist[6][0:-1]   #                                            'VERSION=1.02'
variables= filelist[7][0:-1]   #                                            'ps%2Cqv%2Ct'  

for year in range(int(T_start[0]), int(T_stop[0])):
    if year > 2001:
        label0  = label[0:11]+'300'+label[14:]
    elif year > 1992:
        label0  = label[0:11]+'200'+label[14:]
    else:
        label0  = label[0:11]+'100'+label[14:]

    for month in range(1,13):
        if (year==2010) & (month>5) & (month<11):
            label0  = label[6:11]+'301'+label[14:]
            
        n_day = calendar.monthrange(year,month)[1] # total number of days in month
        for day in range(1,n_day+1):
            digit = str(10000*year+100*month+day)
            label_= label0.replace('xxxxxxxx',digit)
            name_ = name[0:52]+str(year)+name[56:59]+str(month).rjust(2,'0')+name[61:64]+label_[6:-9]+name[-5:]
            url = urlhd+name_+format+label_+flag+layer+version+variables
            file = label_[6:-1]
            if(not(os.path.exists(file))):
                print "downloading " + file + "..."
                urllib.urlretrieve(url, file)

year = int(T_stop[0])
if year > 2001:
   label0  = label[0:11]+'300'+label[14:]
elif year > 1992:
   label0  = label[0:11]+'200'+label[14:]
else:
   label0  = label[0:11]+'100'+label[14:]

m0=1
if(int(T_stop[0])==int(T_start[0])):
    m0 = int(T_start[1])
    print m0, int(T_stop[1])
   
for month in range(m0,int(T_stop[1])+1):
    if (year==2010) & (month>5) & (month<11):
        label0  = label[6:11]+'301'+label[14:]
            
    n_day = calendar.monthrange(year,month)[1] # total number of days in month
    for day in range(1,n_day+1):
        digit = str(10000*year+100*month+day)
        label_= label0.replace('xxxxxxxx',digit)
        name_ = name[0:52]+str(year)+name[56:59]+str(month).rjust(2,'0')+name[61:64]+label_[6:-9]+name[-5:]
        url = urlhd+name_+format+label_+flag+layer+version+variables
	print url
        file = label_[6:-1]
        if(not(os.path.exists(file))):
            print "downloading " + file + "..."
            urllib.urlretrieve(url, file)

