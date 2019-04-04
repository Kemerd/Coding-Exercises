'''

= D. Everett Hinton =

1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other. 

Comments: I saw this, and instead of making something for two strings, I wanted to make it
work for any infinite amount of strings.

Sorry for the messy comments. For these CtCI problems I thought I'd walk through them step by step.

'''

# Define our inputs.
strings = ["string", "strign"]
sum = [0,0]

# Define our main function.
def main():

	# Initial check. If they're not the same length, they're not permutations.
    if len(strings[0]) != len(strings[1]):
        return False
    else:
	
	# A trick for using indexed loops in Python. Loop through our input strings.
        for i, v in enumerate(strings):
		
			# This loops through every character in the string v.
            for k in v:
				# Converts the character to it's ascii equivelant, and add its to a sum given to every string of those ascii values.
                sum[i] += ord(k)
				
			# If it isn't the first in the table, if it isn't equal to the last one, they're not all permutations.
			# Alternatively we could go one up and check if every sum[i] is equal to one another.
            if (i != 0) and (sum[i]!=sum[i-1]):
                return False
				
    # If nothing has proved it wrong yet, it's probably right.
	return True

# Call our main function and print the outcome.
if main():
    print("They are permutations!")
else:
    print("They are not permutations!")
