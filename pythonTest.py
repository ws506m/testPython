#This is the test python code for git test purpose
x,y,z,N = (int(raw_input()) for _ in range(4))
print([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a+b+c !=N])
