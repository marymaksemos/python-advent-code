#
file = open("input")
t_input=file.read()
file.close()
t_input=t_input.splitlines()
data=[]
for n in t_input:
  data.append(int(n))
  print(n)
for idx in range(0, len(data)):
  if(data[idx]+data[idx-1]) == 2020:
    m = data[idx] * data[idx-1] 
    print(m)

    #else: print("not found")
