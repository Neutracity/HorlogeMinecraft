h =1
m=0
s=0
stri = ''
if h < 10:
    stri +=  f'0{h}'
else:
    stri += str(h)
if m < 10:
    stri +=  f'0{m}'
else:
    stri += str(m)
if s < 10:
    stri +=  f'0{s}'
else:
    stri += str(s)
print(stri)