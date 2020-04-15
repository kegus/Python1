# 1. TrafficLight
from time import sleep
from itertools import cycle


class TrafficLight:
    __color = None
    index = 0
    color_list = ["red", "yellow", "green"]
    time_list = [7, 2, 8]

    def inc_index(self):
        self.index += 1
        if self.index > 2:
            self.index = 0

    def running(self):
        n = 0
        for i, clr in cycle(enumerate(self.color_list)):
            n += 1
            self.__color = self.color_list[self.index]
            print(n, self.__color)
            sleep(self.time_list[self.index])
            if i != self.index:
                print("Index error")
                break
            if n > 9:
                break
            self.inc_index()


semaphore = TrafficLight()
semaphore.running()
print("finished")
