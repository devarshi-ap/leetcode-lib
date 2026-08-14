class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        myNums = []
        
        # for-loop emulates stream
        for x in range(1, n+1):
            print(x, myNums, target)
            if myNums == target:
                return operations # we have match, stop
            else:
                operations.append("Push")
                myNums.append(x)
                if x not in target: # "scratch that"
                    operations.append("Pop")
                    myNums.pop()
        
        return operations


        """
        target = [1,2]
        exp = [1,2,3,4]
            1 in target -> push
            2 in target -> push
            (if at any point, we match target, stop)
            no need to: 3 not in target -> push, pop
            no need to: 4 not in target -> push, pop
        result = [push, push, push, pop, push, pop]
        """