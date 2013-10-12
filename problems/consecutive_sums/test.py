from nose.tools import assert_equal
from sumfinder import solve_list

def test_examples():
	for intarray, solution in (
			([-1, 5, 6, -2, 20, -50, 4], [5, 6, -2, 20]),
			([-1, -2, 20, -50, 4], [20]),
			([-1, -2, 20, 0, 4], [20, 0, 4]),
			([3, -2, 20, 0, 4], [3, -2, 20, 0, 4]),
			([2, -2, 20, 0, 4], [20, 0, 4]),
			([1, -2, 20, 0, 4], [20, 0, 4]),
			([2, -1, 2, -1, 2], [2, -1, 2, -1, 2]),
			([1, -1, 1, -1, 1], [1]),
			([-1, -1, -1, -1, -1], [-1]),
			([1, 3, 1, -5, -5, 2, 3], [2, 3]),
			([], []),
	):
		yield assert_equal, solve_list(intarray), solution
