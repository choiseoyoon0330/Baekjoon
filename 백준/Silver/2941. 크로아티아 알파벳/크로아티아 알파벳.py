word=input()
cro_list=['c=','c-','dz=','d-','lj','nj','s=','z=']
count=0

for i in range(8):
    count+=word.count(cro_list[i])
    word=word.replace(cro_list[i],'.')
print(len(word))