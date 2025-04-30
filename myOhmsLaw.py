def calculateVoltage(Current, Resistance) :
    Voltage = Current * Resistance
    return Voltage 

def calculateResistance(Voltage, Current) :
    Resistance = Voltage / Current
    return Resistance 

def calculateCurrent(Voltage, Resistance) :
    Current = Voltage / Resistance
    return Current