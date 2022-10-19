def solution(msg):
    '''
    사전에 있는 가장 긴 값 출력하고 없으면 등록
    '''
    answer = []
    # 사전 정의 - ord 아스키코드로 알파벳 판별하려고 했으나 값이 계속 추가됨
    vocab = dict()
    num = 1
    for alphabet in range(ord('A'), ord('Z')+1):
        vocab[chr(alphabet)] = num
        num += 1
    #print(vocab)
    
    msg = list(msg)
    idx = 0
    word = ''
    while idx < len(msg):
        word += msg[idx]
        if word in vocab.keys(): # 단어가 이미 있는 경우
            idx  += 1
            continue
        else: # 단어가 없는 경우 -> vocab에 추가
            vocab[word] = num
            num += 1
            
            # !! 마지막 글자를 제외한 단어는 사전에 있으므로 해당 단어를 answer에 append
            answer.append(vocab[word[:-1]])
            word = ''
    
    answer.append(vocab[word]) # !! 마지막 글자가 남아있음
    return answer