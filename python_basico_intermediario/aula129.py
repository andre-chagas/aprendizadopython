import importlib

import aula129_m

print(aula129_m.variavel)

for i in range(10):
 importlib.reload(aula129_m)
 print(i)
 


print('Fim')
