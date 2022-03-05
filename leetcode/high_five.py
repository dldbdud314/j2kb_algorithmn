def getTopFiveAvg(items):
    score_dict = {}
    for id, score in items:
        try:
            score_dict[id].append(score)
        except:
            score_dict[id] = [score, ]
 
    answer = []
    for key in score_dict.keys():
        score_dict[key].sort(reverse = True)
        answer.append([key, sum(score_dict[key][:5])//5])
    
    return answer
    
print(getTopFiveAvg([[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]))