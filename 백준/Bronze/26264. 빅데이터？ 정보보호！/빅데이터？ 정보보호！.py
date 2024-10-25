n = int(input())
ans = input()
bigdata = ans.count("bigdata")
security = ans.count("security")
if bigdata > security:
    print("bigdata?")
elif bigdata < security:
    print("security!")
else:
    print("bigdata? security!")