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
while True:
    UserNumber = input('请输入数字')
    if not check_number(UserNumber):
        print('数字非法')
        continue
    UserNumber = int(UserNumber)
    if UserNumber > MaxNumber:
        print('所输数字大于最大值')
        continue
    if UserNumber < MinNumber:
        print('所输数字小于最大值')
        continue