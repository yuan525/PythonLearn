x = input("")
if int(x)%2==0:
    x = int(x-1)
else:
    x = int(x)
i =1
while i<=x:
    str="*" * i
    print("{:i^}".format(str))
    i=i+2
    # TODO: write code...