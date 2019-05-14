## Propsed Version of Q - Learning Algorithm

<b> <u> Representation of state of the system </b> </u>

In order to incorporate notion of Cooperative Multi Agent System,  We need to change the way we define the state of the system.

Let L = (B1,B2,B3 .... BM) be a tuple of length 'M' such that B1, B2 , B3 are the locations of Bot1, Bot2, Bot3 at a given instant.
<b>
L represents the state of the system.
</b>
Set of all possible states of a system gives the state space. 
An indexed state space is considered where different permutation is given a different index.
<b>
StateSpace = [ L.0, L.1 , L.2, L.3, L.4, ...... L.(P(N,M)-1) ]
</b>
In this case, the length of state space can be given by P(N,M) where P(N,M) returns the number of permutations of arranging N items in M places without repetation.

<b><u> State : Action : Reward </b></u>

Let the bots change locations from Li to Lj. 
This implies that the system has <b> performed an action </b> such that the <b> state of the system </b> changed from Si = Li to Sj = Lj.

For each action, the agent receives a <b> penalty </b>  as given by the <b> penalty function</b>.
