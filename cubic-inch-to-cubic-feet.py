def inches_to_cubic_inches(d1,d2,d3):
	return d1 * d2 * d3

def cubic_inches_to_cubic_feet(cubic_inches):
	return cubic_inches / (12**3)

def cubic_feet_to_cubic_yards(cubic_feet):
	return cubic_feet / (3**3)

if __name__ == '__main__':

	import sys

	args = sys.argv[1:]

	if len(args) != 1 and len(args) != 3:
		print("Incorrect number of arguments.")

	else:

		if len(args) == 3:

			try:
				d1 = float(args[0])
				d2 = float(args[1])
				d3 = float(args[2])

			except:
				print("Arguments aren't floats.")

			print(f"dimensions: {d1} x {d2} x {d3}")

			cu_in = inches_to_cubic_inches(d1,d2,d3)

		else:

			try:
				cu_in = float(args[0])

			except:
				print("Argument isn't a float.")

		cu_ft = cubic_inches_to_cubic_feet(cu_in)
		cu_yd = cubic_feet_to_cubic_yards(cu_ft)

		print(f"cubic inches: {cu_in:1.3f}")
		print(f"cubic feet: {cu_ft:11.3f}")
		print(f"cubic yards: {cu_yd:10.3f}")

	

