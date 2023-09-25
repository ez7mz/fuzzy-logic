import numpy as np
import matplotlib.pyplot as plt
from toolspack import *

# main function
if __name__ == "__main__":
    label = input("Enter label: ")
    
    if label == 'cars-price':
        
        car_age = [6, 10, 17, 28, 2]
        car_distance = [80000, 50000, 1000, 200000, 250000]
        car_price = []
        
        # get control system and simulation
        car_price_ctrl, car_price_simulation = get_fuzzy_toolkit(label)
        
        for i in range(len(car_age)):
            car_price_simulation.input['car_age'] = car_age[i]
            car_price_simulation.input['car_distance'] = car_distance[i]
            car_price_simulation.compute()
            car_price.append(car_price_simulation.output['car_price'])
            
        test_system_pretty_print(["Car Age", "Distance", "Car Price"], [car_age, car_distance, car_price])
        
        # Plot membership functions
        car_price_ctrl["car_age"].view()
        car_price_ctrl["car_distance"].view()
        car_price_ctrl["car_price"].view()
        plt.show()
        
    elif label == 'cpu-fan-speed':
        
        # Test values
        core_temps = [80, 75, 25, 90, 60]
        clocks = [3.5, 1.5, 1.2, 3.8, 2.7]
        fan_speeds = []
        
        # get control system and simulation
        fan_speeds_ctrl, fan_speeds_simulation = get_fuzzy_toolkit(label)
        
        for i in range(len(core_temps)):
            fan_speeds_simulation.input['core_temperature'] = core_temps[i]
            fan_speeds_simulation.input['clock_speed'] = clocks[i]
            fan_speeds_simulation.compute()
            fan_speeds.append(fan_speeds_simulation.output['fan_speed'])
            
        test_system_pretty_print(["Core Temp", "Clocks", "Fan Speed"], [core_temps, clocks, fan_speeds])
        
        # Plot membership functions
        fan_speeds_ctrl["core_temperature"].view()
        fan_speeds_ctrl["clock_speed"].view()
        fan_speeds_ctrl["fan_speed"].view()
        plt.show()
    
    else:
        print('Error: label not found')
        exit(1)