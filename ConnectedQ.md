## ConnectedQ
#### Proposed alternative of Q Learning for Multi Agent System applied in this use case for Path Planning

<b> <u> Representation of state of the system </b> </u>

In order to incorporate notion of Cooperative Multi Agent System,  We need to change the way we define the state of the system.

Let L = (B1,B2,B3 .... BM) be a tuple of length 'M' such that B1, B2 , B3 are the locations of Bot1, Bot2, Bot3 at a given instant.
<b>

L represents the state of the system.
</b>

Set of all possible states of a system gives the state space. 

An indexed state space is considered where different permutation is given a different index.
<b>

In this case, the length of state space can be given by P(N,M) where P(N,M) returns the number of permutations of arranging N items in M places without repetation.

StateSpace = [ L.0, L.1 , L.2, L.3, L.4, ...... L.(P(N,M)-1) ]
</b>

<b> Input: </b>

<u> Field Parameters </u>

	Coordinates of Target Points:
	P1 [0] ['x'] 
	P1 [0] ['y']
	P1 [1] ['x'] 
	P1 [1] ['y']
	P1 [2] ['x'] 
	P1 [2] ['y']
	...
	P1 [N-1] ['x'] 
	P1 [N-1] ['y'] 
	P1 = [ P1.0, P1.2, P2.2, .... P2.N ]
	
	Location of Bots:
	An M sized sequence from P1

	L = Length of the total Area 
	B = Breadth of the total Area

<u> Algorithm Hyperparameters </u>	

	G = Gamma = Learning Rate
	E = Number of Episodes




<b> <u> State : Action : Reward </b></u>

Let the bots change locations from Li to Lj. 
This implies that the system has <b> performed an action </b> such that the <b> state of the system </b> changed from Si = Li to Sj = Lj.

For each action, the agent receives a <b> penalty </b>  as given by the <b> penalty function</b>.

<b> <u> Penalty Function: </b> </u>

Penalty = mean of distances travelled by each bot where divided by the diagonal length.

	Penalty(L1,L2):
		S = 0
		for i in range(length(L1)):
			S + = DistanceBeteenPoints ( L1 [i] , L2[i] )
		S = S / length(L1)
		return S/Di # Di = Diagonal Length
		

<b> <u> Q Matrix:</b> </u>

As described in the previous section,
Q[State,Action] = Quality of the given transition

In our case, Action is basically transition to a different state ( a different L ).
Hence the Q matrix has the dimension same as length of State Space, P(N,M).

<b> <u> Training </b> </u>

<b> Declarations to be done before begining training </b>

	AllPoints = {} # Set of Target Points (Set P1 as mentioned in problem 	description section)
	Q = Zero Matrix of order P(N,M) x P(N,M)
	scores = []
	policies = []

<b>Functions: </b>

<u>Specially defined functions: </u>

	NextState(Visited): 
		
		p = State index selected at random
		next_state = StateSpace[p]
		
		if( isSubset( set(next_state), Visited) ):
			NextState(Visited) 
		else:
			return next_state
		 
<u> Generic functions: </u>
	
	1. Union(A,B): 
	returns the union of sets A and B
	
	2. isSubSet(A,B) :
	returns 1 if A is subset of B, returns 0 otherwise
	
	3. isSuperSet(A,B):
	returns 1 if A is superset of B, returns 0 otherwise


An episode of training can be described as follows:
	
	TrainEpisode():	
		
		p = State index selected at random
		initial_state = StateSpace[p]
		current_state = initial_state 
		Visited = {} # Set of Visited Points
		Visited = Union( Visited, set( current_state ) )
		policy = [] # Sequence of States forming the policy for the considered episode
		EpisodePenalty = 0
			
		while( isSuperSet ( AllPoints, Visited ) ):
		
			next_state = NextState( Visited )
			policy.append(next_state)
			Visited = Union( Visited , set(next_state) )
			EpisodePenalty = EpisodePenalty + Penalty(current_state, next_state)
			Q[current_state][next_state] = Penalty(current_state, next_state) + G*min(Q[next_state])
			current_state = next_state 
			
		scores.append(EpisodePenalty)
		policies.append(policy)
<b> <u> Implementation </b> </u>

<b> Input: </b>

<u> Field Parameters </u>

	Coordinates of Target Points:
	P1 [0] ['x'] 
	P1 [0] ['y']
	P1 [1] ['x'] 
	P1 [1] ['y']
	P1 [2] ['x'] 
	P1 [2] ['y']
	...
	P1 [N-1] ['x'] 
	P1 [N-1] ['y'] 
	P1 = [ P1.0, P1.2, P2.2, .... P2.N ]
	
	Location of Bots:
	An M sized sequence from P1

	L = Length of the total Area 
	B = Breadth of the total Area

<u> Algorithm Hyperparameters </u>	

	G = Gamma = Learning Rate
	E = Number of Episodes

<b> Training: </b>

	for e in range(E):
		TrainEpisode()

<b> Testing </b>
		
	Initial_State = < As given in the input >
	current_state = Initial_State 
	Visited = {} # Set of Visited Points 
	Visited = Union( Visited, set( current_state ) ) 
	policy = [] # Sequence of States forming the policy for the considered episode
	EpisodePenalty = 0 
		
		while( isSuperSet ( AllPoints, Visited ) ): 
			next_state = NextStatebyQ(current_state) 
			policy.append(next_state) 
			Visited = Union( Visited , set(next_state) ) 
			EpisodePenalty = EpisodePenalty + Penalty(current_state, next_state)
		scores.append(EpisodePenalty) 
		policies.append(policy)
	
	NextStateByQ(Initial_State):
		s = 0
		for i in range ( length ( Q[Initial_State] ) ):
			if(Q[Initial_State][i]<Q[Initial_State][m]):
				s = i
		return StateSpace[s]
		
