#memasukkan data
r = int(input("Bilangan 1 :"))
s = int(input("Bilangan 2 :"))
t = int(input("Bilangan 3 :"))

#memasukkan rumus if dan else
if (r<s) and (r<t):
        if (s<t):
            print("Urutan bilangan dari yang terkecil adalah" ,r, s, t)
        else:
            print("Urutan bilangan dari yang terkecil adalah" ,r , t, s)
elif (s<t) and (s<r):
    if (t<r):
        print("Urutan bilangan dari yang terkecil adalah" ,s, t, r)
    else:
        print("Urutan bilangan dari yang terkecil adalah" ,s, r, t)
else:
    if(r<s):
        print("Urutan bilangan dari yang terkecil adalah" ,t, r, s)
    else:
        print("Urutan bilangan dari yang terkecil adalah" ,t, s, r)
        
    
        
