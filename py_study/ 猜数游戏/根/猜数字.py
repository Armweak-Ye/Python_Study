answer = 68
def game():
   a = input('我想了一个100以内的正整数，你要不要猜猜看 Yes or No:')
   if a == 'Yes':
       while True:
           yours = int(input('你猜是多少：'))
           if yours == answer:
             print('你猜对了，真棒。')
             exit()
           elif 100>=yours > answer:
             print('太大了，再小一点')
           elif 0<= yours < answer:
             print('太小了，往大了猜')
           elif yours > 100:
             print('我说过是100以内的数')
           else:
             print('我说过是一个正整数')
   else:
     print('好吧，看来你不想和我玩，伤心')
game()