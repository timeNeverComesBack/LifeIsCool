import os
from time import sleep


def valueSum():
    sum = a + b + c + d
    return sum

def valueLeave(valueSum):
    valueLeave = 40 - valueSum
    return valueLeave

def lifeIsRolling():
    global a
    global b
    global c
    global d
    global left
    a = input("请设置体质：")
    while 1:
        try:
            a = int(a)
            break
        except:
            a = input("离谱输入，请重新设置体质：")

    while 1:
        if 0 <= a <= 40:
            break
        else:
            a = input("离谱输入，请重新设置体质：")

    left = valueLeave( valueSum() )
    print("剩余 " + str( valueLeave( valueSum() ) ) + "点")

    b = input("请设置智力：")
    while 1:
        try:
            b = int(b)
            if 0 <= b <= left:
                break
            else:
                b = input("离谱输入，请重新设置智力：")
        except:
            b = input("离谱输入，请重新设置智力：")

    left = valueLeave( valueSum() )
    print("剩余 " + str( valueLeave( valueSum() ) ) + "点")

    c = input("请设置颜值：")
    while 1:
        try:
            c = int(c)
            if 0 <= c <= left:
                break
            else:
                c = input("离谱输入，请重新设置颜值：")
        except:
            c = input("离谱输入，请重新设置颜值：")

    left = valueLeave( valueSum() )
    print("剩余 " + str( valueLeave( valueSum() ) ) + "点")

    d = input("请设置家境：")
    while 1:
        try:
            d = int(d)
            if 0 <= d <= left:
                break
            else:
                d = input("离谱输入，请重新设置家境：")
        except:
            d = input("离谱输入，请重新设置家境：")


print("""
         _      _  __       _____        _____            _ 
        | |    (_)/ _|     |_   _|      / ____|          | |
        | |     _| |_ ___    | |  ___  | |     ___   ___ | |
        | |    | |  _/ _ \   | | / __| | |    / _ \ / _ \| |
        | |____| | ||  __/  _| |_\__ \ | |___| (_) | (_) | |
        |______|_|_| \___| |_____|___/  \_____\___/ \___/|_|
                                                            
"""
)

a = 0
b = 0
c = 0
d = 0
left = 40
print("轰隆！！！")
sleep(0.5)
print("伴随着一声惊雷，我慢慢地睁开了眼。")
sleep(1)
print("眼前一片虚无，突然，我面前出现了一个控制面板。")
sleep(1)
print("一声电子的女生传来……")
sleep(0.8)
print("欢迎来到新世界，请选择出生。")
sleep(0.8)
print("我仔细看着面前的控制面板，上面写着：")
sleep(1)
print("人生控制器，这里共40个点数，请配置出生属性。\n")

lifeIsRolling()

print("\n当前数值为：\n体质：\t" + str(a) + "\n智力：\t" + str(b) + "\n颜值：\t" + str(c) + "\n家境：\t" + str(d) + "\n")
confirmResult = input("请确认开始你的人生：输入yes开始！")

while 1:
    if confirmResult == "yes" or confirmResult == 'y':
        print("你出生了！")
        if a == 10 and b == 10 and c == 10 and d == 10:
            with open("Possibilities/1.txt","r", encoding='utf-8') as f:
                print(f.read())
        else:
            with open("Possibilities/2.txt","r", encoding='utf-8') as f:
                print(f.read())
        print("Game Over!")
        over = input("是否重头来过？ yes or no：")
        if over == "yes" or over == 'y':
            a = 0
            b = 0
            c = 0
            d = 0
            left = 40
            print("共40个点数，请配置出生属性\n")
            lifeIsRolling()
            print("\n当前数值为：\n体质：\t" + str(a) + "\n智力：\t" + str(b) + "\n颜值：\t" + str(c) + "\n家境：\t" + str(d) + "\n")
            confirmResult = input("请确认开始你的人生：输入yes开始！")
        else:
            print("\n")
            break
        # break
    else:
        a = 0
        b = 0
        c = 0
        d = 0
        left = 40
        print("共40个点数，请配置出生属性\n")
        lifeIsRolling()
        print("\n当前数值为：\n体质：\t" + str(a) + "\n智力：\t" + str(b) + "\n颜值：\t" + str(c) + "\n家境：\t" + str(d) + "\n")
        confirmResult = input("请确认开始你的人生：输入yes开始！")

os.system("pause")