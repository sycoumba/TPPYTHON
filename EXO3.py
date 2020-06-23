R1=int(input("R1?"))
R2=int(input("R2?"))
R3=int(input("R3?"))
Rser= R1+R2+R3
Rpar=(R1*R2*R3)//((R1*R2)+(R2*R3)+(R1*R3))
print("la resistance en serie?",Rser)
print("la resistance en paralelle?",Rpar)