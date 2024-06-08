def test_kwargs(name,age,*args,**kwargs):
  print(name,age,args)
  print(kwargs)

test_kwargs('田中',29,'広島','大阪',univ ='京都',btm = '大阪')
