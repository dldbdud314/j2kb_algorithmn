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

const list = ["cat", "cats", "dog", "dogs", "app", "apple", "application"];

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

//그래서 얘가 리턴하는건? target에 대하여 가능한 모든 후보 리스트
const searchDFS = (trie, target) => {
  let rootDict = trie;

  const result = [];

  for (let i = 0; i < target.length; i++) {
    const curTargetChar = target[i];
    if (!rootDict[curTargetChar]) return [];
    rootDict = rootDict[curTargetChar];
  } //여기까진 target search가 끝났구나 -> "app"
  DFSAlg(rootDict, result); //result 반영이 어떻게 되는거지?! 반환이 잘 안 그려진다
  return result;
};

//target의 하위에 해당하는 모든 단어를 모아준다 -> "app..."
const DFSAlg = (curRoot, result) => {
  for (let [key, val] of Object.entries(curRoot)) {
    if (key === "*") {
      //end of word
      result.push(val);
      continue;
    }
    DFSAlg(val, result);
  }
};

console.log(solution(list, "app")); //target = "app"(검색어)
