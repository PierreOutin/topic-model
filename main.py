from parser1 import *

p = Parser()
#p.convertToJSON("rawData/resultat1.txt", "jsonData/result.json")
discutions = p.openFromJSON("jsonData/result.json")
print("nombre de discutions (mail et conversations)",len(discutions))

questions = getAllVisitorsQuestions(discutions)

print("nombre de questions : ",len(questions))

mails = getAllMails(discutions)


print("nombre de mails : ",len(mails))

questionsanswers= getAllVisitorsQuestionsWithAnswer(discutions)
print("nombre de questions, reponses: ",len(questionsanswers))



