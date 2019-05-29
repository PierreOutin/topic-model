SENDER_TYPES = ["VISITOR", "BOT"]
TYPES = ["MAIL", "CHAT"]

class Message:

    def __init__(self, content=None, date=None, senderType=None):
        self.content = content
        self.date = date
        self.senderType = senderType

class Discution:

    def __init__(self, visitorName=None, type=None):
        self.type = type
        self.visitorName = visitorName
        self.messages=[]

    def addMessage(self, message):
        self.messages.append(message)


    def getVisitorsMail(self):
        if self.type == "CHAT":
            return []
        else:
            return [self.messages[0].content]

    def getVisitorsQuestions(self):
        if self.type == "MAIL":
            return []
        else:
            questions = []
            for message in self.messages:
                if len(message.content) != 0 and message.senderType == "VISITOR" and (
                        "?" in message.content or "pouvez vous" in message.content.lower() or "comment" in message.content.lower() or "pourquoi" in message.content.lower() or "je recherche" in message.content.lower()):
                    if "baise" not in message.content or "gay" not in message.content or "batard" not in message.content or "merde" not in message.content or "enculer" not in message.content or "coke" not in message.content or "pd?" not in message.content:
                        questions.append(message.content)
            return questions

    def getVisitorsQuestionsWithAnswer(self):
        if self.type == "MAIL":
            return []
        else:
            questions = []
            for i in range(len(self.messages)):
                message = self.messages[i]
                if i < len(self.messages) - 1 and len(message.content) != 0 and message.senderType == "VISITOR" and (
                        "?" in message.content or "pouvez vous" in message.content.lower() or "comment" in message.content.lower() or "pourquoi" in message.content.lower() or "je recherche" in message.content.lower()):
                    question = message.content
                    j = i + 1
                    while j < len(self.messages) and self.messages[j].senderType == "VISITOR":
                        j = j + 1
                    while j < len(self.messages) and self.messages[j].senderType == "BOT":
                        question += self.messages[j].content
                        j = j + 1
                    questions.append(question)
            return questions

def getAllVisitorsQuestions(discutions):
    questions = []
    for d in discutions:
        questions += d.getVisitorsQuestions()
    return questions

def getAllMails(discutions):
    questions = []
    for d in discutions:
        questions += d.getVisitorsMail()
    return questions

def getAllVisitorsQuestionsWithAnswer(discutions):
    questions = []
    for d in discutions:
        questions += d.getVisitorsQuestionsWithAnswer()
    return questions

if __name__ == "__main__":
    from parser1 import *
    from main import *
    p = Parser()
    p.convertToJSON("rawData/resultat1.txt", "jsonData/result.json")
    #p.openFromJSON("jsonData/result.json")
    #qa = getAllVisitorsQuestions(discutions)
    #questionsv2=open("questionv2.csv","w",errors="ignore",encoding='utf-8')
    #for i in qa:
    #questionsv2.write(i+"\n")



