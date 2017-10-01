from transitions import TRANSITIONS
from simulator import simulate


START_STATE = '0000'
TACTS_COUNT = 100000

P = 0.75
PI1 = 0.7
PI2 = 0.7


def main():
    states_statistics = simulate(TRANSITIONS, P, PI1, PI2, TACTS_COUNT, START_STATE)

    for state, count in sorted(states_statistics.items(), key=lambda x: int(x[0])):
        print(state, count / TACTS_COUNT)


if __name__ == '__main__':
    main()
