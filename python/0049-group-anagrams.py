class Solution(object):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    def groupAnagrams(self, strs):
        groups = {}

        for string in strs:
            sorted_string = ''.join(sorted(string))

            print(sorted_string)

            if (sorted_string not in groups):
                groups.update({sorted_string: [string]})
                continue

            groups.get(sorted_string).append(string)

        array_groups = [group for group in groups.values()]
        return array_groups
