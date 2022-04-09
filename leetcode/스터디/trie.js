/*
Trie Data Structure

Trie => Dictionary => fast search => words
DFS search

['cat', 'cats', 'dog', 'dogs', 'app', 'application']

{
    'a' : {
        'p' : {
            'p' : {
                '*' : "app",
                'l' : {...}
            }
        }
    },
    'c' : {
        'a' : {
            't' : {
                '*' : "cat",
                's' : {
                    '*' : "cats"
                }
            }
        }
    }
}
time complexity : O(N * M) => N: number of elements of list, M: length of longest word in the list
*/

const list = ["cat", "cats", "dog", "dogs", "app", "application"];

const solution = (list, val) => {
  const trie = {};
  const newTrie = buildTrie(list, trie);
  return searchDFS(newTrie, val);
};

const buildTrie = (list, trie) => {
  if (!list.length) return {};
  for (let l = 0; l < list.length; l++) {
    const currentWord = list[l];

    let currentRoot = trie;
    for (let c = 0; c < currentWord.length; c++) {
      const currentChar = currentWord[c];
      if (!currentRoot[currentChar]) {
        currentRoot[currentChar] = {};
      }
      currentRoot = currentRoot[currentChar];
    }
    currentRoot["*"] = currentWord;
  }
  return trie;
};

const searchDFS = (trie, target) => {
  let rootDict = trie;

  const result = [];

  for (let i = 0; i < target.length; i++) {
    const curTargetChar = target[i];
    if (!rootDict[curTargetChar]) return [];
    rootDict = rootDict[curTargetChar];
  }
  console.log("searchDFS -> ", rootDict);
  DFSAlg(rootDict, result);
  return result;
};

const DFSAlg = (curRoot, result) => {
  console.log("DFSAlg -> ", curRoot);
  for (let [key, val] of Object.entries(curRoot)) {
    if (key === "*") {
      result.push(key);
      continue;
    }
    DFSAlg(val, result);
  }
};

console.log(solution(list, "app"));
