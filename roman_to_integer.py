# Problem found & solved on Leetcode: https://leetcode.com/problems/roman-to-integer/submissions/

class Solution(object):
	def romanToInt(self, s):
		"""
			Given a string of Roman numerals, uses two nested recursion functions to return
		the equivalent in Arabic numberals.

		:type s: str
		:rtype: int

		>>> Solution.romanToInt("I")
		1

		>>> Solution.romanToInt("CDXLIV")
		444

		>>> Solution.romanToInt("xcix")
		99

		>>> Solution.romanToInt("LMNOP")
		ValueError('Input is not a Roman numeral.')

		>>> Solution.romanToInt(777)
		ValueError('777 is not a string.')

		"""

		romanDict = {
			"I": 1,
			"IV": 4,
			"V": 5,
			"IX": 9,
			"X": 10,
			"XL": 40,
			"L": 50,
			"XC": 90,
			"C": 100,
			"CD": 400,
			"D": 500,
			"CM": 900,
			"M": 1000
		}


		def _romanToInt(string, result=[]):
			"""
			"""

			if not string:
				return result

			if string[0] in romanDict:
				if string[:2] in romanDict:
					val = romanDict[string[:2]]
					rest = string[2:]
				else:
					val = romanDict[string[0]]
					rest = string[1:]

				result.append(val)
				return _romanToInt(rest, result)

			else:
				raise ValueError('Input is not a Roman numeral.')

			return result


		def _addRecursively(lst, num=0):
			"""
				Given a list of integers, returns the sum of the list.

			>>> _addRecursively([1, 2, 3], 0)
			6

			>>> _addRecursively([0], 0)
			0

			>>> _addRecursively([7, 6, 5, 4, 7, 8, 9], 0)
			46

			"""

			if not lst:
				return num

			num += lst[0]
			return _addRecursively(lst[1:], num)



		if not isinstance(s, str):
			raise ValueError("{} is not a string".format(s))
		finalNum = list(_romanToInt(s.upper(), result=[]))

		finalNum = _addRecursively(finalLst)

		return finalNum


