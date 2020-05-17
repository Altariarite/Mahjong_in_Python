from Pai import originalYama,allPai,showHand
import numpy as np

testcase = np.random.permutation(allPai[:27]*4)

#立直Ron
def lichi(lichi):
    if(lichi):
        return 1,True
    else:
        return 0,False

#断幺九Ron
def noyaojiu(hand,openHand):
    ron = True
    yao13 = [0,8,9,17,18,26,27,28,29,30,31,32,33]
    for i in yao13:
        if(hand[0][i]==1):
            ron = ron and False
        for oph in openHand:
            if(i in oph):
                ron = ron and False
    if(ron):
        return 1,True
    else:
        return 0,False

#十三幺Ron
def kokusi13machi(hand,openHand):
    yao13 = ["一萬","九萬","一筒","九筒","一索","九索","中","發","白","東","西","南","北"]
    last = hand[-1]
    ron = (len(hand) == 14) and (len(openHand)==0)
    for p in yao13:
        ron = ron and p in [str(h) for h in hand]
    ron = ron and str(last) in yao13
    if(ron):
        return 6
    else:
        return 0


#七对子Ron
def chitoi(hand,openHand):
    hand.sort()
    ron = (len(hand) == 14) and (len(openHand)==0)
    for i in range(0,14,2):
        ron = ron and (str(hand[i]) == str(hand[i+1]))
    if(ron):
        return 2
    else:
        return 0

#飘Ron
def piao(hand,openHand,hand_num):
    ron = True
    #检查展开的手牌是否均为碰牌
    for oph in openHand:
        if(not (oph[0]==oph[1] and oph[1]==oph[2])):
            ron = ron and False
    #检查手中的牌是否满足飘的条件
    #如果手中是一个雀头则一定满足条件
    if(hand_num==2):
        ron = ron and True
    #如果手中是一个雀头加任意数量的刻子则也满足条件,但需要注意可能出现一杯口或七对子误判的情况
    else:
        quetou = 0
        for j in range(34):
            if(openHand[j][0]==1):
                 if(openHand[j][1]==1 and openHand[j][2]==0):
                     quetou += 1
                 if(not (openHand[j][1]==1 and openHand[j][2]==1) and not(openHand[j][1]==1 and openHand[j][2]==0)):
                     ron = ron and False
        if( not quetou == 1):
            ron = ron and False
    if(ron):
        return 2,True
    else:
        return 0,False

#大三元Ron
def dasanyuan(hand,openHand):
    ron = [False,False,False]
    if(hand[27][2]==1):
        ron[0]=True
    if(hand[28][2]==1):
        ron[1]=True
    if(hand[29][2]==1):
        ron[2]=True
    for oph in openHand:
        if(27 in oph):
            ron[0]=True
        if(28 in oph):
            ron[1]=True
        if(29 in oph):
            ron[2]=True
    if(not False in ron):
        return 4,True
    else:
        return 0,False


#役牌 自风
def zifeng(hand,openHand,zifeng):
    ron = False
    for oph in openHand:
        if(zifeng in oph):
            ron = True
    if(hand[zifeng][2]==1):
        ron = True
    if(ron):
        return 1,True
    else:
        return 0,False

#役牌 场风
def zifeng(hand,openHand,changfeng):
    ron = False
    for oph in openHand:
        if(changfeng in oph):
            ron = True
    if(hand[changfeng][2]==1):
        ron = True
    if(ron):
        return 1,True
    else:
        return 0,False

#役牌 中
def sanyuan_zhong(hand,openHand):
    ron = False
    for oph in openHand:
        if(27 in oph):
            ron = True
    if(hand[27][2]==1):
        ron=True
    if(ron):
        return 1,True
    else:
        return 0,False
#役牌 发
def sanyuan_fa(hand,openHand):
    ron = False
    for oph in openHand:
        if(28 in oph):
            ron = True
    if(hand[28][2]==1):
        ron=True
    if(ron):
        return 1,True
    else:
        return 0,False

#役牌 白
def sanyuan_bai(hand,openHand):
    ron = False
    for oph in openHand:
        if(29 in oph):
            ron = True
    if(hand[29][2]==1):
        ron=True
    if(ron):
        return 1,True
    else:
        return 0,False

#役牌 一杯口 此处hand为list[Pai] openHand为list[list[Pai]]
def yibeikou(hand,openHand):
#在判断一杯口的时候，需要防止出现飘牌误判,七对子误判,或者三暗刻误判.
    if(len(openHand))>0):
        ron = False
    else:
        for i in range(3):
            for j in range(0+9*i,6+9*i):
                if(hand.count(j)==2):
                    if(hand.count(j+1)==2):
                        ron = True
                    if(hand.count(j+1)==3 and hand.count(j+2)==3 and (hand.count(j+3)==1 or hand.count(j+3)==4) and (j+3 < 9+9*i)):
                        ron = True
                    if(hand.count(j-1)==3 and hand.count(j-2)==3 and (hand.count(j-3)==1 or hand.count(j-3)==4) and (j-3 > 9*i)):
                        ron = True
    if(ron):
        return 1,True
    else:
        return 0,False



def num2array(hand):
    nums = np.zeros([9])
    label = {"一":1,"二":2,"三":3,"四":4,"五":5,"六":6,"七":7,"八":8,"九":9}
    for p in hand:
        nums[label[str(p)[0]]] += 1
    return nums

def pai2array(hand):
    nums = np.zeros([34])
    label = {'一萬': 0, '二萬': 1, '三萬': 2, '四萬': 3, '五萬': 4, '六萬': 5, '七萬': 6, '八萬': 7, '九萬': 8,
             '一筒': 9, '二筒': 10, '三筒': 11, '四筒': 12, '五筒': 13, '六筒': 14, '七筒': 15, '八筒': 16, '九筒': 17,
             '一索': 18, '二索': 19, '三索': 20, '四索': 21, '五索': 22, '六索': 23, '七索': 24, '八索': 25, '九索': 26,
             '中': 27, '發': 28, '白': 29, '東': 30, '西': 31, '南': 32, '北': 33}
    for p in hand:
        nums[label[str(p)]] += 1
    return nums

def existMians(num):
    if not sum(num)%3 == 0: # Mians couldnot be constructed
        return False
    a = num[0]         # Pai currentry concerend
    b = num[1]         # next pai tobe concerned
    for i in range(7):
        r = a % 3      # number of Pai not becoming Mians
        if(b>=r and num[i+2]>=r):
            a = b - r
            b = num[i+2] - r
        else:
            return False
    if(a%3==0 and b%3==0): # last check
        return True
    else:
        return False

def qinwho(num):
    handsum = 0
    for i in range(9):
        handsum += i*num[i]
    i = int(handsum *2 %3)
    return backtrack(i,num)

def backtrack(i,num):
    if not i<9:
        return False
    num[i] -= 2       # try this as head
    if num[i] >= 0:
        if existMians(num):
            num[i] += 2
            return True
    num[i] += 2
    return backtrack(i+3,num)

def who(hand):
    nums = pai2array(hand)
    head = -1               # head is not decided yet
    # judge each numPais
    for i in range(3):
        case = sum(nums[i*9:i*9+10])%3
        if case == 1:
            return False
        elif case == 2:
            if(head==-1):
                head = i
            else:
                return False

    # judge for charPais
    for i in range(27,34):
        if nums[i]%3 == 1:
            return False
        elif nums[i]%3 == 2:
            if head == -1:
                head = i
            else:
                return False
        else:
            pass # charPai forms 刻子

    # final judge with head check
    for i in range(3):
        if i==head: # head is nmPai
            if not qinwho(nums[9*i:9*i+10]):
                return False
        else:
            if not existMians(nums[9*i:9*i+10]):
                return False
    return True


#日本麻将胡牌函数
#hand 为 int[4][34],openHand 为 list[list[Pai]]
#lichi为booolean,为了判断Player是否立直
#zifeng和changfeng均为int,[30--33](表示本场游戏的自风与场风)
def JapanRon(hand,openHand,lichi,zifeng,changfeng):
    open_num = 0
    hand_num = 0
    for i in range(4):
        for j in range(34):
            if(hand[o][h]==1):
                open_num += 1
            if(openHand[o][h]==1):
                hand_num += 1
    kokusi = kokusi13machi(hand,openHand)
    chitois = chitoi(hand,openHand)
    piao = piao(hand,openHand,hand_num)
    return (kokusi + chitois + normal_who)