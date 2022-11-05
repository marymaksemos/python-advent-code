#
file = open("input")
t_input=file.read()
file.close()
t_input=t_input.splitlines()
data=[]
for n in t_input:
  data.append(int(n))
  #print(n)
for idx in range(0, len(data)):
  for i in range(idx+1, len(data)):
     if(data[idx]+data[i]) == 2020:
      print(data[idx] * data[i]) 
    
