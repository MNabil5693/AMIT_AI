def fac_1(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return n*fac_1(n-1)



def isprime(num):
    for i in range(2, num):
        if num % i ==0:
            return False
    return True



def word_counter(words):
    uni_words=set(words)
    for words in uni_words:
        print(f"{words}:{words.count(words)}")