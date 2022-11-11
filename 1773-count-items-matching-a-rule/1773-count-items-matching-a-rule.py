class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        count = 0
        keyIdx = 0 if ruleKey == "type" else 1 if ruleKey == "color" else 2
        for item in items:
            count += 1 if item[keyIdx] == ruleValue else 0
        return count