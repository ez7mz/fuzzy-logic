import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def get_fuzzy_toolkit(label):
    if label == 'cpu-fan-speed':
        # Create fuzzy controller
        core_temperature = ctrl.Antecedent(np.arange(0, 101, 1), 'core_temperature')
        clock_speed = ctrl.Antecedent(np.arange(0, 4.1, 0.1), 'clock_speed')
        fan_speed = ctrl.Consequent(np.arange(0, 6001, 1), 'fan_speed')

        # Define membership functions
        core_temperature['cold'] = fuzz.trimf(core_temperature.universe, [0, 0, 50])
        core_temperature['warm'] = fuzz.trimf(core_temperature.universe, [30, 50, 70])
        core_temperature['hot'] = fuzz.trimf(core_temperature.universe, [50, 100, 100])

        clock_speed['low'] = fuzz.trimf(clock_speed.universe, [0, 0, 1.5])
        clock_speed['warm'] = fuzz.trimf(clock_speed.universe, [0.5, 2, 3.5])
        clock_speed['hot'] = fuzz.trimf(clock_speed.universe, [2.5, 4, 4])

        fan_speed['slow'] = fuzz.trimf(fan_speed.universe, [0, 0, 3500])
        fan_speed['fast'] = fuzz.trimf(fan_speed.universe, [2500, 6000, 6000])

        # Define rules
        rule1 = ctrl.Rule(core_temperature['cold'] & clock_speed['low'], fan_speed['slow'])
        rule2 = ctrl.Rule(core_temperature['cold'] & clock_speed['warm'], fan_speed['slow'])
        rule3 = ctrl.Rule(core_temperature['cold'] & clock_speed['hot'], fan_speed['fast'])
        rule4 = ctrl.Rule(core_temperature['warm'] & clock_speed['low'], fan_speed['slow'])
        rule5 = ctrl.Rule(core_temperature['warm'] & clock_speed['warm'], fan_speed['slow'])
        rule6 = ctrl.Rule(core_temperature['warm'] & clock_speed['hot'], fan_speed['fast'])
        rule7 = ctrl.Rule(core_temperature['hot'] & clock_speed['low'], fan_speed['slow'])
        rule8 = ctrl.Rule(core_temperature['hot'] & clock_speed['warm'], fan_speed['fast'])
        rule9 = ctrl.Rule(core_temperature['hot'] & clock_speed['hot'], fan_speed['fast'])

        # Create fuzzy system
        fan_speed_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
        fan_speed_simulation = ctrl.ControlSystemSimulation(fan_speed_ctrl)

        return {"core_temperature": core_temperature, "clock_speed": clock_speed, "fan_speed": fan_speed}, fan_speed_simulation
    elif label == 'cars-price':
        # Create fuzzy controller
        car_age = ctrl.Antecedent(np.arange(0, 31, 1), 'car_age')
        car_distance = ctrl.Antecedent(np.arange(0, 300001, 1), 'car_distance')
        car_price = ctrl.Consequent(np.arange(0, 30001, 1), 'car_price')

        # Define membership functions
        car_age['old'] = fuzz.trimf(car_age.universe, [0, 5, 15])
        car_age['average'] = fuzz.trimf(car_age.universe, [5, 15, 25])
        car_age['new'] = fuzz.trimf(car_age.universe, [15, 25, 30])

        car_distance['short'] = fuzz.trimf(car_distance.universe, [0, 50000, 150000])
        car_distance['medium'] = fuzz.trimf(car_distance.universe, [50000, 150000, 250000])
        car_distance['large'] = fuzz.trimf(car_distance.universe, [150000, 250000, 300000])

        car_price['cheap'] = fuzz.trimf(car_price.universe, [0, 5000, 15000])
        car_price['economic'] = fuzz.trimf(car_price.universe, [5000, 15000, 25000])
        car_price['expensive'] = fuzz.trimf(car_price.universe, [15000, 25000, 30000])

        # Define rules
        rule1 = ctrl.Rule(car_age['old'] & car_distance['short'], car_price['economic'])
        rule2 = ctrl.Rule(car_age['old'] & car_distance['medium'], car_price['cheap'])
        rule3 = ctrl.Rule(car_age['old'] & car_distance['large'], car_price['cheap'])
        rule4 = ctrl.Rule(car_age['average'] & car_distance['short'], car_price['expensive'])
        rule5 = ctrl.Rule(car_age['average'] & car_distance['medium'], car_price['economic'])
        rule6 = ctrl.Rule(car_age['average'] & car_distance['large'], car_price['cheap'])
        rule7 = ctrl.Rule(car_age['new'] & car_distance['short'], car_price['expensive'])
        rule8 = ctrl.Rule(car_age['new'] & car_distance['medium'], car_price['expensive'])
        rule9 = ctrl.Rule(car_age['new'] & car_distance['large'], car_price['economic'])

        # Create fuzzy system
        car_price_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
        car_price_simulation = ctrl.ControlSystemSimulation(car_price_ctrl)

        return {"car_age":car_age, "car_distance":car_distance, "car_price":car_price}, car_price_simulation

    
def test_system_pretty_print(header, body):
    # Display the table
    print("System test result:\n")
    
    # header is a list contain each column title
    _header = "    ".join(header)
    print("    "+_header)
    print("    __________" * len(header))
    
    for i in range(len(body[0])):
        print(f"    {body[0][i]:<8}    {body[1][i]:<6}    {body[2][i]:<12.1f}")