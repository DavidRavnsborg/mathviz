There is a block sorting game with the following rules:
* Blocks are all the same size.
* Blocks all have a colour, and blocks of the same colour are identical and indistinguishable from one another.
* Blocks must always be stacked on a tower, each taking up one unit of stackable height.
* There are a finite number of block colours, represented by $c$.
* There are a finite number of blocks per colour $n$.
* The maximum stackable height of each tower (in stackable units) is represented by $h$, where $h \ge n$.
* There are a finite number of towers $k$ where $k \ge c+1$ to ensure the game is solvable.
* The top block of a stack can be moved to the top of another tower's stack. A block will settle so it is immediately above the next highest block on the stack.
* There are no empty spots on towers in-between blocks as the only empty spots that can exist are above other stacks of blocks or on empty towers.
* The goal of the game is to get each set of blocks of the same colour together on a tower, isolated from the other blocks.
* The blocks start randomly sorted, though if the game were to start in a victory condition, the blocks will be re-sorted randomly instead.