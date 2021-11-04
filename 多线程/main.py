'''
    主程序
'''
from kfc import *
from producer import *
from consumer import *

kfc = KFC()
p1=Producer("生产者1",kfc)
p2=Producer("生产者2",kfc)
p3=Producer("生产者3",kfc)

c1 = Consumer("消费者1",kfc)
c2 = Consumer("消费者2",kfc)
c3 = Consumer("消费者3",kfc)
c4 = Consumer("消费者4",kfc)
c5 = Consumer("消费者5",kfc)
c6 = Consumer("消费者6",kfc)
c7 = Consumer("消费者7",kfc)
c8 = Consumer("消费者8",kfc)

p1.start()
p2.start()
p3.start()

c1.start()
c2.start()
c3.start()
c4.start()
c5.start()
c6.start()
c7.start()
c8.start()

