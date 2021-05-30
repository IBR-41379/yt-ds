import os
import json
import glob
import os.path
#def is_tool(name):
    #"""Check whether `name` is on PATH and marked as executable."""
    ## from whichcraft import which
    #from shutil import which
   # return which(name) is not None

def size_format(b):
    if b < 1000:
              return '%i' % b + 'B'
    elif 1000 <= b < 1000000:
        return '%.1f' % float(b/1000) + 'KB'
    elif 1000000 <= b < 1000000000:
        return '%.1f' % float(b/1000000) + 'MB'
    elif 1000000000 <= b < 1000000000000:
        return '%.1f' % float(b/1000000000) + 'GB'
    elif 1000000000000 <= b:
        return '%.1f' % float(b/1000000000000) + 'TB'


def dependency():
    x=os.popen('pip3 list | grep youtube-dl')
    z=os.popen('pip3 list | grep youtube-search-python')
    xz=os.popen('pip3 list | grep langcodes')
    w=z.readlines()
    v=x.readlines()
    wv=xz.readlines()

    if len(v)==0:
        m=input("youtube-dl is missing from your system. Do you want to intsall it(y/n)")
        if m == "y":
            os.system("pip3 install --upgrade youtube-dl")
        else:
            print("Ok, closing program")
            exit() 
    else:
        pass
    

    if len(w)==0:
        m=input("youtube-search-python is missing from your system. Do you want to install it(y/n)")
        if m == "y":
            os.system("pip3 install --upgrade youtube-search-python")
        else:
            print("Ok, closing program")
            exit() 
    else:
        pass


    if len(wv)==0:
        m=input("langcodes is missing from your system. Do you want to intsall it(y/n)")
        if m == "y":
            os.system("pip3 install --upgrade langcodes")
            os.system("pip3 install --upgrade language_data")
        else:
            print("Ok, closing program")
            exit() 
    else:
        pass

def intro():
    print("yt-ds\n(A script to make youtubedl simple)\nVersion: 0.4(beta)\n")


intro()
dependency()


import youtubesearchpython
from youtubesearchpython import VideosSearch
from youtubesearchpython import *
from youtube_dl import YoutubeDL
from langcodes import *

def vidaudinfoV2(m):
    ydl = YoutubeDL()
    info = ydl.extract_info(m, download=False)
    return info


def getvidinfo(v):
    a=os.popen("youtube-dl -F"+' '+v)
    b=a.readlines()
    #print(b)
    f=[]
    p=len(b)
    for i in range(7,p-2):
        x=b[i]
        y=x[0:3]
        f.append(y)
    return f
        #print(z)

def getaudinfo(v):
    a=os.popen("youtube-dl -F"+' '+v)
    b=a.readlines()
    #print(b)
    f=[]
    #p=len(b)
    for i in range(3,8):
        x=b[i]
        y=x[0:3]
        f.append(y)
    return f
        #print(z)

def getsizeinfo(v):
    a=os.popen("youtube-dl -F"+' '+v)
    b=a.readlines()
    #print(b)
    h=[]
    dict={}
    p=len(b)
    for i in range(7,p-2):
        c=b[i]
        d=c.replace('\n','')
        e=d.split(',')
        f=len(e)
        g=e[f-1]
        k=e[0]
        key=k[0:3]
        #print(e)
        #print(key)
        dict[key]=g
    return dict

def getformatinfo(v):
    a=os.popen("youtube-dl -F"+' '+v)
    b=a.readlines()
    #print(b)
    h=[]
    dict={}
    p=len(b)
    for i in range(7,p-2):
        c=b[i]
        d=c.replace('\n','')
        e=d.split(',')
        f=len(e)
        g=e[f-4]
        k=e[0]
        key=k[0:3]
        #print(e)
        #print(key)
        dict[key]=g
    return dict

def getfpsinfo(v):
    a=os.popen("youtube-dl -F"+' '+v)
    b=a.readlines()
    #print(b)
    h=[]
    dict={}
    p=len(b)
    for i in range(7,p-2):
        c=b[i]
        d=c.replace('\n','')
        e=d.split(',')
        f=len(e)
        g=e[f-3]
        k=e[0]
        key=k[0:3]
        #print(e)
        #print(key)
        dict[key]=g
    return dict

def getresinfo(v):
    a=os.popen("youtube-dl -F"+' '+v)
    b=a.readlines()
    #print(b)
    #h=[]
    dict={}
    p=len(b)
    for i in range(7,p-2):
        c=b[i]
        d=c.replace('\n','')
        e=d.split(',')
        h=e[0]
        mo=h.replace('  ',' ')
        i=mo.replace('          ',',')
        j=i.replace('       ',',')
        m=j.replace('  ',',')
        n=m.replace(' ',',')
        t=n.split(',')
        f=len(t)
        g=t[f-3]
        key=t[0]
        #print(e)
        #print(key)
        dict[key]=g
    return dict

def getextenstioninfo(v):
    a=os.popen("youtube-dl -F"+' '+v)
    b=a.readlines()
    #print(b)
    #h=[]
    dict={}
    p=len(b)
    for i in range(7,p-2):
        c=b[i]
        d=c.replace('\n','')
        e=d.split(',')
        h=e[0]
        i=h.replace('          ',',')
        j=i.replace('       ',',')
        #m=j.replace('  ',',')
        #n=m.replace(' ',',')
        t=j.split(',')
        #f=len(t)
        g=t[1]
        key=t[0]
        #print(e)
        #print(key)
        dict[key]=g
    return dict

def getvideoname(m):
    videoInfo = Video.getInfo(m, mode = ResultMode.json)
    x=videoInfo
    zeb=x.replace('\n','')
    ya=zeb.replace('    ','')
    res = json.loads(ya)
    j=res['title']
    return j

def resolutionV2(m):
    lol=vidaudinfoV2(m)
    l=lol.get('formats')
    v=len(l)
    for i in range(4,v-2):
        m=l[i]
        ab=m.get('vcodec')+'@ '+str(m.get('vbr'))+'k'
        #print(ab)
        ba= "{:<28}".format(ab)
        bab="{:<3}".format(str(i-3))
        print(bab,':',m.get('format_note'),',',ba,',',m.get('fps'),'fps,',m.get('ext'),',',size_format(m.get('filesize')))
    print(v-5,': Back to main menu')



def getaudsizeinfo(v):
    a=os.popen("youtube-dl -F"+' '+v)
    b=a.readlines()
    #print(b)
    h=[]
    dict={}
    p=len(b)
    for i in range(3,8):
        c=b[i]
        d=c.replace('\n','')
        e=d.split(',')
        f=len(e)
        g=e[f-1]
        k=e[0]
        key=k[0:3]
        #print(e)
        #print(key)
        dict[key]=g
    return dict

def getaudformatinfo(v):
    a=os.popen("youtube-dl -F"+' '+v)
    b=a.readlines()
    #print(b)
    h=[]
    dict={}
    p=len(b)
    for i in range(3,8):
        c=b[i]
        d=c.replace('\n','')
        e=d.split(',')
        f=len(e)
        g=e[f-2]
        k=e[0]
        key=k[0:3]
        #print(e)
        #print(key)
        dict[key]=g
    return dict


def audioV2(m):
    lol=vidaudinfoV2(m)
    l=lol.get('formats')
    v=len(l)
    for i in range(4):
        m=l[i]
        ab=m.get('acodec')+'@ '+str(m.get('abr'))+'k'
        #print(ab)
        ba= "{:<28}".format(ab)
        bab="{:<3}".format(str(i+1))
        print(bab,':',ba,',',m.get('ext'),',',size_format(m.get('filesize')))
    print(5,': Back to Video Resolution')



def vidcodeV2(m):
    a=int(input("Enter the number to choose resolution or go back to previous page :"))
    lol=vidaudinfoV2(m)
    z=lol.get('formats')
    if a == len(z)-5:
        mainprogram()
    else:
        mo=z[a+3]
        c=mo.get('format_id')
    return c



def audcodeV2(m):
    a=int(input("Enter the number to choose audio fotmat or go back to previous page :"))
    lol=vidaudinfoV2(m)
    z=lol.get('formats')
    if a == 5:
        resolutionV2(m)
        q=vidcodeV2(m)
        print()
        audioV2(m)
        r=audcodeV2(m)
        print()
        downloader(q,r,m)
    else:
        mo=z[a-1]
        c=mo.get('format_id')
        return c


def timestampinfo(m):
    a=vidaudinfoV2(m)
    sayan=a.get('title')
    lab=m.split('/')
    laba=len(lab)
    lababa=lab[laba-1]
    f = open(sayan+'-'+lababa+'.info.json','r')
    data = json.loads(f.read())
    g=data.get('chapters')
    if g == None:
        #os.system('rm -r "'+sayan+'-'+lababa+'.en.vtt"')
        os.system('rm -r "'+sayan+'-'+lababa+'.info.json"')
        os.system('rm -r "'+sayan+'-'+lababa+'.srt"')
        print('Press y to go to main menu or any button to exit')
        inp=input(':')
        if inp == 'y':
            mainprogram()
        else:
            exit()
    else:
        x=open('metadata','a')
        y=';FFMETADATA1\ntitle='+sayan
        x.write(y)
        h=len(g)
        for i in range(h):
            j=g[i]
            #st_len=len(str(j['start_time']))
            start=str(j['start_time']*1000)
            #start=st_time[0:st_len]
            #en_len=len(str(j['end_time']))
            end=str(j['end_time']*1000)
            #end=en_time[0:en_len]
            title=j['title']
            z='\n\n[CHAPTER]\nTIMEBASE=1/1000\nSTART='+start+'\nEND='+end+'\ntitle='+title
            x.write(z)
        x.write('\n\n[STREAM]\ntitle='+sayan)
        #return z
        f.close()
        x.close()
        list_of_files =os.getcwd()+'/' 
        latest_file = sorted(os.listdir(list_of_files),key=lambda p: os.path.getctime(os.path.join(list_of_files, p)))
        t2 = "%s/%s" % (list_of_files, latest_file[-2])
        mon=t2.replace('/',',')
        nom=mon.split(',')
        lennom=len(nom)
        nomnom=nom[lennom-1]
        #os.system('ffmpeg -i "'+sayan+'-'+lababa+'.en.vtt"'+' "'+sayan+'-'+lababa+'.srt"')
        os.system('ffmpeg -i "'+nomnom+'" -i metadata -map_metadata 1 -codec copy "(Ch)'+nomnom+'"')
        os.system('ffmpeg -i "(Ch)'+nomnom+'" -i "'+sayan+'-'+lababa+'.srt" -c copy -c:s mov_text "(chsub)'+nomnom+'"')
        os.system('rm -r metadata')
        
        if os.path.isfile(os.getcwd()+'/'+'"'+sayan+'-'+lababa+'.srt"'):
            os.system('rm -r "(Ch)'+nomnom+'"')
        else:
            pass
        os.system('rm -r "'+nomnom+'"')
        #os.system('ffmpeg -i "'+sayan+'-'+lababa+'.en.vtt"'+' "'+sayan+'-'+lababa+'.ass"')
        #os.system('rm -r "'+sayan+'-'+lababa+'.en.vtt"')
        #os.system('rm -r "'+sayan+'-'+lababa+'.srt"')
        os.system('rm -r "'+sayan+'-'+lababa+'.srt"')
        os.system('rm -r "'+sayan+'-'+lababa+'.info.json"')
        print('Press y to go to main menu or any button to exit')
        inp=input(':')
        if inp == 'y':
            mainprogram()
        else:
            exit()

def presubinfo(m):
    ca=vidaudinfoV2(m)
    ma=ca.get('subtitles')
    return ma

def subtitleV2(m):
    ma = presubinfo(m)
    maaa=len(ma)
    if ma == None:
        pass
    
    elif maaa == 0:
        pass

    else:
        am=ma.keys()
        mam=list(am)
        popo=len(mam)
        for i in range(popo):
            lan=Language.make(language=mam[i]).display_name()
            #bhasa=lan.name
            sata="{:<2}".format(str(i+1))
            print(sata,':',lan)
            #print(lan)
        return mam

def getsubinfo(m):
    am=subtitleV2(m)
    m=int(input("Enter your choice:"))
    maa=m-1
    lolu=am[maa]
    return lolu


def downloader(a,b,c):
    luv=presubinfo(c)
    e=input("Enter download path :")
    if luv==None:
        po='n'
    else:
        print('Do you want do download subtitles(if onlu auto-sub is there,press n)(y/n)')
        po=input('(Default==n):')
    videoInfo = Video.getInfo(c, mode = ResultMode.json)
    x=videoInfo
    z=x.replace('\n','')
    y=z.replace('    ','')
    res = json.loads(y)
    suv=res['title']
    lab=c.split('/')
    laba=len(lab)
    lababa=lab[laba-1]
    j=res['channel']
    k=j['name']
    
    
    if po=='y':
        nihongo=getsubinfo(c)
        print('Do you to make a new folder with the name of the youtube channel download video in that folder(y/n)')
        op=input('(Default==n):')
        if op=='y':
            try:
                while True:
                    os.chdir(e+'/'+k)
                    os.system('youtube-dl --write-info-json --write-srt --sub-lang '+nihongo+' -f '+a+'+'+b+' '+c)
                   
        
            except FileNotFoundError:
                os.chdir(e)
                os.mkdir(k)
                os.chdir(e+'/'+k)
                os.system('youtube-dl --write-info-json --write-srt --sub-lang '+nihongo+' -f '+a+'+'+b+' '+c)
               
        else:
            os.chdir(e)
            os.system('youtube-dl --write-info-json --write-srt --sub-lang '+nihongo+' -f  '+a+'+'+b+' '+c)
        list_of_files =os.getcwd()+'/' 
        latest_file = sorted(os.listdir(list_of_files),key=lambda p: os.path.getctime(os.path.join(list_of_files, p)))
        t2 = "%s/%s" % (list_of_files, latest_file[-1])
        mon=t2.replace('/',',')
        nom=mon.split(',')
        lennom=len(nom)
        nomnom=nom[lennom-1]
        os.system('ffmpeg -i "'+suv+'-'+lababa+'.en.vtt"'+' "'+suv+'-'+lababa+'.srt"')
        os.system('ffmpeg -i "'+nomnom+'" -i "'+suv+'-'+lababa+'.srt" -c copy -c:s mov_text "(yt)'+nomnom+'"')
        os.system('rm -r "'+suv+'-'+lababa+'.en.vtt"')
        #os.system('rm -r "'+suv+'-'+lababa+'.srt"')
        os.system('rm -r "'+nomnom+'"')


    
    else:
        print('Do you to make a new folder with the name of the youtube channel download video in that folder(y/n)')
        op=input('(Default==n):')
        if op=='y':
            try:
                while True:
                    os.chdir(e+'/'+k)
                    os.system('youtube-dl --write-info-json -f '+a+'+'+b+' '+c)
                    
        
            except FileNotFoundError:
                os.chdir(e)
                os.mkdir(k)
                os.chdir(e+'/'+k)
                os.system('youtube-dl --write-info-json -f '+a+'+'+b+' '+c)
                
        else:
            os.chdir(e)
            os.system('youtube-dl --write-info-json -f '+a+'+'+b+' '+c)

        
    timestampinfo(c)
    #os.system('rm -r "'+suv+'-'+lababa+'.info.json"')
    #hum=os.getcwd()
    
           
       

def link():
    a=input('Enter youtube link :')
    return a

def searchyoutube():
    a=input("Enter items to be searched :")
    b=int(input("Enter number of results you want to search :"))
    videosSearch = VideosSearch(a, limit = b)
    x=videosSearch.result()
    for r in x:
        l=x[r]
        for i in range(b):
            j=str(i)
            m=l[i]
            n=m['channel']
            p=n['name']
            o=m['title']
            print()
            print(j+')'+'channel name :'+p+'\n'+'Videoname :'+o+'\n'+'link :'+m['link'])
        s=int(input("\nEnter number :"))
        t=l[s]
        u=t['link']
        return u

def onlydownload():
    l=link()
    resolutionV2(l)
    q=vidcodeV2(l)
    print()
    audioV2(l)
    r=audcodeV2(l)
    print()
    downloader(q,r,l)
    #print('Press any button to exit')
    #input()
    #exit()

def searchdownload():
    l=searchyoutube()
    print()
    resolutionV2(l)
    q=vidcodeV2(l)
    print()
    audioV2(l)
    r=audcodeV2(l)
    print()
    downloader(q,r,l)
    #print('Press any button to exit')
    #input()
    #exit()

def mainprogram():
    print()
    print('1)Search for youtube video\n2)Paste youtube video link\n3)Exit')
    f=input('Enter the number(Default==2) :')
    print()
    if len(f)==0:
        f='2'
    else:
        pass


    if int(f)==1:
        searchdownload()
    elif int(f)==2:
        onlydownload()
    elif int(f)==3:
        exit()
    else:
        print("Wrong choice. Try again")
        mainprogram()

mainprogram()

#l=link()
#print(getaudinfo(l))
#resolution()
#audio()







    
    

    
