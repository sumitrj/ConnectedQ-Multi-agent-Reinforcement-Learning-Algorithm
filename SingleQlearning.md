
## Q Learning for single agent:

1. An agent starts from a start state, makes a number of transitions from its current state to a next state based on its choice of action and also the environment the agent is interacting in. 

2. At every step of transition, the agent from a state takes an action, observes a reward from the environment, and then transits to another state. 

3. If at any point of time the agent ends up in one of the terminating states that means there are no further transition possible. This is the condition of completion of an <u> episode. </u>

While transiting states, it is vital to have a notion of the reward which could be obtained in the furture transitions after completion of the current transition, hence providing a metric of the quality of the current transition.

<b> This is achieved by the Value matrix. </b>

By definition, 
<b> V[x] = Quality of transitions from State x. </b>
