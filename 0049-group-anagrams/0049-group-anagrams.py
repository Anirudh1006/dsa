class Solution(object):
    def sort_string(self, s):
        chars = list(s)
        chars.sort()
        return "".join(chars)

    def groupAnagrams(self, strs):
        dict1 = {}

        for s in strs:
            key = self.sort_string(s)

            if key in dict1:
                dict1[key].append(s)
            else:
                dict1[key] = [s]

        return list(dict1.values())
        