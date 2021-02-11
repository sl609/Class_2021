def test_blood_test():
	from blood_test import analyze_HDL
	answer = analyze_HDL(65)
	expected = "Normal"
	assert answer == expected	