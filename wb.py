# Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

# Each letter in the magazine can only be used once in ransomNote.

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true


def solution(ransomNote, magazine):
    for i in ransomNote:
        if i in magazine: 
            magazine.count(i) == ransomNote.count(i)
            return True
        else:
            return False
            

print(solution('a', 'b'))
print(solution('aabbcc', 'aab'))