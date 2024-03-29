# Done By:
# Muhd Zharif bin Msduki (1611777)
# Muhamad Arif Lutfi bin Aziz (1315791)

# sent = "Time flies like an arrow"
icecream = "3 1 3"
# x_seq = sent.split()
# x_seq = icecream.split()
Q = {'N', 'DT', 'V', 'P'}
# Q = ('Sunny','Rainy')
# O = ('walk', 'shop', 'clean')
O = ('Time', 'flies', 'like', 'an', 'arrow')
# SP = {'Rainy': 0.6, 'Sunny': 0.4}   #start to the state
SP = {'N': 0.5, 'DT': 0.4, 'V': 0.1, 'P': 0.0}

'''TP = {'Rainy' : {'Rainy': 0.7, 'Sunny': 0.3},   #rainy to rainy or rainy to sunny
      'Sunny' : {'Rainy': 0.4, 'Sunny': 0.6}}'''

TP = {'N': {'N': 0.2, 'V': 0.7, 'P': 0.1, 'DT': 0.0},
      'DT': {'N': 1.0, 'V': 0, 'P': 0, 'DT': 0},
      'V': {'DT': 0.4, 'N': 0.4, 'P': 0.1, 'V': 0.1},
      'P': {'DT': 0.6, 'N': 0.4, 'V': 0, 'P': 0}}

EP = {'N': {'Time': 0.1, 'flies': 0.1, 'like': 0, 'an': 0, 'arrow': 0.1},
      'DT': {'Time': 0, 'flies': 0, 'like': 0, 'an': 0.3, 'arrow': 0},
      'V': {'Time': 0.1, 'flies': 0.2, 'like': 0.2, 'an': 0, 'arrow': 0},
      'P': {'Time': 0, 'flies': 0, 'like': 0.1, 'an': 0, 'arrow': 0}}

'''EP = {'Rainy' : {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
      'Sunny' : {'walk': 0.6, 'shop': 0.3, 'clean': 0.1}}'''


# TP = transition_probability
# EP = emission_probability

# this function consider all possible combination of states = pow(2,n)
def viterbi(O, Q, SP, TP, EP):
    # a set that hold the final best probable path for the list of observations (max alpha)
    T = {}

    # for every possible state in Q
    for q in Q:
        # get probability of each starting state, create a tuple(pair of values)
        T[q] = (SP[q], [q])  # example: T[q] = (0.4,['Sunny'])

    # for every possible observations in O
    for x in O:
        # create a set/dictionary to hold prob. for each observation
        U = {}

        # for every next state in Q states
        for q_next in Q:

            # initialize max path and max_p
            max_path = None;
            max_p = 0

            # for every state in Q
            for q in Q:

                # set prob and path = prob of each start state
                (prob, path) = T[q]

                # calculate prob. of alpha[i,j]
                p = prob * TP[q][q_next] * EP[q_next][x]

                # compare p with default max_p
                if p > max_p:
                    max_p = p;
                    max_path = path + [q_next]  # concatenation of paths

            # pick the best path at each alpha
            U[q_next] = (max_p, max_path)

        # print(U)
        T = U

    return (T)


path = viterbi(O, Q, SP, TP, EP)
print(path)