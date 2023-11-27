def get_count(sentence):
    #pass
    cnt = 0
    for stcs in sentence:
        if stcs == 'a' or stcs == 'e' or stcs == 'i' or stcs == 'o' or stcs == 'u':
            cnt = cnt + 1
    return cnt