"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskSample import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        #'index.html',
        'index.html',
        title='Home Page',
        year=datetime.now().year
    )

@app.route('/ppt1')
def ppt1():
    """Renders the home page."""
    return render_template(
        #'index.html',
        'ppt1.html',
        title='Home Page',
        year=datetime.now().year
    )

@app.route('/ppt2')
def ppt2():
    """Renders the home page."""
    return render_template(
        #'index.html',
        'ppt2.html',
        title='Home Page',
        year=datetime.now().year
    )

@app.route('/ppt3')
def ppt3():
    """Renders the home page."""
    return render_template(
        #'index.html',
        'ppt3.html',
        title='Home Page',
        year=datetime.now().year
    )

@app.route('/ppt4')
def ppt4():
    """Renders the home page."""
    return render_template(
        #'index.html',
        'ppt4.html',
        title='Home Page',
        year=datetime.now().year
    )

@app.route('/feedback')
def feedback():
    """Renders the home page."""
    return render_template(
        #'index.html',
        'feedback.html',
        title='Home Page',
        year=datetime.now().year,
        #text = raw_contents,
        #package = contextPackage
        #chunk = chunk,
        data = data
    )

@app.route('/game')
def game():
    """Renders the home page."""
    return render_template(
        #'index.html',
        'game.html',
        title='Home Page',
        year=datetime.now().year
    )

@app.route('/conclusion')
def conclusion():
    """Renders the home page."""
    return render_template(
        #'index.html',
        'conclusion.html',
        title='Home Page',
        year=datetime.now().year
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
        

    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


####################################################


from konlpy.tag import Kkma
kkma = Kkma()


class attrDic:
    keywordList = []
    attrList = []

    def __init__(self):
        self.keywordList.append('냄새/NNG')
        self.attrList.append(['나/NP'])
        self.keywordList.append('가격/NNG')
        self.attrList.append(['착하/VA'])
        self.keywordList.append('배송/NNG')
        self.attrList.append(['빠르/VA'])

    def isAttr(self, keyword, attr):
        if keyword in self.keywordList:
            i = self.keywordList.index(keyword)
            if i > -1:
                return True
            else:
                return False
        else:
            return False

class ruleDetail:
    r1SCheck = False
    r1ECheck = False
    r2SCheck = False
    r2ECheck = False
    r3SCheck = False
    r3ECheck = False
    r1SList = []
    r1EList = []
    r2SList = []
    r2EList = []
    r3SList = []
    r3EList = []
    ruleDepth = 0
    def __init__(self, rule):
        if len(rule[0][0]) > 0: self.r1SCheck = True
        if len(rule[0][1]) > 0: self.r1ECheck = True
        if len(rule[1][0]) > 0: self.r2SCheck = True
        if len(rule[1][0]) > 0: self.r2ECheck = True
        if len(rule[2][0]) > 0: self.r3SCheck = True
        if len(rule[2][0]) > 0: self.r3ECheck = True

        self.r1SList = rule[0][0]
        self.r1EList = rule[0][1]
        self.r2SList = rule[1][0]
        self.r2EList = rule[1][1]
        self.r3SList = rule[2][0]
        self.r3EList = rule[2][1]

        if self.r3SCheck or self.r3ECheck: self.ruleDepth = 3
        elif self.r2SCheck or self.r2ECheck: self.ruleDepth = 2
        elif self.r1SCheck or self.r1ECheck: self.ruleDepth = 1

class applyRuleReport:
    applyYN = False
    context = []
    packaged= []
    def __init__(self, applyYn, context, packaged):
        self.context = context
        self.packaged = packaged
        self.applyYN = applyYn

class decoRuleCheckResult:
    result = []
    text = '\t'
    length = 0
    target = 'None'
    deco = 'None'
    def __init__(self, result):
        self.result = result
        self.length = len(result)
        for i in range(len(result)):
            if type(result[i]) is chnkDetailT:
                self.text += result[i].text + ' '
            elif type(result[i]) is str:
                self.text += result[i] + ' '

class sumRuleCheckResult:
    processResult = -1
    depth = -1
    def __init__(self, processResult, depth):
        self.processResult = processResult
        self.depth = depth

class applyRule:
    context = []
    decoRuleList = [
        [
            # ['착하/VA', 'ㄴ/ETD']['가격/NNG', '에다/JC']
            [
                [[], ['ETD']]
                , [['NNG'], []]
                , [[], []]
            ]
            , [
                'R1' # R1
                , '>'
                , 'R2' # R2
            ]
        ]
        , [
            # ['화질/NNG', '도/JX']['좋/VA', '고/ECE']
            [
                [['NNG'], ['JKM', 'JX']]
                , [['VA', 'VV'], []]
                , [[], []]
            ]
            , [
                'R1' # R1
                , '<'
                , 'R2' # R2
            ]
        ]
        , [
            # ['배터리/NNG', '가/JKS']['빨리/MAG']['닳/VV', '아서/ECD']
            [
                [['NNG'], []]
                , [['MAG'], []]
                , [['VA', 'VV'], []]
            ]
            , [
                'R1'  # R1
                , '<'
                , 'R2'  # R2
                , '>'
                , 'R3'
            ]
        ]
        , [
            # ['가격/NNG', '도/JX']['저렴/XR', '하/XSA', '고/ECE']
            [
                [['NNG'], []]
                , [['XR'], []]
                , [[], []]
            ]
            , [
                'R1'  # R1
                , '>'
                , 'R2'  # R2
            ]
        ]
    ]

    sumRuleList = [
        # ['좋/VA', '은/ETD']['것/NNB']['같/VA', '아요/EFN']
        # ['하/VV', 'ㄹ/ETD']['수/NNB']['있/VV', '어서/ECD']]
        # ['믿/VV', '을/ETD']['수/NNB']['있/VV', '는/ETD']
        [
            [
                []
                , ['ETD']
            ]
            , [
                ['NNB']
                , ['NNB']
            ]
            , [
                ['VA', 'VV', 'VCN']
                , []
            ]
        ]
        # ['권하/VV', '고/ECE']['싶/VXA', '은/ETD']
        # ['챙기/VV', '어/ECS']['주/VXV', '고/ECE']
        # ['하/VV', '어/ECS']['주/VXV', '시/EPH', '고/ECE']
        # ['나쁘/VA', '지/ECD']['않/VXV', '고/ECE']
        # ['쓰/VV', 'ㄹ/ETD']['만하/VXA', 'ㅂ니다/EFN']
        , [
            [
                []
                , ['ECE', 'ECS', 'ECD', 'ETD']
            ]
            , [
                ['VXA', 'VXV']
                , []
            ]
            , [
                []
                , []
            ]
        ]
        # ['부모님/NNG', '과/JKM']['제가/NNG']
        , [
            [
                ['NNG']
                , ['JKM']
            ]
            , [
                ['NNG', 'NP']
                , []
            ]
            , [
                []
                , []
            ]
        ]
        # ['보내/VV', '었/EPT', '으면/ECD']['하/VV', 'ㅂ니다/EFN']
        , [
            [
                []
                , ['ECD']
            ]
            , [
                ['VV']
                , []
            ]
            , [
                []
                , []
            ]
        ]
    ]

    def __init__(self, context):
        self.context = context

    def decoRuleCheck(self):
        ret = []
        t_ret = []
        for i in range(len(self.decoRuleList)):
            rDetail = ruleDetail(self.decoRuleList[i][0])
            processResult = self.ruleCheckProcess(rDetail)

            if processResult > -1:
                index = processResult
                for j in range(len(self.decoRuleList[i][1])):
                    if self.decoRuleList[i][1][j] == 'R1' or self.decoRuleList[i][1][j] == 'R2' or self.decoRuleList[i][1][j] == 'R3':
                        t_ret.append(self.context.chnkDetailList[index])
                        index += 1
                    elif self.decoRuleList[i][1][j] == '>' or self.decoRuleList[i][1][j] == '<':
                        t_ret.append(self.decoRuleList[i][1][j])
                ret.append(decoRuleCheckResult(t_ret))
                t_ret = []
        return ret

    def sumRuleCheck(self):
        ret = ''
        #t_ret = []
        for i in range(len(self.sumRuleList)):
            rDetail = ruleDetail(self.sumRuleList[i])
            processResult = self.ruleCheckProcess(rDetail)

            if processResult > -1:
                ret = sumRuleCheckResult(processResult, rDetail.ruleDepth)
                break

        return ret

    def ruleCheckProcess(self, rDetail):
        index = -1
        ret = []
        t_ret = []
        for i in range(self.context.length):
            r1SPass = False
            r1EPass = False
            r2SPass = False
            r2EPass = False
            r3SPass = False
            r3EPass = False

            detail = self.context.chnkDetailList[i]
            nextDetail = 'None'
            nextDetail1 = 'None'
            if i < len(self.context.chnkDetailList) - 1:
                nextDetail = self.context.chnkDetailList[i + 1]
            if i < len(self.context.chnkDetailList) - 2:
                nextDetail1 = self.context.chnkDetailList[i + 2]

            if rDetail.ruleDepth == 1:
                if rDetail.r1SCheck:
                    if detail.sTag in rDetail.r1SList: r1SPass = True
                if rDetail.r1ECheck:
                    if detail.eTag in rDetail.r1EList: r1EPass = True

                if r1SPass or r1EPass:
                    index = i
                    break

            if rDetail.ruleDepth == 2:
                if rDetail.r1SCheck:
                    if detail.sTag in rDetail.r1SList: r1SPass = True
                if rDetail.r1ECheck:
                    if detail.eTag in rDetail.r1EList: r1EPass = True

                if r1SPass or r1EPass:
                    if rDetail.r2SCheck:
                        if nextDetail != 'None' and nextDetail.sTag in rDetail.r2SList: r2SPass = True
                    if rDetail.r2ECheck:
                        if nextDetail != 'None' and nextDetail.eTag in rDetail.r2EList: r2EPass = True

                    if r2SPass or r2EPass:
                        index = i
                        break

            if rDetail.ruleDepth == 3:
                if rDetail.r1SCheck:
                    if detail.sTag in rDetail.r1SList: r1SPass = True
                if rDetail.r1ECheck:
                    if detail.eTag in rDetail.r1EList: r1EPass = True

                if r1SPass or r1EPass:
                    if rDetail.r2SCheck:
                        if nextDetail != 'None' and nextDetail.sTag in rDetail.r2SList: r2SPass = True
                    if rDetail.r2ECheck:
                        if nextDetail != 'None' and nextDetail.eTag in rDetail.r2EList: r2EPass = True

                    if r2SPass or r2EPass:
                        if rDetail.r3SCheck:
                            if nextDetail1 != 'None' and nextDetail1.sTag in rDetail.r3SList: r3SPass = True
                        if rDetail.r3ECheck:
                            if nextDetail1 != 'None' and nextDetail1.eTag in rDetail.r3EList: r3EPass = True

                        if r3SPass or r3EPass:
                            index = i
                            break
        return index

class tokenPackageT:
    tokenList = [] # '화질/NNG', '도/JX', '좋/VA', '고/ECE' ...
    length = 0;
    i = 0;

    def __init__(self, tokenList):
        self.tokenList = tokenList # '화질/NNG', '도/JX', '좋/VA', '고/ECE' ...
        self.length = len(tokenList)

    def index(self, i):
        self.i = i
        return self.tokenList[i]

    def nextTag(self):
        if self.i < self.length - 1:
            return self.tokenList[self.i + 1].split('/')[1]
        else:
            return 'None'

class chnkDetailT:
    chnkList = [] # ['가격/NNG', '대비/NNG', '최고/NNG', '에/JKM', '요/JX']
    text = ''
    sToken = ''  # 가격/NNG
    sTag = '' # NNG
    eToken = ''  # 요/JX
    eTag = ''  # JX
    eToken_1 = 'None' # 에/JKM
    eTag_1 = 'None' # JKM
    length = 0;
    i = 0
    def __init__(self, chnkList):
        if len(chnkList) > 0:
            if type(chnkList[0]) is str:
                self.chnkList = chnkList  # ['가격/NNG', '대비/NNG', '최고/NNG', '에/JKM', '요/JX']
                self.text = str(chnkList)
                self.length = len(chnkList)
                self.sTag = chnkList[0].split('/')[1]  # NNG
                self.eTag = chnkList[-1].split('/')[1]  # JX
                self.sToken = chnkList[0]  # 가격/NNG
                self.eToken = chnkList[-1]  # 요/JX
                if len(chnkList) > 1:
                    self.eToken_1 = chnkList[-2]  # 에/JKM
                    self.eTag_1 = chnkList[-2].split('/')[1]  # JKM
            elif type(chnkList[0]) is chnkDetailT:
                for i in range(len(chnkList)):
                    self.chnkList.append(chnkList[i].chnkList)
                    self.text += chnkList[i].text
                    self.length += chnkList[i].length
                self.text = '[' + self.text + ']'
                self.sTag = chnkList[0].sTag
                self.eTag = chnkList[-1].sTag
                self.sToken = chnkList[0].sToken
                self.eToken = chnkList[0].eToken
                if len(chnkList) > 1:
                    self.eToken_1 = chnkList[-2].eToken
                    self.eTag_1 = chnkList[-2].eTag

class chnkPackageT:
    chnkDetailList = []
    length = 0
    i = 0
    text = ''

    def __init__(self, chnkDetailList):
        self.chnkDetailList = chnkDetailList
        self.length = len(chnkDetailList)
        for i in range(len(chnkDetailList)):
            self.text += chnkDetailList[i].text

    def index(self, i):
        self.i = i
        return self.chnkDetailList[i]

    def nextDetail(self):
        if self.i < self.length - 1:
            return self.chnkDetailList[self.i + 1]
        else:
            return 'None'

    def nextDetail1(self):
        if self.i < self.length - 2:
            return self.chnkDetailList[self.i + 2]
        else:
            return 'None'

    def beforeDetail(self):
        if self.i > 0:
            return self.chnkDetailList[self.i - 1]
        else:
            return 'None'

    def beforeDetail1(self):
        if self.i > 1:
            return self.chnkDetailList[self.i - 2]
        else:
            return 'None'

class contextPackageT:
    chnkPackageList = []
    length = 0
    i = 0
    text = ''

    def __init__(self, chnkPackageList):
        self.chnkPackageList = chnkPackageList
        self.length = len(chnkPackageList)
        for i in range(len(chnkPackageList)):
            self.text += chnkPackageList[i].text

    def index(self, i):
        self.i = i
        return self.chnkPackageList[i]

    def nextContext(self):
        if self.i < self.length - 1:
            return self.chnkPackageList[self.i + 1]
        else:
            return 'None'

    def beforeContext(self):
        if self.i < self.length - 1:
            return self.chnkPackageList[self.i + 1]
        else:
            return 'None'

class textAnalyzer:
    text = ""
    tokenized = []
    tagList = []
    eList = ['EPH', 'EPT', 'EPP', 'EFN', 'EFQ', 'EFO', 'EFA', 'EFI', 'EFR', 'ECE', 'ECS', 'ECD', 'ETN', 'ETD']  # 어미
    jList = ['JKS', 'JKC', 'JKG', 'JKO', 'JKM', 'JKI', 'JKQ', 'JC', 'JX']  # 관계언
    vList = ['VV', 'VA', 'VXV', 'VXA', 'VCP', 'VCN']  # 용언
    sList = ['SF', 'SE', 'SS', 'SP', 'SO', 'SW']
    exceptList = ['MAG', 'MAC']

    def __init__(self, text):
        self.text = text
        self.tokenized = self.tokenize()  # '화질/NNG', '도/JX', '좋/VA', '고/ECE' ...
        self.tagList = self.setTagList()  # NNG, JX, VA, ECE ...
        self.chnkPackage = self.setChnkPackage()  # ['화질/NNG', '도/JX']['좋/VA', '고/ECE'] ...
        self.contextPackage = self.setContextPackage()

    def tokenize(self):
        return ['/'.join(t) for t in kkma.pos(self.text)]

    def setTagList(self):
        tagList = []
        for i in range(len(self.tokenized)):
            tagList.append(self.tokenized[i].split('/')[1])
        return tagList

    def setChnkPackage(self): # '화질/NNG', '도/JX' >> ['화질/NNG', '도/JX'] '좋/VA', '고/ECE' >> ['좋/VA', '고/ECE']
        ret = []
        t_ret = []
        tokenPackage = tokenPackageT(self.tokenized)
        for i in range(len(self.tokenized)):
            token = tokenPackage.index(i)
            tag = token.split('/')[1]
            nextTag = tokenPackage.nextTag()

            if tag in self.sList or tag == 'EMO':  # 기호 및 Emoticon 제외
                continue

            t_ret.append(token)
            if nextTag in self.exceptList or nextTag in self.vList:  # MAG나 용언(동사, 형용사) 앞에서 나눔
                if len(t_ret) > 0:
                    ret.append(chnkDetailT(t_ret))
                t_ret = []
            if tag in self.eList or tag in self.jList:  # 어미나 관계언(조사)에서 나눔
                if nextTag in self.eList or nextTag in self.jList:  # 다음 토큰도 어미나 관계언이면 Pass
                    pass
                else:
                    if len(t_ret) > 0:
                        ret.append(chnkDetailT(t_ret))
                    t_ret = []
            if tag in self.exceptList:  # MAG나 기호에서 나눔
                if len(t_ret) > 0:
                    ret.append(chnkDetailT(t_ret))
                t_ret = []

            '''
            if token == '배송/NNG' and nextTag  == 'NNG':
                if len(t_ret) > 0:
                    ret.append(chnkDetailT(t_ret))
                t_ret = []
            '''

        if len(t_ret) > 0:
            ret.append(chnkDetailT(t_ret))
        t_ret = []
        return chnkPackageT(ret)

    def printChnkPackage(self):
        temp_string = ''
        for i in range(self.chnkPackage.length):
            detail = self.chnkPackage.index(i)
            temp_string += detail.text
        print(temp_string)

    def setContextPackage(self):
        t_ret = []
        ret = []

        eList = self.eList[:]  # eList와 self.eList가 동일한 참조를 가져 슬라이싱([:]) 추가
        if 'ETD' in eList:
            eList.pop(eList.index('ETD'))  # ['있/VV', '는/ETD']['브랜드/NNG', '에/JKM']

        detailList = self.chnkPackage
        for i in range(detailList.length):  # chnkDetail(['화질/NNG', '도/JX']), chnkDetail(['좋/VA', '고/ECE']) ...
            detail = detailList.index(i)
            nextDetail = detailList.nextDetail()
            t_ret.append(detail)

            if detail.eTag in eList:  # 기본적으로, 어미로 끝나면 줄나눔
                # if nextDetail != 'None' and nextDetail.sTag in eList:
                # pass
                if type(nextDetail) is chnkDetailT and (nextDetail.sTag == 'VXV' or nextDetail.sTag == 'VXA'):
                    # 어미 + 보조동사는 줄나눔 X : 하/XSV 고/ECE 있/VXV 었/EPT ...
                    # 어미 + 보조형용사는 줄나눔 X : ['권하/VV', '고/ECE'] ['싶/VXA', '은/ETD']
                    pass
                elif detail.eTag == 'ECD' and type(nextDetail) is chnkDetailT and nextDetail.sTag == 'VV':
                    pass
                else:
                    if len(t_ret) > 0:
                        ret.append(chnkPackageT(t_ret))
                    t_ret = []

            ###########################################################################

            '''
            if detail.eToken == '요/JX':  # ~에요(에/JKM, 요/JX)로 끝나면 줄나눔
                if detail.eToken_1 == '에/JKM':
                    if len(t_ret) > 0:
                        ret.append(t_ret)
                    t_ret = []

            if detail.eToken == '하지만/MAC':  # ['콩알/NNG', '만/JX']['하지만/MAC']['과일/NNG', '맛/NNG', '이/JKS']
                if len(t_ret) > 0:
                    ret.append(t_ret)
                t_ret = []
            '''

        if len(t_ret) > 0:
            ret.append(chnkPackageT(t_ret))
        t_ret = []

        contextPackage = contextPackageT(ret)
        contextRePackage = self.setContextRePackage(contextPackage)

        return contextRePackage

    def setContextRePackage(self, contextPackage):
        for i in range(len(contextPackage.chnkPackageList)):
            index = applyRule(contextPackage.chnkPackageList[i]).sumRuleCheck()
            if type(index) is sumRuleCheckResult:
                ret = []
                t_ret = []
                jumpFlag = False
                for j in range(len(contextPackage.chnkPackageList[i].chnkDetailList)):
                    if j in range(index.processResult, index.processResult + index.depth):
                        if jumpFlag == False: jumpFlag = True
                        t_ret.append(contextPackage.chnkPackageList[i].chnkDetailList[j])
                    else:
                        if jumpFlag == True:
                            jumpFlag = False
                            ret.append(chnkDetailT(t_ret))
                            t_ret = []
                        ret.append(contextPackage.chnkPackageList[i].chnkDetailList[j])
                ret.append(chnkDetailT(t_ret))
                t_ret = []
                contextPackage.chnkPackageList[i] = chnkPackageT(ret)

        return contextPackage

    def printContextPackage(self):
        temp_string = []
        for i in range(self.contextPackage.length):
            context = self.contextPackage.index(i)
            # print(context.text)
            temp_string.append(context.text)

            decoResult = applyRule(context).decoRuleCheck()
            for j in range(len(decoResult)):
                # print(decoResult[j].text)
                temp_string.append(decoResult[j].text)
        return temp_string
                



def read_data(filename):
    with open(filename, 'r', encoding='UTF-8') as f:
        data = [line for line in f.read().splitlines()]
    return data


raw_data = read_data('p_rvw_text.txt')

raw_contents = []
contextPackage = []
for i in range(len(raw_data)):
    raw_contents.append(raw_data[i])
    tokenSet = textAnalyzer(raw_data[i])
    contextPackage.append(tokenSet.printContextPackage())

data = []
for i in range(len(raw_contents)):
    data.append([raw_contents[i], contextPackage[i]])

'''
chunk = []
for i in range(len(raw_contents)):
    chunk.append(analyzer(raw_contents[i]).chunk)

deco = []
for i in range(len(raw_contents)):
    deco.append(analyzer(raw_contents[i]).deco)






for i in range(len(textList)):
    tokenSet = textAnalyzer(textList[i])
    #print(tokenSet.tokenized)
    #print(tokenSet.tagList)
    #tokenSet.printChnkPackage()
    tokenSet.printContextPackage()
    #tokenSet.printChnkListDep2()
    print('')
'''