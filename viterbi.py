#sent = "Time flies like an arrow"
icecream = "3 1 3"
#x_seq = sent.split()
#x_seq = icecream.split() 

Q = ('N','DT','V','ADV','P','ADJ') #Q adalah state
O = ('the','cook','prepares','a','lovely','drink')
SP = {'N': 0.5, 'DT': 0.4, 'V':0.1,'P':0.0,'ADV':0.0,'ADJ':0.0}
TP = {'DT': {'N': 0.7, 'V': 0.3, 'ADV':0.1,'P':0.0,'DT':0.0,'ADJ':0.0},
      'N' : {'N': 0.5, 'V': 0.4,'P':0.1,'DT':0.0,'ADV':0.0,'ADJ':0.0},
      'V':{'DT':0.3,'N':0.4,'P':0.1,'V':0.1,'ADV':0.0,'ADJ':0.0},
      'P':{'DT':0.6,'N':0.4,'P':0.0,'ADV':0.0,'V':0.0,'ADJ':0.0},
      'ADV':{'N':0.5,'ADJ':0.1,'V':0.3,'ADV':0.0,'DT':0.0,'P':0.0},
      'ADJ': {'N': 0.0, 'ADJ': 0.0, 'V': 0.0, 'ADV': 0.0, 'DT': 0.0, 'P': 0.0}}

EP = {'N' : {'the':0.0,'cook':0.1,'prepares':0.0,'a':0.0,'lovely':0.0,'drink':0.2},
      'V' : {'the':0.0,'cook':0.4,'prepares':0.1,'a':0.0,'lovely':0.0,'drink':0.5},
      'ADV':{'the':0.0,'cook':0.0,'prepares':0.0,'a':0.0,'lovely':0.2,'drink':0.0},
      'DT':{'the': 0.3, 'cook': 0.0, 'prepares': 0.0, 'a': 0.4, 'lovely': 0.0, 'drink': 0.0},
      'P': {'the': 0.0, 'cook': 0.0, 'prepares': 0.0, 'a': 0.0, 'lovely': 0.0, 'drink': 0.0},
      'ADJ': {'the': 0.0, 'cook': 0.0, 'prepares': 0.0, 'a': 0.0, 'lovely': 0.0, 'drink': 0.0}}

#TP = transition_probability
#EP = emission_probability

# this function consider all possible combination of states = pow(2,n)
def viterbi(O, Q, SP, TP, EP):    
    #a set that hold the final best probable path for the list of observations (max alpha)
    T = {}
    
    #for every possible state in Q
    for q in Q:
        #get probability of each starting state, create a tuple(pair of values)
        T[q] = (SP[q], [q]) #example: T[q] = (0.4,['Sunny'])        

    #for every possible observations in O
    for x in O:
        #create a set/dictionary to hold prob. for each observation
        U = {}       

        #for every next state in Q states
        for q_next in Q:

            #initialize max path and max_p
            max_path = None;
            max_p = 0

            #for every state in Q
            for q in Q:

                #set prob and path = prob of each start state
                (prob, path) = T[q]
                
                #calculate prob. of alpha[i,j]
                p = prob * TP[q][q_next] * EP[q_next][x]

                #compare p with default max_p
                if p > max_p:
                    max_p = p;
                    max_path = path+[q_next] #concatenation of paths

            #pick the best path at each alpha
            U[q_next] = (max_p, max_path)
            
        #print(U)    
        T = U

    return(T)

path = viterbi(O, Q, SP, TP, EP)
print(path)

