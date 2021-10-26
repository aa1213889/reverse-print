f = open('reverse-print.js', 'w', encoding='utf-8')


def numParse(num):
    strNum = str(num)
    strLen = len(strNum)
    text = '    case ' + strNum + ':\n'
    text += '      console.log(`是' + str(strLen) + '位数`)\n'
    for i in range(0, strLen):
        text += '      console.log(`第' + str((i+1)) + \
            '位数是' + strNum[i:i+1] + '`)\n'
    text += '      console.log(`倒过来是' + strNum[::-1] + '`)\n'
    text += '      break\n'
    return text


def joinChar(maxNum):
    startText = 'function reverse(num) { \n   switch(num){\n'
    numText = ''
    for i in range(0, maxNum):
        numText += numParse(i)
    endText = '\n }\n}\n\nreverse(233)'
    return startText + numText + endText


# 控制枚举的数量
f.write(joinChar(100000))
f.close()
