#Creates an empty matrix (filled with 0)
def newMatrix(col,row):
#@param col: int
#@param row: int
	matr=[]
	for r in range(row):
		matr.append([])
		for c in range(col):
			matr[r].append(0)
	return  matr

#Fill the matrix
def fillMatrix():
	matr=newMatrix(9,9)
	for y in range(9):
		for x in range(9):
			t='('+str(x+1)+";"+str(y+1)+'): '
			inp=raw_input(t)
			if not inp:
				inp=0
			elif int(inp)>=1 and int(inp)<=9:
				matr[y][x]=int(inp)
			else:
				print "error: "+str(inp)+" its not a number between 1 and 9, its been left empty"
	return matr

#Creates a grid
def grid(col,row,xx,yy,w):
#@param col: Int (number of coulumns)
#@param row: Int (number of rows)
#@param xx: Int (lenght in px)
#@param yy: Int (height in px)
#@param w: Int (wide in px)
	grey=makeColor(125,125,125)
	tre=[]
	for c in range(0,10,3):
		tre.append(c)

	pic=makeEmptyPicture(xx,yy,white)
	colP=xx/col
	rowP=yy/row
	for r in range(row+1):
		rr=min(r*rowP,yy-1)
		for i in range(-w/2,w/2):
			addLine(pic,0,rr+i,yy,rr+i,grey)

	for c in range(col+1):
		cc=min(c*colP,xx-1)
		for i in range(-w/2,w/2):
			addLine(pic,cc+i,0,cc+i,xx,grey)

	if col==9 and row==9:
		for r in tre:
			rr=min(r*rowP,yy-1)
			for i in range(-w/2,w/2):
				addLine(pic,0,rr+i,yy,rr+i,black)

		for c in tre:
			cc=min(c*colP,xx-1)
			for i in range(-w/2,w/2):
				addLine(pic,cc+i,0,cc+i,xx,black)

	return pic

#Fill the grid
def showSudoku(matr):
	#@param matr: matrix
	col=len(matr[0])
	row=len(matr)
	xx=len(matr[0])*50
	yy=len(matr)*50
	pic=grid(col,row,xx,yy,6)
	sty=makeStyle(mono,bold,30)
	for r in range(row):
		for c in range(col):
			if matr[r][c]!=0:
				dimC=xx/col
				dimR=yy/row
				x=(dimC*c)+(dimC/2)
				y=(dimR*r)+(dimR/2)
				addTextWithStyle(pic,x-10,y+10,str(matr[r][c]),sty,black)
	show(pic)

#Check a 3x3 block
def blockCheck(matr,xB,yB):
	xx=xB*3
	yy=yB*3
	nBoll=[0]*len(matr)
	for x in range(xx,xx+3):
		for y in range(yy,yy+3):
			if matr[y][x]!=0:	
				if nBoll[(matr[y][x])-1]==0:
					nBoll[(matr[y][x])-1]=1
				else:
					return 0
			else:
				return 0		
	return 1

#Check th single column and row
def rowColCheck(matr,x,y):
	v=[0]*9
	for xx in range(9):
		if matr[y][xx]!=0:
			if v[matr[y][xx]-1]==0:
				v[matr[y][xx]-1]=1
			else:
				return 0
		else:
			return 0
	v=[0]*9
	for yy in range(9):
		if matr[yy][x]!=0:
			if v[matr[yy][x]-1]==0:
				v[matr[yy][x]-1]=1
			else:
				return 0
		else:
			return 0
	return 1

#Check the whole sudoku
def check(matr):
	for xy in range(9):
			if rowColCheck(matr,xy,xy)==0:
				return 0
	for x in range(3):
		for y in range(3):
			if blockCheck(matr,x,y)==0:
				return 0
	return 1

#Control if a n number can be placed in the (x,y) position
def precheck(matr,x,y,n):
	for i in range(9):
		if matr[y][i]==n:
			return 0
	for i in range(9):
		if matr[i][x]==n:
			return 0
	xx=(x//3)*3
	yy=(y//3)*3
	for i in range(3):
		for j in range(3):
			if matr[yy+i][xx+i]==n:
				return 0
	return 1

#The Solver
def resolve(matr):
	for y in range(9):
		for x  in range(9):
			if matr[y][x]==0:
				for a in range(1,10):
					if precheck(matr,x,y,a):
						matr[y][x]=a
						if resolve(matr):
							return 1
						else:
							matr[y][x]=0
				return 0	
	
	return 1



#---autoboot---
matr=[[5, 3, 0, 0, 7, 0, 0, 0, 0],
[6, 0, 0, 1, 9, 5, 0, 0, 0],
[0, 9, 8, 0, 0, 0, 0, 6, 0],
[8, 0, 0, 0, 6, 0, 0, 0, 3],
[4, 0, 0, 8, 0, 3, 0, 0, 1],
[7, 0, 0, 0, 2, 0, 0, 0, 6],
[0, 6, 0, 0, 0, 0, 2, 8, 0],
[0, 0, 0, 4, 1, 9, 0, 0, 5],
[0, 0, 0, 0, 8, 0, 0, 7, 9]]
print "-1- Add a new sudoku to solve (default)"
print "-2- Solve the example"
inp=raw_input("1 or 2: ")
if not inp:
	inp=1
print ""
if int(inp)==1:
	print "(x;y)"
	matr=fillMatrix()
	print "Solving..."
	resolve(matr)
	if check(matr):
		showSudoku(matr)
	else:
		print "There are no solutions."
elif int(inp)==2:
	showSudoku(matr)
	print "Solving..."
	resolve(matr)
	showSudoku(matr)
elif int(inp)==404:
	print "Mini Easter Egg Found!"
else:
	print "Error 404:  you can select only 1 or 2"

