class Stack: 

	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return(self.items.pop())

	def list(self):
		print(self.items)

	def isBalanced(self, symbolString):

		# Resetting previous values
		self.items = []

		# To check if it's an opening character.
		opening = {"(":")", "{":"}", "[":"]"}

		openingCharacter = opening.keys()

		for character in symbolString:

			# If character is an opening character, add to Stack
			if character in openingCharacter:
				self.items.append(character)
			# Else pop and check with last inserted element if it's a match. If not, exit.
			else:
				lastInsertedCharacter = self.items.pop()

				if (opening[lastInsertedCharacter] != character):
					return False

		if (self.items != []):
			return False
		else:
			return True 


stack = Stack()

print(stack.isBalanced("[{(){}}][(){}()]"))