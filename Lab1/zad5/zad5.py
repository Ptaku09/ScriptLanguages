import wikipedia

query = input("Enter search query: ")
print(wikipedia.page(query).url)
print(wikipedia.summary(query))