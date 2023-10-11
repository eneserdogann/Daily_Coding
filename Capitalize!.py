s = 'alan parsons project'

for i in s.split():
    s = s.replace(i,i.capitalize())

print(s)