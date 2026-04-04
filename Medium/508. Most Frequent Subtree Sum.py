class Solution:
    def findFrequentTreeSum(self, root):
        from collections import defaultdict
        
        freq = defaultdict(int)
        self.maxFreq = 0
        
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            total = node.val + left + right
            
            freq[total] += 1
            self.maxFreq = max(self.maxFreq, freq[total])
            
            return total
        
        dfs(root)
        
        return [s for s in freq if freq[s] == self.maxFreq]
