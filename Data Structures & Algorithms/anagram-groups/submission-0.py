class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # to group all anagrams together into each sublist, we need to have a "common ground" for each group
        # one way to do that is to have a *normalized* word of each group (since all words in each group anagram will contain the exact same chars)
        # one way to have a normalized word can be a word that's sorted alphabetically
        # use that word as a key in a dict/hashmap, then as we go through each word in the list we sort that word and compare to the key if it matches, if so then store it as an element in the list as value

        # at the end , return a list of all group anagrams (each group is a sublist)

        grp_anagrams = {}
        for s in strs:
            s_norm = "".join(sorted(s))
            if s_norm not in grp_anagrams:
                grp_anagrams[s_norm] = [s]
            else:
                grp_anagrams[s_norm].append(s)
        
        # now we have a group anagram in terms of hashmap
        # store all values (sublists of anagrams) in the output list
        output = list(grp_anagrams.values())
        return output




