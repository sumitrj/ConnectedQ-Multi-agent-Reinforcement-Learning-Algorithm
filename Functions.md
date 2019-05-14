<b> <u> Penalty Function: </b> </u>

Penalty = mean of distances travelled by each bot where divided by the diagonal length.

	Penalty(L1,L2):
		S = 0
		for i in range(length(L1)):
			S + = DistanceBeteenPoints ( L1 [i] , L2[i] )
		S = S / length(L1)
		return S/Di # Di = Diagonal Length
    
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

