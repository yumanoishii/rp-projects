from gpiozero import CPUTemperature
from time import sleep, strftime,time
import matplotlib.pyplot as plt

cpu = CPUTemperature()
cpu.temperature


while True:
    cpu.temperature
    sleep(1)
    
