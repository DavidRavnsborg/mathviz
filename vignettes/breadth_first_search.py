def breadth_first_search(n):
    """ Create a state space graph one step at a time,
	using a deqeue (because deque.popleft runs in 
	O(1), whereas list.pop() runs in O(n)).
	
	Intuitively, this works by building up the state
	space 1 layer deep at a time, then testing that 
	state space. Any states leading to a longer series 
	of steps will be cut off when the shortest path
	through the state space returns. This also means
	it is possible that another unfinished route in 
	the state space can make it to 1 in the same number
	of steps.
	
	I did use a LLM to suggest BFS. But I do not 
	implement LLM code blindly without understanding
	it first, nor do I input details of sensitive 
	project work into another company's LLM.
"""
    visited = set()
    # The deque stores tuples of (number, steps_taken)
    queue = deque([(n, 0)])  

    while queue:
        current, steps = queue.popleft()
        
        # If we reach 1, return the number of steps
        if current == 1:
            return steps

        # Mark the current number as visited
        visited.add(current)

        # Add next numbers to queue
        if current + 1 not in visited:
            queue.append((current + 1, steps + 1))
            visited.add(current + 1)

        if current - 1 > 0 and current - 1 not in visited:
            queue.append((current - 1, steps + 1))
            visited.add(current - 1)

        if current % 2 == 0:
            next_val = current // 2
            if next_val not in visited:
                queue.append((next_val, steps + 1))
                visited.add(next_val)
                

def solution(n):
    n = int(n)
    return breadth_first_search(n)