aaa=dict(a=1,b=2,c=3)
print(sorted([(v,k) for k,v in aaa.items()],reverse=True))