from model import *
import json
import codecs


class Parser:

    def splitChat(self, chatLine, visitorName):
        date = chatLine[:21]
        splitted = chatLine[21:].split(":")
        sender = splitted[0]
        content = ":".join(splitted[1:])
        if sender.strip() == visitorName.strip():
            return Message(content=content, date=date, senderType="VISITOR")
        else:
            return Message(content=content, date=date, senderType="BOT")

    def parse(self, filename):
        results = []
        currentDiscution = Discution()
        f = open(filename, 'r', encoding='utf-8', errors='ignore').readlines()
        i = 0
        while i < len(f):
            line = f[i]

            if line[:12] == "Visitor Name":
                currentDiscution.visitorName = line[13:]

            if line[:7] == "Browser":
                i += 1
                if f[i][:8] == "Message:":  # MAIL TYPE
                    currentDiscution.type = "MAIL"
                    content = f[i][8:]
                    i += 1
                    while f[i][:10] != "==========":
                        content = content + f[i]
                        i += 1
                    message = Message(content=content)
                    message.content = message.content.rstrip()
                    currentDiscution.addMessage(message)
                else:  # CHAT TYPE
                    currentDiscution.type = "CHAT"
                    while f[i][:10] != "==========":
                        rawMsg = f[i]
                        while f[i+1][0] != "(" and f[i+1][:10] != "==========" and i+1 < len(f):
                            i+=1
                            rawMsg+= f[i]
                        message = self.splitChat(rawMsg, currentDiscution.visitorName)
                        message.content = message.content.rstrip()
                        currentDiscution.addMessage(message)
                        i += 1
                ## IN BOTH CASES -> append the discution result and recreate empty Discution object
                results.append(currentDiscution)
                currentDiscution = Discution()
            i += 1
        return results

    def convertToJSON(self, input, output):
        obj = self.parse(input)
        with codecs.open(output, 'w', encoding='utf-8') as f:
            json.dump(obj, f, default=lambda x: x.__dict__, indent=4, ensure_ascii=False)

    def openFromJSON(self, jsonFile):
        result = []
        with open(jsonFile, encoding='utf-8', errors='ignore') as json_file:
            data = json.load(json_file)
            for dd in data:
                discution = Discution(type = dd['type'], visitorName=dd["visitorName"])
                for m in dd['messages']:
                    message = Message(content=m['content'], date=m['date'], senderType=m['senderType'])
                    discution.addMessage(message)
                result.append(discution)
        return result


