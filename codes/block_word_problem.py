def generate_successor(state, goal_state):
    list_of_states = []
    for i in range(3):
        if len(state[i]) == 0:
            continue
        temp = state[i][len(state[i]) - 1]
        state[i].pop()

        for j in range(3):
            if i != j:
                new_state = []
                state[j].append(temp)
                new_state = copy.deepcopy(state)
                print(new_state)
                if new_state == goal_state:
                    print("*** fuck it!!! ***")
                    sys.exit()

                list_of_states.append(new_state)
                state[j].pop()

        state[i].append(temp)

    return list_of_states


import copy
import sys
curr_state = [['A'], ['B', 'C'], []]
goal_state = [[], ['C','B','A'], []]
mera_state_list = generate_successor(curr_state, goal_state)
print("\n#############\n")


for i in mera_state_list:
    _ = generate_successor(i, goal_state)
    for j in _:
        _ = generate_successor(j, goal_state)
        for j in _:
            _ = generate_successor(j, goal_state)
            for j in _:
                _ = generate_successor(j, goal_state)
                print("\n********\n")
            print("\n********\n")
        print("\n********\n")
    print("\n#############\n")