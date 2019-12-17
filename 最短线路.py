from collections import deque
import sys
q=0
flag=True
while q<len(sys.argv):
    if sys.argv[q]=='-map':
        flag=False
    if sys.argv[q]=='-a':
        flag=False
    if sys.argv[q]=='-o':
        flag=False
    if sys.argv[q] == '-b':
        flag = False
    q+=1
if flag:
    print('未输入有效参数')
    exit(0)
def duru(src1):
    if(src1==''):
        return
    try:
        src = open(src1, "r", encoding='UTF-8')
        dst = open("E:\\作业\\软件工程\\输入.txt", "w", encoding='UTF-8')
        dst.write(src.read())
        src.close()
        dst.close()
    except:
        print('无此文件')
        exit(0)

src1=''
q=0
while q<len(sys.argv):
    if sys.argv[q]=='-map':
        src1=sys.argv[q+1]
        # "E:\\作业\\软件工程\\北京地铁路线.txt"
        duru(src1)
    q+=1

file_name = "E:\\作业\\软件工程\\输入.txt"
file = open(file_name,encoding='UTF-8')
xl =[]
xl1 =[]
while True:
    s = file.readline()
    if s == '\n' or s == '':
        break
    i=s.index(':')
    xl.append(s[:i])
    xl.append(s[i+1:-1])
j=1
x=-1
y=-1
graph = {}
zx={}

while j<len(xl) :
   xl1.append(xl[j-1])
   xl1.append([])
   while True:
    x=y
    y=(xl[j]).find(' ',x+1)
    if y < 0:
        zx[(xl[j])[x + 1:]] = []
        graph[(xl[j])[x+1:]] = []
        xl1[j].append((xl[j])[x+1:])
        break
    zx[(xl[j])[x+1:y]]=[]
    graph[(xl[j])[x+1:y]]=[]
    xl1[j].append((xl[j])[x+1:y])
   y=-1
   j+=2

j=1
x=-1
y=-1
while j<len(xl) :
   while True:
    x=y
    y=(xl[j]).find(' ',x+1)
    if y < 0:
        zx[(xl[j])[x + 1:]].append(xl[j-1])
        break
    zx[(xl[j])[x + 1:y]].append(xl[j-1])
   y=-1
   j+=2
j=0
d={}
while j<len(xl) :
   d[xl[j]]=xl[j+1]
   j+=2
file.close()
j=1
x=-1
y=-1

while j<len(xl) :
    while True:
        x=y
        y = (xl[j]).find(' ',x+1)
        if  (xl[j]).find(' ',y+1) < 0:
            graph[(xl[j])[x + 1:y]].append((xl[j])[y + 1:])
            graph[(xl[j])[y + 1:]].append((xl[j])[x + 1:y])
            break
        graph[(xl[j])[y+1:(xl[j]).find(' ',y+1)]].append((xl[j])[x+1:y])
        graph[(xl[j])[x + 1:y]].append((xl[j])[y + 1:(xl[j]).find(' ', y + 1)])
        if y<0 :
            break
    y=-1
    j+=2
graph2={}
for key in graph:
    graph2[key]=list(set(graph[key]))

# print(graph2)
# exit(0) #测试

def zdist(name,name2):
      return name == name2

f = {}
def search(z1,z2,s):
    if z1 not in graph2.keys():
        s.write('无此站点或少输了参数')
        s.write('\n')
        print('无此站点或少输了参数')
        return False
    if z2 not in graph2.keys():
        s.write('无此站点或少输了参数')
        s.write('\n')
        print('无此站点或少输了参数')
        return False
    search_queue = deque()
    search_queue += graph2[z1]
    for i in graph2[z1]:
        f[i]=z1
    searched = [z1]
    while search_queue:
        zd = search_queue.popleft()
        if not zd in searched:
            if zdist(zd,z2):
                luxian = []
                while True:
                    luxian.append(z2)
                    if (z2 == z1):
                        break
                    else:
                        z2 = f[z2]
                luxian.reverse()
                return luxian
            else:
                for i in graph2[zd]:
                    if i in f.keys() :
                        continue
                    f[i]=zd
                    search_queue += [i]
                searched.append(zd)
    return False

def cxzd(z1,z2,s) :
    xianl=search(z1,z2,s)
    if not xianl:
        return
    s.write(str(len(xianl)))
    s.write('\n')
    print(len(xianl))
    c=1
    nowxl=list(set(zx[xianl[0]])&set(zx[xianl[1]]))
    s.write(xianl[0])
    s.write('\n')
    print(xianl[0])
    while c<len(xianl):
        nextxl=list(set(zx[xianl[c]])&set(zx[xianl[c-1]]))
        if nowxl[0] not in nextxl:
            nowxl=nextxl
            s.write(nowxl[0])
            s.write('\n')
            print(nowxl[0])
        s.write(xianl[c])
        s.write('\n')
        print(xianl[c])
        c+=1

def cxallzd(xl,xl1,s):
    if xl in xl1:
        i=xl1.index(xl)+1
    else:
        s.write('无此地铁线路')
        s.write('\n')
        print('无此地铁线路')
        return
    c=0
    while c<len(xl1[i]):
        s.write(xl1[i][c])
        s.write('\n')
        print(xl1[i][c])
        c+=1
src2=''
q=0
while q<len(sys.argv):
    if sys.argv[q]=='-o':
        src2=sys.argv[q+1]
        # "E:\\作业\\软件工程\\输出.txt"
    q += 1
if src2=='':
    src2="输出(default).txt"
shuchu = open(src2, "w",encoding='UTF-8')
q=0
while q<len(sys.argv):
    if sys.argv[q] == '-a':
        cxallzd(sys.argv[q+1], xl1, shuchu)
        shuchu.write('\n')
        print('\n')
    q += 1

q=0
while q<len(sys.argv):
    if sys.argv[q] == '-b':
        cxzd(sys.argv[q+1],sys.argv[q+2],shuchu)
        shuchu.write('\n')
        print('\n')
    q += 1

shuchu.close()

