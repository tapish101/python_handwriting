
                #'^' defines writing on left of the margin
                         #'^~' means new page


id='tapish'    #name of folder that contains data folders

#for more randomness
tilt=False



from PIL import Image
import random



#no. of pixels from left and right respectively on page from where words starts to paste
pageW=267  
pageH=249
#max height before automatically jumping to new page
Hmax=2000
#no. of pixels as space for writing on left margin like Que or Ans
fromleft=130
#the space b/w each characters
charspacing=2  
#height and width to write the page number
Pwidth=1430
Pheight=2055
#pixel diff b/w consecutive lines
lineWidth=56
#no of folsers to choose from
nof=5
#max writable pixel length on a line
lof=1720





leftmargin=False  #true when '^' is passes to textTOimg()
pageNo=1     #sarting page no.

#opens the blank ruled A4 paper image
image=Image.open('source/image.jpeg')

width=pageW 
height=pageH
margin=fromleft+random.randint(0,13)

char_map={'^': '^', ' ': 'space', '&': 'and', '*': 'astric', ',': 'comma', '$': 'dollar', '"': 'dquote', '!': 'exclam', '/': 'f_slash', '#': 'hash', '-': 'minus', '%': 'percent', '+': 'plus', "'": 'quote', '_': 'uscore', '(': 'sbracket_l', ')': 'sbracket_r', '.': 'stop', '`': 'ajeeb', '@': 'at', '[': 'bbracket_l', ']': 'bbracket_r', ':': 'colon', '{': 'curly_l', '}': 'curly_r', '|': 'danda', '=': 'equal', '>': 'greaterthan', '<': 'lessthan', '?': 'que', ';': 'semicolon', '~': 'slant', '\\t': 'tab'}


#responsible to write on left to margin
def writeonleft(t):
    global leftmargin,margin
    if t=="space":
        leftmargin=False
        margin=fromleft
    elif t=='slant':
        leftmargin=False
        margin=fromleft
        newpage()
    else:
        rand=random.randint(0,nof-1)
        img=Image.open('source/'+id+'/data'+str(rand)+'/'+t+'.png')
        if tilt:
            size=list(img.size)
            scl=random.uniform(-0.1,0.1)
            size[0]=round(size[0]+size[0]*scl)
            size[1]=round(size[1]+size[1]*scl)
            ang=random.uniform(-10,10)
            img=img.rotate(ang)
            if size[0]!=0 and size[1]!=0:
                img=img.resize(size)
            
        image.paste(img,(margin,height),img)
        margin=margin+img.size[0]


#calls pagenum() and then saves the written image in output folder
#and if end is false (i.e the saved page not last page) opens the black page again to write
def newpage(end=False):
    global image,height,width,pageNo
    pagenum(pageNo)
    image.save('output/page'+str(pageNo)+'.jpeg')
    if end:
        print('Completed...\nCheck Output folder for Images.')
    else:
        image=Image.open('source/image.jpeg')
        #set default staring point
        width=pageW
        height=pageH
        pageNo=pageNo+1
    


#moves the cursor to next line and it lines are ended calls newpage()
def nextline():
    global height,width
    height=height+lineWidth
    width=pageW
    if(height>Hmax):
        newpage()

#write page number to page 
def pagenum(x):
    wid=Pwidth

    for y in str(x):
        #randomly select each character from diff data folder
        rand=random.randint(0,nof-1)
        img=Image.open('source/'+id+'/data'+str(rand)+'/'+y+'.png')
        image.paste(img,(wid,Pheight),img)
        wid=wid+img.size[0]+charspacing

        
        

# takes the whole text at ones and iterate over it to pass each char to paste on background page image
def txtTOimg(txt):
    global width,leftmargin
    for i in txt:

        if i.isnumeric():
            i=str(i)
        elif i=="\n":
            i='enter'
        elif not i.isalpha():
            i=char_map[i]


        if i=='^':
            leftmargin=True
            continue
        elif i=='space':
            if(width>1700-267-50):
                nextline()
                continue
        elif i=='enter':
            nextline()
            continue
        


        if(leftmargin):
            writeonleft(i)
        else:
            rand=random.randint(0,4)
            try:
                img=Image.open('source/'+id+'/data'+str(rand)+'/'+i+'.png')
            except Exception:
                img=Image.open('source/'+id+'/data'+str(rand)+'/space.png')
                print("char not found,",i)
            if tilt:
                size=list(img.size)
                scl=random.uniform(-0.1,0.1)
                size[0]=round(size[0]+size[0]*scl)
                size[1]=round(size[1]+size[1]*scl)
                ang=random.uniform(-10,10)
                img=img.rotate(ang)
                if size[0]!=0 and size[1]!=0:
                    img=img.resize(size)
            image.paste(img,(width,height),img)
            width=width+img.size[0]+charspacing
        

try:
    #open the text file and pass whole text to text variable
    file=open('input.txt')
    text=file.read()
except FileNotFoundError:
    print("input.txt file not found.\nCreated the file\nInput text in input.txt file.")
    with open('input.txt', 'w') as f:
        f.write('Write text into this file.')
except Exception:
    print('Something went wrong with program.')
finally:
    txtTOimg(text)
    #saves the latest open page img and program ends here
    newpage(end=True)
