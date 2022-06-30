from mq import *
import sys, time

mq = MQ();
while True:
    perc = mq.MQPercentage()
    sys.stdout.write("\r")
    sys.stdout.write("\033[K")
    sys.stdout.write("LPG: %g ppm" % (perc["GAS_LPG"]))
    sys.stdout.flush()
    time.sleep(0.1)