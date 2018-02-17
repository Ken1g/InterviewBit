class Solution():
	
	class TrieNode(object):

		def __init__(self, char: str):
			self.char = char
			self.children = []
			self.word_finished = False
			self.counter = 1

	def add(self, root, word):
		node = root
		for char in word:
			found_in_child = False
			for child in node.children:
				if child.char == char:
					child.counter += 1
					node = child
					found_in_child = True
					break
			if not found_in_child:
				new_node = self.TrieNode(char)
				node.children.append(new_node)
				node = new_node
		node.word_finished = True

	def find_prefix(self, root, prefix):
			node = root
			if not root.children:
				return 0
			for char in prefix:
				char_not_found = True
				for child in node.children:
					if child.char == char:
						char_not_found = False
						node = child
						break
				if char_not_found:
					return 0
			return node.counter


	def prefix(self, A):
		root = Solution.TrieNode("*")
		for word in A:
			self.add(root, word)
		ans = []
		for word in A:
			length_of_str = 1
			while True:
				string = word[:length_of_str]
				if self.find_prefix(root, string) == 1:
					ans.append(string)
					break
				length_of_str += 1

		return ans





sol = Solution()
A = ["zebra", "dog", "duck", "dove"]
print(sol.prefix(A))