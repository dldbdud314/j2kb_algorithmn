from collections import deque

class Solution:              
    def wordBreak(self, s, wordDict):
        def build_trie(words):
            trie = {}
            for word in words:
                cur_root = trie
                for i in range(len(word)):
                    cur_char = word[i]
                    if not cur_char in cur_root:
                        cur_root[cur_char] = {}
                    cur_root = cur_root[cur_char]
                cur_root['*'] = word
            return trie
    
        def search_dfs(string, trie):
            root_dict = trie
            sstring = ''
            queue = deque(string)
            while queue:
                cur_char = queue.popleft()
                if cur_char not in root_dict:
                    return False
                root_dict = root_dict[cur_char]
                if '*' in root_dict:
                    sstring += root_dict['*']
                    root_dict = trie #다시 root로
            print(sstring)
            return string == sstring
        
        trie = build_trie(wordDict)
        return search_dfs(s, trie)
      
solution = Solution()
print(solution.wordBreak("aaaaaaa", ["aaaa", "aaa"]))

#to fix..
#testcase: "aaaaaaa", ["aaaa", "aaa"]