#14.最长公共前缀
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        if "" in strs:
            return ""
        if len(set(strs)) == 1:
            return first_word
        prefixs = ""
        for i,prefix in enumerate(first_word):
            for word in strs[1:]:
                if len(word) < i+1:
                    return prefixs
                if word[i] != prefix:
                    return prefixs
            prefixs = prefixs + prefix
        return prefixs