import random
with open("abc.txt", "r", encoding="utf-8") as stream:
    rstream = stream.readlines()

while True:
    ran = random.randrange(0, len(rstream) - 1,2)
    dic1 = rstream[ran]
    print(dic1.strip())
    print(rstream[rstream.index(dic1)+1].strip())
    anser = input("请输入答案:")
    with open("anser.txt", "r") as stream1:
        rstream1 = stream1.readlines()
        lst1 = str(rstream1[ran]).strip()
        print(lst1)
    if anser == lst1:
        print("对")
    else:
        print(f"error!!! 正确答案是{lst1}")
