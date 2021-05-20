import os
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

dependency()


import youtubesearchpython
from youtubesearchpython import Search

def intro():
    print("yt-ds\n(A script to make youtubedl simple)\nVersion: 0.1(alpha)\n")

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



def resolution(m):
    z=getvidinfo(m)
    print('Available resolutions are:')
    for d in z:
        if d=='160':
            c=z.index('160')
            print(c,' : 144p  ,avc1.4d400c@  84k    ,30fps  ,mp4')
        else:
            pass

        if d=='278':
            c=z.index('278')
            print(c,' : 144p  ,vp9@  85k            ,30fps  ,webm')
            
        else:
            pass

        if d=='394':
            c=z.index('394')
            print(c,' : 144p  ,av01.0.00M.08@  97k  ,30fps  ,mp4')
        else:
            pass

        if d=='242':
            c=z.index('242')
            print(c,' : 240p  ,vp9@ 183k            ,30fps  ,webm')
        else:
            pass

        if d=='133':
            c=z.index('133')
            print(c,' : 240p  ,avc1.4d4015@ 207k    ,30fps  ,mp4')
        else:
            pass


        if d=='395':
            c=z.index('395')
            print(c,' : 240p  ,av01.0.00M.08@ 226k  ,30fps  ,mp4')
        else:
            pass

        if d=='243':
            c=z.index('243')
            print(c,' : 360p  ,vp9@ 401k            ,30fps  ,webm')
        else:
            pass
    
        if d=='396':
            c=z.index('396')
            print(c,' : 360p  ,av01.0.01M.08@ 414k  ,30fps  ,mp4')
        else:
            pass

        if d=='134':
            c=z.index('134')
            print(c,' : 360p  ,avc1.4d401e@ 484k    ,30fps  ,mp4')
        else:
            pass

        if d=='244':
            c=z.index('244')
            print(c,' : 480p  ,vp9@ 739k            ,30fps  ,webm')
        else:
            pass

        if d=='397':
            c=z.index('397')
            print(c,': 480p  ,av01.0.04M.08@ 765k  ,30fps  ,mp4')
        else:
            pass

        if d=='135':
            c=z.index('135')
            print(c,': 480p  ,avc1.4d401f@ 846k    ,30fps  ,mp4')
        else:
            pass
        if d=='247':
            c=z.index('247')
            print(c,': 720p  ,vp9@1512k            ,30fps  ,webm')
        else:  
            pass

        if d=='136':
            c=z.index('136')
            print(c,': 720p  ,avc1.4d401f@2212k    ,30fps  ,mp4')
        else:
            pass

        if d=='398':
            c=z.index('398')
            print(c,': 720p  ,av01.0.08M.08@2549k  ,60fps  ,mp4')
        else:
            pass

        if d=='302':
            c=z.index('302')
            print(c,': 720p  ,vp9@2581k            ,60fps  ,webm')
        else:
            pass

        if d=='298':
            c=z.index('298')
            print(c,': 720p  ,avc1.4d4020@3376k    ,60fps  ,mp4')
        else:
            pass

        if d=='399':
            c=z.index('399')
            print(c,': 1080p ,av01.0.09M.08@3924k  ,60fps  ,mp4')
        else:
            pass

        if d=='303':
            c=z.index('303')
            print(c,': 1080p ,vp9@4420k            ,60fps  ,webm')
        else:
            pass

        if d=='299':
            c=z.index('299')
            print(c,': 1080p ,avc1.64002a@5662k    ,60fps  ,mp4')
        else:
            pass

        if d=='400':
            c=z.index('400')
            print(c,': 1440p ,av01.0.12M.08@11928k ,60fps  ,mp4')
        else:
            pass

        if d=='308':
            c=z.index('308')
            print(c,': 1440p ,vp9@12598k           ,60fps  ,webm')
        else:
            pass

        if d=='401':
            c=z.index('401')
            print(c,': 2160p ,av01.0.13M.08@19748k ,60fps  ,mp4')
        else:
            pass

        if d=='315':
            c=z.index('315')
            print(c,': 2160p ,vp9@25783k           ,60fps  ,webm')
        else:
            pass
def audio(m):
    z=getaudinfo(m)
    print('Choose audio format:')
    
    if '249' in z:
        c=z.index('249')
        print(c,': opus @ 57k (48000Hz), webm')
    else:
        pass

    if '250' in z:
        c=z.index('250')
        print(c,': opus @ 75k (48000Hz), webm')
    else:
        pass

    if '140' in z:
        c=z.index('140')
        print(c,': mp4a.40.2@129k (44100Hz), m4a')
    else:
        pass

    if '251' in z:
        c=z.index('251')
        print(c,': opus @145k (48000Hz) , webm')
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
    e=input("Enter download path")
    os.chdir(e)
    os.system('youtube-dl -f '+a+'+'+b+' '+c)

def link():
    a=input('Enter youtube link :')
    return a

def searchyoutube():
    a=input("Enter items to be searched :")
    b=int(input("Enter number of results you want to search :"))
    allSearch = Search(a, limit = b)
    x=allSearch.result()
    for r in x:
        l=x[r]
        for i in range(b):
            j=str(i)
            m=l[i]
            n=m['channel']
            p=n['name']
            o=m['title']
            print(j+')'+'channel name :'+p+'\n'+'Videoname :'+o+'\n'+'link :'+m['link'])
            print()
        s=int(input("Enter number :"))
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
    print('Press any button to exit')
    input()
    exit()

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
    print('Press any button to exit')
    input()
    exit()


intro()
dependency()
print()
print('1)Search for youtube video\n2)Paste youtube video link')
w=int(input('Enter the number :'))
while True:    
    if w==1:
        searchdownload()
    elif w==2:
        onlydownload()
    else:
        print("Wrong choice. Try again")
        continue



#l=link()
#print(getaudinfo(l))
#resolution()
#audio()







    
    

    
