def canCompleteCircuit(gas, cost):
    station_idx = -1
    gas_amount = 0
    for g, c, i in zip(gas, cost, range(len(cost))):
        if g + gas_amount >= c:
            gas_amount = gas_amount + g - c
            if station_idx == -1:
                station_idx = i
        else:
            gas_amount = 0
            station_idx = -1
    
    if station_idx == -1:
        return station_idx

    for i in range(station_idx):
        if gas[i] + gas_amount >= cost[i]:
            gas_amount = gas_amount + gas[i] - cost[i]
        else:
            return -1

    return station_idx
