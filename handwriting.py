                         #32 rows in one page

                         #for input.txt file
                #'^' defines writing on left of the margin
                         #'^~' means new page


id='tapish'    #name of folder that contains data folders
               #diff name to use diff hand writing 



from PIL import Image
import random

#these variable are to be changes accordingly

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

                  #till here



leftmargin=False  #true when '^' is passes to textTOimg()
pageNo=1     #sarting page no.

#opens the blank ruled A4 paper image
image=Image.open('source/image.jpeg')

width=pageW 
height=pageH
margin=fromleft+random.randint(0,13)
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



def write(txt):
    global width,leftmargin,insertImg
    for i in txt:
        if i=='^':
            leftmargin=True
        elif(width>lof-pageW) and i==' ':
            nextline()
        elif i=='\n':
            nextline()
        elif i=='<':
            insertImg=True
        else:
            if insertImg:
                insert(i)
            else:
                if i.isalpha():
                    txtTOimg(str(i))
                else:
                    txtTOimg(i)



# takes the whole text at ones and iterate over it to pass each char to paste on background page image
def txtTOimg(txt):
    global width,leftmargin
    for i in txt:

        if i=='^':
            leftmargin=True
            continue
        elif i==' ':
            i='space'
            if(width>1700-267-50):
                nextline()
                continue
        elif i=='\n':
            nextline()
            continue
        elif i=='&':
            i='and'
        elif i=='*':
            i='astric'
        elif i==',':
            i='comma'
        elif i=='$':
            i='dollar'
        elif i=='"':
            i='dquote'
        elif i=='!':
            i='exclam'
        elif i=='/':
            i='f_slash'
        elif i=='#':
            i='hash'
        elif i=='-':
            i='minus'
        elif i=='%':
            i='percent'
        elif i=='+':
            i='plus'
        elif i=="'":
            i='quote'
        elif i=='_':
            i='uscore'
        elif i=='(':
            i='sbracket_l'
        elif i==')':
            i='sbracket_r'
        elif i=='.':
            i='stop'
        elif i.isalpha():
            i=str(i)
        elif i=='`':
            i='ajeeb' 
        elif i=='@':
            i='at'
        elif i=='[':
            i='bbracket_l'
        elif i==']':
            i='bbracket_r'
        elif i==":":
            i='colon'
        elif i=='{':
            i='curly_l'
        elif i=='}':
            i='curly_r'
        elif i=='|':
            i='danda'
        elif i=='=':
            i='equal'
        elif i=='>':
            i='greaterthan'
        elif i=='<':
            i='lessthan'
        elif i=='?':
            i='que'
        elif i==';':
            i='semicolon'
        elif i=="~":
            i='slant'
        elif i=='\t':
            i='tab'
        

        if(leftmargin):
            writeonleft(i)
        else:
            rand=random.randint(0,4)
            img=Image.open('source/'+id+'/data'+str(rand)+'/'+i+'.png')
            image.paste(img,(width,height),img)
            width=width+img.size[0]+charspacing
        

#open the text file and pass whole text to text variable
file=open('input.txt')
text=file.read()

txtTOimg(text)

#saves the latest open page img and program ends here
newpage(end=True)
