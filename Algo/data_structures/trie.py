#from typing import Tuple

class TrieNode(object):

	def __init__(self, char: str):
		self.char = char
		self.children = []
		# is the word finished?
		self.word_finished = False
		# how many times this character appeared in the additional process
		self.counter = 1


def add(root, word: str):
	"""
	Adding a word in the trie structure
	"""
	node = root
	for char in word:
		found_in_child = False
		# search for the character in the children of the node
		for child in node.children:
			if child.char == char:
				#found
				child.counter += 1
				node = child
				found_in_child = True
				break
		if not found_in_child:
			new_node = TrieNode(char)
			node.children.append(new_node)
			# point the node to the new child
			node = new_node
	node.word_finished = True

def find_prefix(root, prefix: str): #-> Tuple[bool, int]
		'''
		Check and return
		1. If the prefix exists in any of the words we added
		2. If yes then how many words actually have the prefix
		'''
		node = root
		# If the root contains no children return False
		if not root.children:
			return False, 0
		for char in prefix:
			char_not_found = True
			# search through all the children of the present node
			for child in node.children:
				if child.char == char:
					# found
					char_not_found = False
					node = child
					break
			if char_not_found:
				return False, 0
		return True, node.counter

root = TrieNode("*")
add(root, "dog")
add(root, "word")
print(find_prefix(root, "dog"))
print(find_prefix(root, 'word'))

