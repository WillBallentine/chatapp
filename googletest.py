#test.py

from googlesearch import search

google_search = 'cats'
google_search2 = str(google_search)
google_answer = []
for j in search(google_search2, num_results=1, lang="en"):
	google_answer.append(j)

print(google_answer)