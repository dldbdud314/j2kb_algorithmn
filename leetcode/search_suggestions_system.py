class Solution:
    def suggestedProducts(self, products, searchWord):
        def buildTrie(list):
            trie = {}
            for cur_word in list:
                cur_root = trie
                for c in cur_word:
                    if c not in cur_root:
                        cur_root[c] = {}
                    cur_root = cur_root[c]
                cur_root['*'] = cur_word
            return trie
            
        def DFSAlg(cur_root, res):
            for key, val in cur_root.items():
                if key == '*':
                    res.append(val)
                    continue
                DFSAlg(val, res)
        
        def searchDFS(target, trie):
            root_dict = trie
            res = []
            for x in target:
                if x not in root_dict:
                    return [];
                root_dict = root_dict[x]
            DFSAlg(root_dict, res)
            return res
            
        products.sort()
        new_trie = buildTrie(products)
        res = []
        for i in range(1, len(searchWord)+1):
            candidates = searchDFS(searchWord[0:i], new_trie)
            res.append(candidates[0:3] if len(candidates) > 3 else candidates)
        return res
    
solution = Solution()
print(solution.suggestedProducts(["bags","baggage","banner","box","cloths"], "bags"))