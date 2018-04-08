
class KeyworsUtil(object):

    def getPersonName(self,words, postags):
        numList = []
        nameList = []
        for num in range(len(postags)):
            if postags[num] == 'nh':
                numList.append(num)
                nameList.append(words[num])
        return numList, nameList
