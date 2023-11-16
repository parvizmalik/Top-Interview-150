class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter out non-alphanumeric characters and convert to lowercase
        filtered_chars = [char.lower() for char in s if char.isalnum()]

        # Compare the list with its reverse
        return filtered_chars == filtered_chars[::-1]




class Solution:
    def isPalindrome(self, s: str) -> bool:
    	i, j = 0, len(s) - 1
    	while i < j:
		a, b = s[i].lower(), s[j].lower()
    		if a.isalnum() and b.isalnum():
			if a != b:
    			    return False
    			else:
				i, j = i + 1, j - 1
    				continue
    		i, j = i + (not a.isalnum()), j - (not b.isalnum())
    	return True
