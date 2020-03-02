#problema de los filosofos
import threading
import random
import time

class Filosofos(threading.Thread):

    def __init__(self, name, state,  leftfork, rightfork):
        threading.Thread.__init__(self)
        self.leftfork = leftfork
        self.rightfork = rightfork
        self.name = name
        self.state = state

    def run(self):
        while True:
            try:
                self.rightfork.acquire()
                try:
                    self.leftfork.acquire()
                    self.state = "comiendo"
                    print("El filosofo {} se encuentra {}".format(self.name, self.state))
                    intentosC = 0
                    time.sleep(random.randint(1,5))
                    self.state = "pensando"
                    print("El filosofo {} se encuentra {}".format(self.name, self.state))
                    self.rightfork.release()
                    self.leftfork.release()
                    time.sleep(random.randint(1,10))
                except:
                    self.rightfork.release()
                    self.state = "hambriento"
                    print("El filosofo {} se encuentra {}".format(self.name, self.state))
                    intentosC += 1
                    time.sleep(random.randint(1,3))

            except:
                self.state = "hambriento"
                print("El filosofo {} se encuentra {}".format(self.name, self.state))
                intentosC += 1
                time.sleep(random.randint(1,3)
#aqui es donde nunca deben entrar los hilos de los filosofos, ya que no debe darse el "deadlock" o abrazo mortal
#es decir, bloquearse mutuamente
                if intentosC > 10: 
                    self.state = "Muerto de Hambre"
                    print("El filosofo {} ha {}".format(self.name, self.state))
                    break


                

t1 = threading.RLock()
t2 = threading.RLock()
t3 = threading.RLock()
t4 = threading.RLock()
t5 = threading.RLock()

f1 = Filosofos("1", "pensando", t1, t2)
f2 = Filosofos("2", "pensando", t2, t3)
f3 = Filosofos("3", "pensando", t3, t4)
f4 = Filosofos("4", "pensando", t4, t5)
f5 = Filosofos("5", "pensando", t5, t1)

f1.start()
f2.start()
f3.start()
f4.start()
f5.start()
