# Right now the make_decision function always decides to go left
def make_decision(L1, L2, L3, L4):
	option_1 = L3 + L4
	option_2 = L1 + L2

	result = "R"

	if option_1 < option_2:
		result = "L"
	else:
		result = "R"

	return result

##Test for correctness 
def test_make_decision():
	#start by initializing this to 0
	number_correct = 0

	# Test 1, should return "r" since left path has
	# length 5, which is > left path with length 8
	length_1 = 2
	length_2 = 3
	length_3 = 4
	length_4 = 4



	decision = make_decision(length_1, length_2, length_3, length_4)

	if decision == "R":
		# Test 1 passes
		number_correct = number_correct + 1

		# Test 2, should return "L" since right path still 
		# has length 5 but left is only 3
		length_3 = 1
		length_4 = 2

		decision = make_decision(length_1, length_2, length_3, length_4)
		if decision =="L":
			#Test 2 passes
			number_correct = number_correct +1

		if number_correct == 2:
			all_correct = True
		else:
			all_correct = False

	if test_make_decision():
		print("Nice work! Your function passed both test cases.")
	else:
		print("Not quite. Your function didn't pass both test cases")