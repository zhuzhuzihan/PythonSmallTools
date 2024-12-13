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
    time.sleep(2)
    RobotNumber = random.randint(MinNumber, MaxNumber)
    if not check_number(RobotNumber):
        print('数字非法')
        continue
    RobotNumber = int(RobotNumber)
    if RobotNumber > MaxNumber:
        print('所输数字大于最大值')
        continue
    elif RobotNumber < MinNumber:
        print('所输数字小于最小值')
        continue
    if RobotNumber == RandomNumber:
        print('成功猜到了')
        print(f'所用步数: {User_walk}')
        break
    elif RobotNumber > RandomNumber:
        User_walk += 1
        MaxNumber = RobotNumber
    elif RobotNumber < RandomNumber:
        User_walk += 1
        MinNumber = RobotNumber
    print(f'现在范围{MinNumber}-{MaxNumber}')
