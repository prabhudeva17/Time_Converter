a=1
while(a<15):
    x=int(input('Enter the Number Of Seconds\n'))
    y=x//31536000
    y1=x-y*31536000
    d=y1//86400
    d1=y1-d*86400
    h=d1//3600
    d2=d1-h*3600
    m=d2//60
    s=d2%60
    if(y!=0):
        print(y,"year",d,"day",h,"hour",m,"minute",s,"second")
    else:
        if(d!=0):
            print(d,"day",h,"hour",m,"minute",s,"second")
        else:
            if(h!=0):
                print(h,"hour",m,"minute",s,"second")
            else:
                if(m!=0):
                    print(m, "minute", s, "second")
                else:
                 print(s,"second")
    a=a+1