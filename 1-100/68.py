class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        if not words:
            return []
        ans = []
        i = 0
        lengh = len(words)
        while i < lengh:
            begin = i
            tmp = words[begin]
            i += 1
            if i < lengh:
                tmpl = len(words[begin]) + len(words[i]) + 1
                while tmpl <= maxWidth and i < lengh:
                    i += 1
                    if i < lengh:
                        tmpl = tmpl + 1 + len(words[i])
                if i < lengh:
                    tmpl = tmpl - 1 - len(words[i])
            else:
                tmpl = len(words[begin])
            spacenum = maxWidth - tmpl
            nums = i - begin - 1
            #print(nums,begin,i,tmpl)
            if nums == 0:
                # print(i,lengh,begin,words[begin])
                ans.append(words[begin]+' ' * spacenum)
            else:
                if i < lengh:
                    nums1 = spacenum // nums + 1
                    nums2 = spacenum % nums
                    for d in range(begin+1, begin+nums2+1):
                        tmp += ' ' * (nums1 + 1) + words[d]
                    for d in range(begin+nums2+1, i):
                        tmp += ' ' * nums1 + words[d]
                    ans.append(tmp[:])
                else:
                    for d in range(begin+1, i):
                        tmp += ' ' + words[d]
                    tmp += ' ' * spacenum
                    ans.append(tmp[:])
            # print(i, tmp[:])
        return ans