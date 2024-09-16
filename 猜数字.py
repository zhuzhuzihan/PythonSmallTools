import random
import time


def check_number(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


print('猜数字')
time.sleep(2)
MaxNumber = 1000
MinNumber = 0
print(f'初始范围{MinNumber}-{MaxNumber}')
time.sleep(2)
RandomNumber = random.randint(MinNumber, MaxNumber)
User_walk = 0
while True:
    UserNumber = input('请输入数字: ')
    if not check_number(UserNumber):
        print('数字非法')
        continue
    UserNumber = int(UserNumber)
    if UserNumber > MaxNumber - 1:
        print('所输数字大于最大值')
        continue
    elif UserNumber < MinNumber + 1:
        print('所输数字小于最大值')
        continue
    if UserNumber == RandomNumber:
        print('成功猜到了')
        print(f'所用步数: {User_walk}')
        break
    elif UserNumber > RandomNumber:
        User_walk += 1
        MaxNumber = UserNumber
    elif UserNumber < RandomNumber:
        User_walk += 1
        MinNumber = UserNumber
    print(f'现在范围{MinNumber}-{MaxNumber}')
