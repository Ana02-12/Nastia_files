from typing import List
def longestCommonPrefix(self, strs: List[str]) -> str:
    pattern = strs[0]
    for i_ch, ch in enumerate(pattern):
        for nexts in strs[1:]:
            if i_ch == len(nexts) or nexts[i_ch] != ch:
                return pattern[:i_ch]
    return pattern

