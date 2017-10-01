from random import random
from collections import defaultdict

def simulate(transitions, p, pi1, pi2, tacts_count, start_state):
    result = defaultdict(int)

    current_state = start_state
    for _ in range(tacts_count):
        p_state = random() <= p
        pi1_state = random() <= pi1
        p2_state = random() <= pi2
        result[current_state] += 1        
        current_state = next((x for x in transitions if x[0] == current_state and x[2](p_state, pi1_state, p2_state)))[1]

    return result
