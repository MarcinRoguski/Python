with open('gaming.txt', 'r', encoding = "UTF-8") as file:
    text = str(file.read().splitlines())

newText = text.replace("\n", "")

print(newText)

'''
with open('gaming.txt','r') as file:
    text = file.readlines()
 
text = [line.replace('\n', '') for line in text]
text = [line for line in text if len(line) > 0]
print(text)

'''
    
