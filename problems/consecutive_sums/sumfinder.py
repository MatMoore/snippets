"""
Find the maximum sum possible from picking a contiguous subsequence of an array.
"""
def solve_list(intarray):
	"Return the actual elements that make up the solution"
	if not intarray:
		return []

	current_sum = intarray[0]
	current_start = 0
	current_end = 0
	highest_sum = current_sum
	highest_start = current_start
	highest_end = current_end

	for num in intarray[1:]:
		current_end += 1

		# Add the new element
		if current_sum <= 0:
			# The preceeding elements were useless to us
			current_start = current_end
			current_sum = num
		else:
			# Keep the preceeding elements
			current_sum += num

		# Compare to previous highest sums that we have ruined by trying to add
		# more elements
		if current_sum > highest_sum or \
				(
					# When there are multiple solutions, prefer the shortest ^_^
					current_sum == highest_sum
					and highest_end - highest_start > current_end - current_start
				):
			highest_sum = current_sum
			highest_start = current_start
			highest_end = current_end

	return intarray[highest_start : highest_end + 1]

def solve(intarray):
	"Return the highest consecutive sum"
	chosen_elements = solve_list(intarray)
	return sum(chosen_elements) if chosen_elements else None
