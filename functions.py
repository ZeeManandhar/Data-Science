# 1. Functions

# A function is a block of code that:

# Has a name
# Does one specific task
# Can be used again and again
# In simple words, A function is a reusable piece of code.

# 2. Why Functions Are Needed:

# Code repetition
# Without functions, we have to repeat the same logic many times.
# Example (no function):

print("Hello User!")
print("Hello User!")
print("Hello User!")

# If later we want to change "Welcome" to "Hello" later, we must change it everywhere.

def welcome():
    return "Hello User!"

result = welcome()
print(result)

# 3. Real-Life Analogy

# Take Example of a washing machine:
# We put clothes (input)
# Machine washes (process)
# Clean clothes come out (output)

# A function works the same way:
# Input (optional)
# Logic inside
# Output (optional)

