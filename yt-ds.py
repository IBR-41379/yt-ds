import os
import json
def is_tool(name):
    """Check whether `name` is on PATH and marked as executable."""
    # from whichcraft import which
    from shutil import which
    return which(name) is not None

def dependency():
    x=is_tool("youtube-dl")
    z=os.popen('pip3 list | grep youtube-search-python')
    w=z.readlines()
    if x==False:
        m=input("youtubedl is missing from your system. Do you want to intsall it(y/n)")
        if m == "y":
            os.system("pip3 install youtube-dl")
        else:
            print("Ok, closing program")
            exit() 
    else:
        pass

    if len(w)==0:
        m=input("youtube-search-python is missing from your system. Do you want to intsall it(y/n)")
        if m == "y":
            os.system("pip3 install youtube-search-python")
        else:
            print("Ok, closing program")
            exit() 
    else:
        pass

def intro():
    print("yt-ds\n(A script to make youtubedl simple)\nVersion: 0.25(beta)\n")


intro()
dependency()


import youtubesearchpython
from youtubesearchpython import VideosSearch
from youtubesearchpython import *


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
        i=h.replace('          ',',')
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



def resolution(m):
    z=getvidinfo(m)
    y=getsizeinfo(m)
    n=getformatinfo(m)
    s=getfpsinfo(m)
    t=getresinfo(m)
    u=getextenstioninfo(m)
    print('Available resolutions are:')
    for d in z:
        if d=='160':
            if d in y:
                c=z.index('160')
                print(c,' :  144p  ,',n.get(d),'     ,',s.get(d),'  ,',u.get(d),'  ,',y.get(d))
            else:
                c=z.index('160')
                print(c,' :   144p  ,avc1.4d400c@  84k    ,30fps  ,mp4')
        else:
            pass

        if d=='278':
            if d in y:
                c=z.index('278')
                print(c,' :  144p  ,',n.get(d),'             ,',s.get(d),'  ,',u.get(d),' ,',y.get(d))
            else:
                c=z.index('278')
                print(c,' : 144p  ,vp9@  85k            ,30fps  ,webm')
            
        else:
            pass

        if d=='394':
            if d in y:
                c=z.index('394')
                print(c,' :  144p  ,',n.get(d),'   ,',s.get(d),'  ,',u.get(d),'  ,',y.get(d))
            else:
                c=z.index('394')
                print(c,' : 144p  ,av01.0.00M.08@  97k  ,30fps  ,mp4')
        else:
            pass

        if d=='330':
            if d in y:
                c=z.index(d)
                print(c,' :144p HDR ,',n.get(d),'          ,',s.get(d),'  ,',u.get(d),'  ,',y.get(d))
            else:
                c=z.index(d)
                print(c,' : 144p  ,av01.0.00M.08@  97k  ,30fps  ,mp4')
        else:
            pass


        if d=='242':
            if d in y:
                c=z.index('242')
                print(c,' : ',t.get(d),'  ,',n.get(d),'            ,',s.get(d),'  ,',u.get(d),' ,',y.get(d))
            else:
                c=z.index('242')
                print(c,' : 240p  ,vp9@ 183k            ,30fps  ,webm')
        else:
            pass

        if d=='133':
            if d in y:
                c=z.index('133')
                print(c,' : ',t.get(d),'  ,',n.get(d),'    ,',s.get(d),'  ,',u.get(d),'  ,',y.get(d))
            else:    
                c=z.index('133')
                print(c,' : 240p  ,avc1.4d4015@ 103k    ,30fps  ,mp4')
        else:
            pass


        if d=='395':
            if d in y:
                c=z.index('395')
                print(c,' : ',t.get(d),'  ,',n.get(d),'  ,',s.get(d),'  ,',u.get(d),'  ,',y.get(d))
            else:
                c=z.index('395')
                print(c,' : 240p  ,av01.0.00M.08@ 226k  ,30fps  ,mp4')
        else:
            pass

        if d=='331':
            if d in y:
                c=z.index(d)
                print(c,' :240p HDR ,',n.get(d),'          ,',s.get(d),'  ,',u.get(d),' ,',y.get(d))
            else:
                c=z.index(d)
                print(c,' : 240p  ,av01.0.00M.08@ 226k  ,30fps  ,mp4')
        else:
            pass

        if d=='243':
            if d in y:
                c=z.index('243')
                print(c,' : ',t.get(d),'  ,',n.get(d),'            ,',s.get(d),'  ,',u.get(d),' ,',y.get(d))
            else:
                c=z.index('243')
                print(c,' : 360p  ,vp9@ 401k            ,30fps  ,webm')
        else:
            pass
    
        if d=='396':
            c=z.index('396')
            print(c,' : ',t.get(d),'  ,',n.get(d),'  ,',s.get(d),'  ,',u.get(d),'  ,',y.get(d))
        else:
            pass

        if d=='134':
            c=z.index('134')
            print(c,' : ',t.get(d),'  ,',n.get(d),'    ,',s.get(d),'  ,',u.get(d),'  ,',y.get(d))
        else:
            pass

        if d=='332':
            c=z.index(d)
            print(c,' :360p HDR ,',n.get(d),'          ,',s.get(d),'  ,',u.get(d),' ,',y.get(d))
        else:
            pass

        if d=='244':
            c=z.index('244')
            print(c,' : ',t.get(d),'  ,',n.get(d),'            ,',s.get(d),'  ,',u.get(d),' ,',y.get(d))
        else:
            pass

        if d=='397':
            c=z.index('397')
            print(c,': ',t.get(d),'  ,',n.get(d),'  ,',s.get(d),'  ,',u.get(d),'  ,',y.get(d))
        else:
            pass

        if d=='135':
            c=z.index('135')
            print(c,': ',t.get(d),'  ,',n.get(d),'    ,',s.get(d),'  ,',u.get(d),'  ,',y.get(d))
        else:
            pass

        if d=='333':
            c=z.index(d)
            print(c,':480p HDR ,',n.get(d),'          ,',s.get(d),'  ,',u.get(d),' ,',y.get(d))
        else:
            pass
        
        if d=='247':
            c=z.index('247')
            print(c,': ',t.get(d),'  ,',n.get(d),'            ,',s.get(d),'  ,',u.get(d),' ,',y.get(d))
        else:  
            pass

        if d=='136':
            c=z.index('136')
            print(c,': ',t.get(d),'  ,',n.get(d),'    ,',s.get(d),'  ,',u.get(d),'  ,',y.get(d))
        else:
            pass

        if d=='334':
            c=z.index(d)
            print(c,':720p HDR ,',n.get(d),'          ,',s.get(d),'  ,',u.get(d),' ,',y.get(d))
        else:  
            pass

        if d=='398':
            c=z.index('398')
            print(c,': ',t.get(d),' ,',n.get(d),'  ,',s.get(d),'  ,',u.get(d),'  ,',y.get(d))
        else:
            pass

        if d=='302':
            c=z.index('302')
            print(c,': ',t.get(d),' ,',n.get(d),'            ,',s.get(d),'  ,',u.get(d),' ,',y.get(d))
        else:
            pass

        if d=='298':
            c=z.index('298')
            print(c,': ',t.get(d),' ,',n.get(d),'    ,',s.get(d),'  ,',u.get(d),'  ,',y.get(d))
        else:
            pass


        if d=='399':
            c=z.index('399')
            print(c,': ',t.get(d),',',n.get(d),'  ,',s.get(d),'  ,',u.get(d),'  ,',y.get(d))

        if d=='137':
            c=z.index(d)
            print(c,': ',t.get(d),' ,',n.get(d),'    ,',s.get(d),'  ,',u.get(d),'  ,',y.get(d))
        else:
            pass

        if d=='335':
            c=z.index(d)
            print(c,':1080p HDR,',n.get(d),'          ,',s.get(d),'  ,',u.get(d),' ,',y.get(d))
        else:
            pass

        if d=='248':
            c=z.index(d)
            print(c,': ',t.get(d),' ,',n.get(d),'            ,',s.get(d),'  ,',u.get(d),' ,',y.get(d))
        else:
            pass

        if d=='303':
            c=z.index('303')
            print(c,': ',t.get(d),',',n.get(d),'            ,',s.get(d),'  ,',u.get(d),' ,',y.get(d))
        else:
            pass

        if d=='299':
            c=z.index('299')
            print(c,': ',t.get(d),',',n.get(d),'    ,',s.get(d),'  ,',u.get(d),'  ,',y.get(d))
        else:
            pass

        if d=='271':
            c=z.index(d)
            print(c,': ',t.get(d),' ,',n.get(d),'            ,',s.get(d),'  ,',u.get(d),' ,',y.get(d))
        else:
            pass

        if d=='336':
            c=z.index(d)
            print(c,':1440p HDR,',n.get(d),'         ,',s.get(d),'  ,',u.get(d),' ,',y.get(d))
        else:
            pass


        if d=='400':
            c=z.index('400')
            print(c,': ',t.get(d),',',n.get(d),' ,',s.get(d),'  ,',u.get(d),'  ,',y.get(d))
        else:
            pass

        if d=='308':
            c=z.index('308')
            print(c,': ',t.get(d),',',n.get(d),'           ,',s.get(d),'  ,',u.get(d),' ,',y.get(d))
        else:
            pass

        if d=='313':
            c=z.index(d)
            print(c,': ',t.get(d),' ,',n.get(d),'           ,',s.get(d),'  ,',u.get(d),' ,',y.get(d))
        else:
            pass


        if d=='337':
            c=z.index(d)
            print(c,': 2160p HDR,',n.get(d),'        ,',s.get(d),'  ,',u.get(d),' ,',y.get(d))
        else:
            pass

        if d=='401':
            c=z.index('401')
            print(c,': ',t.get(d),',',n.get(d),' ,',s.get(d),'  ,',u.get(d),'  ,',y.get(d))
        else:
            pass

        if d=='315':
            c=z.index('315')
            print(c,': ',t.get(d),',',n.get(d),'           ,',s.get(d),'  ,',u.get(d),' ,',y.get(d))
        else:
            pass

        if d=='272':
            c=z.index(d)
            print(c,': ',t.get(d),' ,',n.get(d),'          ,',s.get(d),'  ,',u.get(d),' ,',y.get(d))
        else:
            pass

        if d=='402':
            c=z.index(d)
            print(c,': ',t.get(d),' ,',n.get(d),'   ,',s.get(d),'  ,',u.get(d),'  ,',y.get(d))
        else:
            pass

        if d=='571':
            c=z.index(d)
            print(c,': ',t.get(d),' ,',n.get(d),'   ,',s.get(d),'  ,',u.get(d),'  ,',y.get(d))
        else:
            pass



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


def audio(m):
    z=getaudinfo(m)
    y=getaudsizeinfo(m)
    n=getaudformatinfo(m)
    print('Choose audio format:')
    
    if '249' in z:
        c=z.index('249')
        print(c,': ',n.get('249'),'        , webm,',y.get('249'))
    else:
        pass

    if '250' in z:
        c=z.index('250')
        print(c,': ',n.get('250'),'        , webm,',y.get('250'))
    else:
        pass

    if '140' in z:
        c=z.index('140')
        print(c,': ',n.get('140'),'    , m4a ,',y.get('140'))
    else:
        pass

    if '251' in z:
        c=z.index('251')
        print(c,': ',n.get('251'),'        , webm,',y.get('251'))
    else:
        pass

def vidcode(m):
    a=int(input("Enter the number to choose resolution :"))
    z=getvidinfo(m)
    c=z[a]
    return c

def audcode(m):
    a=int(input("Enter the number to choose audio fotmat :"))
    z=getaudinfo(m)
    c=z[a]
    return c

def downloader(a,b,c):
    e=input("Enter download path :")
    videoInfo = Video.getInfo(c, mode = ResultMode.json)
    x=videoInfo
    z=x.replace('\n','')
    y=z.replace('    ','')
    res = json.loads(y)
    j=res['channel']
    k=j['name']
    print('Do you to make a new folder with the name of the youtube channel download video in that folder(y/n)')
    op=input('(Default==n):')
    if op=='y':
        try:
            while True:
                os.chdir(e+'/'+k)
                os.system('youtube-dl -f '+a+'+'+b+' '+c)
                print('Press any button to exit')
                input()
                exit()
        except FileNotFoundError:
            os.chdir(e)
            os.mkdir(k)
            os.chdir(e+'/'+k)
            os.system('youtube-dl -f '+a+'+'+b+' '+c)
            print('Press any button to exit')
            input()
            exit()
    else:
        os.chdir(e)
        os.system('youtube-dl -f '+a+'+'+b+' '+c)
        print('Press any button to exit')
        input()
        exit()

        

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
    print()
    resolution(l)
    q=vidcode(l)
    print()
    audio(l)
    r=audcode(l)
    print()
    downloader(q,r,l)
    #print('Press any button to exit')
    #input()
    #exit()

def searchdownload():
    l=searchyoutube()
    print()
    resolution(l)
    q=vidcode(l)
    print()
    audio(l)
    r=audcode(l)
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







    
    

    
