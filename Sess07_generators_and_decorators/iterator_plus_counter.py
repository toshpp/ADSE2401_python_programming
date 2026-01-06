# python script to demonstrate a custom iterator

class PlusCounter:
    """
    A simple iterator that counts up from a stating number to an end number
    incrementing it by a specific number (default to 1)
    Attributes
    current(int): the current value in the iteration
    end(int): the end/maximum value (inclusive) the counter should reach .
    step(int):the value which to increment the counter on each iteration
    """

    def __init__(self, start, end, step=1):

        """
        Initialize the plus counter object/instance
        Args:
            start(int): the starting value for the counter
            end(int): the ending value for the counter
            step(int): the step value for the counter


        """
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        """

        :returns the iterator object itself
        returns:
            plusCounter:Yhe iterator object/instance
        """
        return self

    def __next__(self):
        """

        :returns the next value in the iterator (or next number in the sequence)
        Raises:
            StopIteration:If the current value is greater than the end value

        Returns:
            int: The next value in the iterator/sequence
        """
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += self.step
            return self.current - 1


# create/instantiate a plusCounter object
my_counter1 = PlusCounter(1, 10)

# iterate over the counter object
for num in my_counter1:
    print(num)
print("\n")

# create/instantiate another plusCounter object to give the multiples of 5 from 1-75
my_counter2 = PlusCounter(1, 75, 5)

# iterate over the counter2 object
for num in my_counter2:
    print(num)
