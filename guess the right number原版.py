import random
score = 0
for n in range(10):
    i = 0
    num = random.randint(1,100)
    while True:
        a = int(input('please input a number='))
        if a > num:
            print('bigger than the right number')
            i+=1
        elif a < num:
            print('smaller than the right number')
            i += 1
        else:
            print('Good Job!!!')
            i = 10 - i
            print('your score is ',i)
            score = score + i
            break
print('game is over!!')
print('Your final score is ',score)
if score == 100:
    print('你TM是挂')
elif score <100 and score >= 90:
    print("fantastic")
elif score < 90 and score >= 70:
    print("fabulous")
elif score <70 and score >= 60:
    print("good")
elif score < 60 and score>=0:
    print("not good")
else:
    print("bad")

