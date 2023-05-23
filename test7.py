num_sentences = int(input())

results = []
for i in range(1, num_sentences+1):
    num_words = int(input())
    
    sentence = input()
    words = sentence.split()
    
    sentence = ''.join(words)
    
    upper_count = 0
    lower_count = 0
    for char in sentence:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
            
    if upper_count == lower_count:
        results.append(f"Sentence #{i}: YES")
    else:
        results.append(f"Sentence #{i}: NO")

for result in results:
    print(result)