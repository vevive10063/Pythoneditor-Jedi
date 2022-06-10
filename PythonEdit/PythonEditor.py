# coding:utf-8
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.Qsci import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import os
import jedi
import copy
g_colorDict={'Default'                  :'#000000',
             'ClassName'    :'#00FF00',
                        'Keyword'                  :'#B0171F'   ,
                        'Comment'                  :'#00FF00'    ,
                        'Number'                    :'#FF00FF' ,
                        'DoubleQuotedString' :'#0000ff'   ,
                        'SingleQuotedString' :'#0000ff'  ,
                        'TripleSingleQuotedString'  :'#288B22'  ,
                        'TripleDoubleQuotedString' :'#288B22',
                        'FunctionMethodName'  :'#0000FF',
                        'Operator'                 :'#191970',
                        'Identifier'          :'#000000',
                        'CommentBlock'        :'#00FF00',
                        'UnclosedString'       :'#0000FF',
                        'HighlightedIdentifier'   :'#FFFF00',
                        'Decorator'              :'#FF8000'
                    }

# 详情页
class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(401, 306)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QRect(0, 0, 401, 311))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#aa0000;\">项目名称：基于Jedi的Python编辑器的设计与实现</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#aa0000;\">开发者：闫银浩</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#aa0000;\">班级：计科184</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#aa0000;\">学号：2018051153</span></p></body></html>"))

class   DetailDlg(QDialog,Ui_Dialog2):
    def __init__(self, parent=None):
        super(DetailDlg, self).__init__(parent)
        self.setupUi(self)
        if parent == None:
            return
        #1.主窗口作为父窗口 ，颜色的初始值由主窗口传入
        self.parent = parent

# 颜色选择器
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(312, 324)
        Dialog.setCursor(QCursor(Qt.ArrowCursor))
        Dialog.setAcceptDrops(False)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(False)
        self.listStyles = QtWidgets.QListWidget(Dialog)
        self.listStyles.setGeometry(QRect(10, 40, 181, 271))
        self.listStyles.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listStyles.setObjectName("listStyles")
        item = QtWidgets.QListWidgetItem()
        self.listStyles.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listStyles.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listStyles.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listStyles.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listStyles.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listStyles.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listStyles.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listStyles.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listStyles.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listStyles.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listStyles.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listStyles.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listStyles.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listStyles.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listStyles.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listStyles.addItem(item)
        self.defaultButton = QtWidgets.QPushButton(Dialog)
        self.defaultButton.setGeometry(QRect(220, 140, 75, 23))
        self.defaultButton.setMaximumSize(QSize(16777215, 16777215))
        self.defaultButton.setObjectName("defaultButton")
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setGeometry(QRect(220, 210, 75, 23))
        self.okButton.setMaximumSize(QSize(16777215, 16777215))
        self.okButton.setObjectName("okButton")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QRect(220, 280, 75, 23))
        self.cancelButton.setObjectName("cancelButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QRect(10, 10, 171, 21))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.okButton.clicked.connect(Dialog.accept)    #Dialog.accept() 是内建函数，不用使用者实现
        self.cancelButton.clicked.connect(Dialog.reject) #Dialog.reject() 是内建函数，不用使用者实现
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "color Dialog"))
        __sortingEnabled = self.listStyles.isSortingEnabled()
        self.listStyles.setSortingEnabled(False)
        item = self.listStyles.item(0)
        item.setText(_translate("Dialog", "Default"))
        item = self.listStyles.item(1)
        item.setText(_translate("Dialog", "ClassName"))
        item = self.listStyles.item(2)
        item.setText(_translate("Dialog", "Keyword"))
        item = self.listStyles.item(3)
        item.setText(_translate("Dialog", "Comment"))
        item = self.listStyles.item(4)
        item.setText(_translate("Dialog", "Number"))
        item = self.listStyles.item(5)
        item.setText(_translate("Dialog", "DoubleQuotedString"))
        item = self.listStyles.item(6)
        item.setText(_translate("Dialog", "SingleQuotedString"))
        item = self.listStyles.item(7)
        item.setText(_translate("Dialog", "TripleSingleQuotedString"))
        item = self.listStyles.item(8)
        item.setText(_translate("Dialog", "TripleDoubleQuotedString"))
        item = self.listStyles.item(9)
        item.setText(_translate("Dialog", "FunctionMethodName"))
        item = self.listStyles.item(10)
        item.setText(_translate("Dialog", "Operator"))
        item = self.listStyles.item(11)
        item.setText(_translate("Dialog", "Identifier"))
        item = self.listStyles.item(12)
        item.setText(_translate("Dialog", "CommentBlock"))
        item = self.listStyles.item(13)
        item.setText(_translate("Dialog", "UnclosedString"))
        item = self.listStyles.item(14)
        item.setText(_translate("Dialog", "HighlightedIdentifier"))
        item = self.listStyles.item(15)
        item.setText(_translate("Dialog", "Decorator"))
        self.listStyles.setSortingEnabled(__sortingEnabled)
        self.defaultButton.setText(_translate("Dialog", "默认"))
        self.okButton.setText(_translate("Dialog", "OK"))
        self.cancelButton.setText(_translate("Dialog", "CANCEL"))
        self.label.setText(_translate("Dialog", "点击相应文字，即可修改颜色"))

class   ColorDlg(QDialog,Ui_Dialog):
    def __init__(self, parent=None):
        super(ColorDlg, self).__init__(parent)
        self.setupUi(self)
        if parent == None:
            return

        self.parent = parent
        self.DlgRepaint()
    def DlgRepaint(self):
        #2.设置每个item的颜色
        for i in range(0, self.listStyles.count()):
            itm = self.listStyles.item(i)
            cl=QColor(self.parent.colorDict[itm.text()])
            #2.1 编辑区的背景 和 焦点行背景，设置底色
            if itm.text() == 'Background' or itm.text() == 'CaretLine':
                itm. setBackground(cl)
            #2.2 其它项设置字体颜色
            else:
                itm.setForeground(cl)
        self.repaint()
    # QListWidget的单击信号的槽函数
    def on_listStyles_clicked(self):
        itm=self.listStyles.currentItem()
        cl=QColorDialog.getColor(QColor(self.parent.colorDict[itm.text()]))
        if cl.isValid():
            try:
                self.parent.colorDict[itm.text()] = cl.name()   #把有效的颜色保存到颜色字典中
            except:
                pass
            # 把刚刚点击的地方更新颜色
            if itm.text() == 'Background' or itm.text() == 'CaretLine':
                itm. setBackground(cl)
            else:
                itm.setForeground(cl)
    def on_defaultButton_clicked(self):
        global g_colorDict
        self.parent.colorDict=copy.deepcopy(g_colorDict)
        self.DlgRepaint()
# 替换窗口
class replace_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(400,80)
        # self.setStyleSheet("background-color:rgb(0,0,0);")
        self.lineEditer1 = QLineEdit()
        self.lineEditer1.setPlaceholderText("替换前的字符")
        self.lineEditer1.setMinimumSize(80,50)
        self.lineEditer2 = QLineEdit()
        self.lineEditer2.setPlaceholderText("替换后的字符")
        self.lineEditer2.setMinimumSize(80, 50)

        self.button = QPushButton("确认")
        # self.button.clicked.connect(self.findtext2)
        splitter3 = QSplitter()
        splitter3.addWidget(self.lineEditer1)
        splitter3.addWidget(self.lineEditer2)
        splitter3.addWidget(self.button)
        splitter3.setStretchFactor(0,5)
        splitter3.setStretchFactor(1,5)
        splitter3.setStretchFactor(2,1)
        self.setCentralWidget(splitter3)
        self.setWindowTitle("替换")

# 查找窗口1
class search_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500,50)
        # self.setStyleSheet("background-color:rgb(0,0,0);")
        self.lineEditer = QLineEdit()
        self.lineEditer.setPlaceholderText("查找")
        # self.lineEditer.setMinimumSize(80,50)
        self.button1 = QPushButton("模糊查询")
        self.button2 = QPushButton("精确查询")
        self.button1.resize(30,50)
        self.button2.resize(30,50)
        self.label = QLabel()
        self.button_up = QToolButton()
        self.button_up.resize(20,20)
        self.button_up.setArrowType(Qt.UpArrow)
        self.button_up.setEnabled(False)
        self.button_down = QToolButton()
        self.button_down.resize(20,20)
        self.button_down.setArrowType(Qt.DownArrow)
        self.button_down.setEnabled(False)
        splitter2 = QSplitter()
        splitter2.addWidget(self.lineEditer)
        splitter2.addWidget(self.button1)
        splitter2.addWidget(self.button2)
        splitter2.addWidget(self.label)
        splitter2.addWidget(self.button_up)
        splitter2.addWidget(self.button_down)
        splitter2.setStretchFactor(0,10)
        splitter2.setStretchFactor(1,1)
        self.setCentralWidget(splitter2)
        self.setWindowTitle("查找")

# 查找窗口2
class search_window_two(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(400,80)
        # self.setStyleSheet("background-color:rgb(0,0,0);")
        self.lineEditer3 = QLineEdit()
        self.lineEditer3.setPlaceholderText("精确查找")
        self.lineEditer3.setMinimumSize(80,50)
        self.button = QPushButton("确认")
        # self.button.clicked.connect(self.findtext2)
        splitter4 = QSplitter()
        splitter4.addWidget(self.lineEditer3)
        splitter4.addWidget(self.button)
        splitter4.setStretchFactor(0,10)
        splitter4.setStretchFactor(1,1)
        self.setCentralWidget(splitter4)
        self.setWindowTitle("精确查找")

# 语法高亮
class highlight(QsciLexerPython):
    def __init__(self, parent):
        QsciLexerPython.__init__(self, parent)
        if parent == None:
            return
        font = QFont()
        font.setFamily('Courier')
        font.setPointSize(12)
        font.setFixedPitch(True)
        self.setFont(font)
        self.setColor(QColor(0, 0, 0))
        self.setPaper(QColor(255, 255, 255))
        # self.setColor(QColor(self.parent().win.colorDict[ 'ClassName'          ],QsciLexerPython.ClassName))
        self.setColor(QColor("#00FF00"), QsciLexerPython.ClassName)
        # self.setColor(QColor(self.parent().win.colorDict['Keyword']), QsciLexerPython.Keyword)
        self.setColor(QColor("#B0171F"), QsciLexerPython.Keyword)
        # self.setColor(QColor(self.parent().win.colorDict['Comment']), QsciLexerPython.Comment)
        self.setColor(QColor("#00FF00"), QsciLexerPython.Comment)
        # self.setColor(QColor(self.parent().win.colorDict['Number']), QsciLexerPython.Number)
        self.setColor(QColor("#FF00FF"), QsciLexerPython.Number)
        # self.setColor(QColor(self.parent().win.colorDict['DoubleQuotedString']), QsciLexerPython.DoubleQuotedString)
        self.setColor(QColor("#0000FF"), QsciLexerPython.DoubleQuotedString)
        # self.setColor(QColor(self.parent().win.colorDict['SingleQuotedString']), QsciLexerPython.SingleQuotedString)
        self.setColor(QColor("#0000FF"), QsciLexerPython.SingleQuotedString)
        # self.setColor(QColor(self.parent().win.colorDict['TripleSingleQuotedString']), QsciLexerPython.TripleSingleQuotedString)
        self.setColor(QColor("#288B22"), QsciLexerPython.TripleSingleQuotedString)
        # self.setColor(QColor(self.parent().win.colorDict['TripleDoubleQuotedString']), QsciLexerPython.TripleDoubleQuotedString)
        self.setColor(QColor("#288B22"), QsciLexerPython.TripleDoubleQuotedString)
        # self.setColor(QColor(self.parent().win.colorDict['FunctionMethodName']), QsciLexerPython.FunctionMethodName)
        self.setColor(QColor("#0000FF"), QsciLexerPython.FunctionMethodName)
        # self.setColor(QColor(self.parent().win.colorDict['Operator']), QsciLexerPython.Operator)
        self.setColor(QColor("#191970"), QsciLexerPython.Operator)
        # self.setColor(QColor(self.parent().win.colorDict['Identifier']), QsciLexerPython.Identifier)
        self.setColor(QColor("#000000"), QsciLexerPython.Identifier)
        # self.setColor(QColor(self.parent().win.colorDict['CommentBlock']), QsciLexerPython.CommentBlock)
        self.setColor(QColor("#00FF00"), QsciLexerPython.CommentBlock)
        # self.setColor(QColor(self.parent().win.colorDict['UnclosedString']), QsciLexerPython.UnclosedString)
        self.setColor(QColor("#0000FF"), QsciLexerPython.UnclosedString)
        # self.setColor(QColor(self.parent().win.colorDict['HighlightedIdentifier']), QsciLexerPython.HighlightedIdentifier)
        self.setColor(QColor("#FFFF00"), QsciLexerPython.HighlightedIdentifier)
        # self.setColor(QColor(self.parent().win.colorDict['Decorator']), QsciLexerPython.Decorator)
        self.setColor(QColor("#FF8000"), QsciLexerPython.Decorator)
        self.setFont(QFont('Courier', 12, weight=QFont.Bold), 5)
        self.setFont(QFont('Courier', 12, italic=True), QsciLexerPython.Comment)

# 主窗口
class MainWindow(QMainWindow):
    def __init__(self, parent=None, title='Python编辑器', filenamearg=None):
        super(MainWindow, self).__init__(parent)
        # 创建查找窗口
        self.search_window = search_window()
        self.search_window_two = search_window_two()

        # 创建替换窗口
        self.replace_window = replace_window()

        # 创建颜色选择器
        self.color_window = ColorDlg()
        self.colorDict = copy.deepcopy(g_colorDict)

        # 创建详情窗口
        self.detail_window = DetailDlg()

        self.list_line = []
        self.setGeometry(100, 100, 1000, 700)
        self.setWindowTitle(title)
        self.EditFont = QFont('Courier',12)
        font = QFont()
        font.setFamily('Courier')
        font.setPointSize(12)
        font.setFixedPitch(True)
        self.setFont(font)

        # 创建编辑器部件
        self.editor = QsciScintilla()
        self.editor.setFont(font)

        # 创建信息输出视图
        self.text_browser = QTextEdit()
        self.text_browser.setReadOnly(True)
        # self.text_browser.setText("信息输出框")
        self.dockBuilt = QDockWidget("日志",self)
        self.dockBuilt.setMinimumSize(600,150)
        self.dockBuilt.setWidget(self.text_browser)

        # 分隔布局容器
        splitter = QSplitter(Qt.Vertical)
        # splitter.addWidget(self.editor)
        splitter.addWidget(self.editor)
        splitter.addWidget(self.dockBuilt)
        splitter.setStretchFactor(0,5)
        splitter.setStretchFactor(1,1)
        self.setCentralWidget(splitter)
        self.editor.setUtf8(True)

        # 设置行号
        self.editor.setMarginsFont(font)
        self.editor.setMarginWidth(0, len(str(len(self.editor.text().split('\n')))) * 20)
        self.editor.setMarginLineNumbers(0, True)

        # 设置改动标记
        self.editor.setMarginType(1, QsciScintilla.SymbolMargin)  # 设置标号为1的页边用于显示改动标记
        self.editor.setMarginWidth(1, "0000")  # 改动标记占用的宽度
        sym_1 = QsciScintilla.SC_MARK_LEFTRECT
        self.editor.markerDefine(sym_1, 0)
        self.editor.setMarginMarkerMask(1, 0b1111)
        self.editor.setMarkerForegroundColor(QColor("#ff0000"),0)
        self.editor.setMarkerBackgroundColor(QColor("#1296db"),0)

        self.editor.setEdgeMode(QsciScintilla.EdgeLine)
        self.editor.setEdgeColumn(80)
        self.editor.setEdgeColor(QColor(0, 0, 0))

        # 设置括号匹配模式
        self.editor.setBraceMatching(QsciScintilla.StrictBraceMatch)
        # 设置Tab键功能
        self.editor.setIndentationsUseTabs(True)
        self.editor.setIndentationWidth(4)
        self.editor.setTabIndents(True)
        self.editor.setAutoIndent(True)
        self.editor.setBackspaceUnindents(True)
        self.editor.setTabWidth(4)

        # 设置光标
        self.editor.setCaretLineVisible(True)
        self.editor.setCaretLineBackgroundColor(QColor('#FFFFCD'))

        # 虚线垂直的方式来显示缩进
        self.editor.setIndentationGuides(True)

        # 设置代码折叠
        self.editor.setFolding(QsciScintilla.PlainFoldStyle)
        self.editor.setMarginWidth(2, 12)

        # 代码折叠的标志 -+
        self.editor.markerDefine(QsciScintilla.Minus, QsciScintilla.SC_MARKNUM_FOLDEROPEN)
        self.editor.markerDefine(QsciScintilla.Plus, QsciScintilla.SC_MARKNUM_FOLDER)
        self.editor.markerDefine(QsciScintilla.Minus, QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
        self.editor.markerDefine(QsciScintilla.Plus, QsciScintilla.SC_MARKNUM_FOLDEREND)

        # +的颜色
        self.editor.setMarkerBackgroundColor(QColor("#FFFFFF"), QsciScintilla.SC_MARKNUM_FOLDEREND)
        self.editor.setMarkerForegroundColor(QColor("#272727"), QsciScintilla.SC_MARKNUM_FOLDEREND)
        self.editor.setMarkerBackgroundColor(QColor("#FFFFFF"), QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
        self.editor.setMarkerForegroundColor(QColor("#272727"), QsciScintilla.SC_MARKNUM_FOLDEROPENMID)

        # 语法高亮显示
        self.editor.setAutoCompletionSource(QsciScintilla.AcsAll)
        self.editor.setAutoCompletionCaseSensitivity(True)
        self.editor.setAutoCompletionReplaceWord(False)
        self.editor.setAutoCompletionThreshold(1)         # 输入一个字符就出现自动补全提示
        self.editor.setAutoCompletionUseSingle(QsciScintilla.AcusExplicit)
        self.lexer = highlight(self.editor)
        self.editor.setLexer(self.lexer)

        self.mod = False
        # 设置自动补全
        self.__api = QsciAPIs(self.lexer)

        self.code = ''
        script = jedi.Script(self.code, path='')
        complete = script.complete()
        # print(len(complete))
        autocompletions = []
        for i in complete:
            autocompletions.append(i.name)

        for ac in autocompletions:
            self.__api.add(ac)
        self.__api.prepare()
        self.editor.autoCompleteFromAll()
        if filenamearg:
            obj = open(filenamearg, 'r+', encoding='utf-8')
            try:
                self.editor.setText(obj.read())
            except:
                QMessageBox.warning(self, '警告', '无法打开此文件！', QMessageBox.Ok)
                self.editor.document().clear()
        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)

        # 菜单栏功能
        fileNewAction = self.createAction("新建", self.newfile,
                                          'Ctrl+N', "filenew", "创建Python文件")
        fileOpenAction = self.createAction("打开", self.fileopen,
                                           'Ctrl+O', "fileopen",
                                           "打开Python文件")
        self.fileSaveAction = self.createAction("保存", self.save,
                                                'Ctrl+S', "filesave", "保存Python文件")
        self.fileSaveAsAction = self.createAction("另存为",
                                                  self.saveas, "Ctrl+Alt+S", "filesaveas",
                                                  "另存为")
        fileQuitAction = self.createAction("退出", self.close,
                                           "Ctrl+Q", "filequit", "退出")
        self.editUndoAction = self.createAction("撤销", self.editor.undo,
                'Ctrl+Z', "editundo",
                "撤销还原")
        self.editRedoAction = self.createAction("重做", self.editor.redo,
                'Ctrl+Alt+Z', "editredo",
                "重做")
        self.editCopyAction = self.createAction("复制",
                                                self.editor.copy, 'Ctrl+C', "editcopy",
                                                "复制")
        self.editCutAction = self.createAction("剪切", self.editor.cut,
                                               'Ctrl+X', "editcut",
                                               "剪切")
        self.editPasteAction = self.createAction("粘贴", self.editor.paste,
                'Ctrl+V', "editpaste",
                "粘贴")
        # self.jedifindAction = self.createAction("精确查找", self.jedifind,
        #                                         'Ctrl+Alt+F', 'editfind2', "精确查找")
        self.findAction = self.createAction("查找",
                                            self.findtext, 'Ctrl+F', "editfind",
                                            "查找")
        self.replaceAction = self.createAction("替换",
                                               self.replace_text,
                                               'Ctrl+R', "editreplace",
                                               "替换")
        self.analyseAction = self.createAction("查找错误",
                                               self.finderror, 'Ctrl+G', "editerrors", "查找错误")
        self.anaNameAction = self.createAction("查找名称",
                                               self.findname, 'Ctrl+H', "editnames", "查找名称")
        self.gotoAction = self.createAction("名称转到",
                                            self.goto, 'Ctrl+J', "editgoto", "名称转到定义处")
        self.inferAction = self.createAction("类型推断",
                                             self.infer, 'Ctrl+K', 'editinfer', "类型推断")
        self.runAction = self.createAction('运行',
                                           self.run, 'Ctrl+B', 'editrun', '运行程序')
        self.colorselectAction = self.createAction('颜色选择',
                                                   self.colorselect,'Ctrl+L','editcolor','颜色选择')
        self.editFontAction = self.createAction("字体选择", self.getFont,
                'Ctrl+Alt+L', 'editcolor',
                "选择字体")
        self.windowShowBuiltAction = self.createAction('日志',
                                                       self.showBuiltWindow,'Ctrl+Alt+B','editbuilt','日志')
        self.detailAction = self.createAction('详情',
                                              self.detailWindow,'Ctrl+N','editdetail','详情')
        # self.inlineAction = self.createAction('内联', self.inline, 'Ctrl+L', 'editinline','内联代码')
        # 菜单按钮
        fileMenu = self.menuBar().addMenu("文件")
        self.addActions(fileMenu, (fileNewAction, fileOpenAction,
                                   self.fileSaveAction, self.fileSaveAsAction, None,
                                   fileQuitAction))
        editMenu = self.menuBar().addMenu("编辑")
        self.addActions(editMenu, (self.editCopyAction,
                                   self.editCutAction, None,
                                    self.findAction,
                                   self.replaceAction,
                                   self.analyseAction,
                                   self.anaNameAction,
                                   self.gotoAction,
                                   self.inferAction))
        runMenu = self.menuBar().addMenu('运行')
        self.addActions(runMenu, (self.runAction,))
        settingMenu = self.menuBar().addMenu('设置')
        self.addActions(settingMenu, (self.colorselectAction,
                                      self.editFontAction))
        windowMenu = self.menuBar().addMenu('窗口')
        self.addActions(windowMenu,(self.windowShowBuiltAction,))
        detailMenu = self.menuBar().addMenu('详情')
        self.addActions(detailMenu,(self.detailAction,))
        # 文件工具栏
        fileToolbar = self.addToolBar("File")
        fileToolbar.setObjectName("FileToolbar")
        self.addActions(fileToolbar,(fileNewAction,
                                     fileOpenAction,
                                     self.fileSaveAction))
        # 编辑工具栏
        editToolbar = self.addToolBar('Edit')
        editToolbar.setObjectName("EditToolbar")
        self.addActions(editToolbar,(self.editRedoAction,
                                     self.editUndoAction,
                                     self.editCopyAction,
                                     self.editPasteAction,
                                     self.editCutAction))
        # 读取颜色信息
        settings = QSettings('setting.ini',QSettings.IniFormat)
        # settings.setIniCodec(QTextCodec.codecForName("utf-8"))
        for style in self.colorDict.keys():
            str1 = 'color/' + style
            str1 = settings.value(str1)
            if str1 is not None:
                self.colorDict[style] = str1
        self.name = ''
        self.editor.textChanged.connect(self.changed)
        self.filename = filenamearg

    def run(self):
        if self.windowTitle() == '未命名':
            self.askforsave()
        print(self.windowTitle())
        os.system('call python ' + self.windowTitle())

    def changed(self):
        self.mod = True
        self.editor.setMarginWidth(0, len(str(len(self.editor.text().split('\n')))) * 20)
        line, index = self.editor.getCursorPosition()    #获取当前光标所在行
        handle_01 = self.editor.markerAdd(line, 0)     # 添加改动标记
        self.list_line.append(handle_01)        #保存改动标记所在的地方，给后面保存文档时消除标记提供信息
        # code = self.editor.text()
        # print(code)
        # script = jedi.Script(code,path='')
        # complete = script.complete(line+1,index+1)
        # print(len(complete))

    def createAction(self, text, slot=None, shortcut=None, icon=None,
                     tip=None, checkable=False, signal="triggered()"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon("./EditIcon/{0}.png".format(icon)))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            action.triggered.connect(slot)
        if checkable:
            action.setCheckable(True)
        return action

    def addActions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def askforsave(self):
        if self.mod:
            r = QMessageBox.question(self, '询问', '是否要保存?',
                                     QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if r == QMessageBox.Cancel:
                return False
            elif r == QMessageBox.Yes:
                return self.save()

            return True

    def save(self):
        if not self.name:
            return self.saveas()
        self.mod = False
        self.setWindowTitle(self.name)
        obj = open(self.name, 'w', encoding='utf-8')
        obj.truncate()
        obj.close()
        obj = open(self.name, 'r+', encoding='utf-8')
        try:
            obj.write(self.editor.text())
        except:
            obj.write('An error has occcured when trying to save this file.')
        obj.close()

    def saveas(self):
        filename, _buff = QFileDialog.getSaveFileName(self, '另存为', './', 'Python文件 (*.py)')
        if filename:
            self.name = filename
            return self.save()
        return False

    def newfile(self):
        if self.mod:
            if not self.askforsave():
                return -1
        self.editor.clear()
        self.mod = False
        self.name = ''
        self.setWindowTitle('未命名')

    def fileopen(self):
        if self.mod:
            if not self.askforsave():
                return -1
        filename, _buff = QFileDialog.getOpenFileName(self, '打开', './', 'Python文件 (*.py)')
        if filename:
            self.name = filename
            obj = open(self.name, 'r+', encoding='utf-8')
            try:
                self.editor.setText(obj.read())
            except Exception as e:
                self.editor.setText("Can't read this file!Error:" + str(e))
            obj.close()
            self.setWindowTitle(self.name)
            self.mod = False

    def closeEvent(self, event):
        if not self.askforsave():
            event.ignore()
        event.accept()

    # def jedifind(self):
    #     self.search_window_two.raise_()
    #     self.search_window_two.show()
    #     self.search_window_two.lineEditer3.setText(self.editor.selectedText())
    #     self.search_window_two.button.clicked.connect(self.jedifind2)

    def jedifind2(self):
        self.text_browser.clear()
        # print(111)
        code = self.editor.text()
        jedifindtext = self.search_window.lineEditer.text()
        # print(jedifindtext)
        script = jedi.Script(code, path='')
        search = script.search(str(jedifindtext))
        # print(search[0]._get_module_context())
        if not jedifindtext:
            warning = QMessageBox.warning(self,
                                          '提示',
                                          '输入字符为空，请重新输入',QMessageBox.Yes)
            if warning == QMessageBox.Yes:
                self.search_window.raise_()
                return False
        elif not search:
            self.search_window.label.setText("0 result")
            self.search_window.button_up.setEnabled(False)
            self.search_window.button_down.setEnabled(False)
            warning2 = QMessageBox.warning(self,
                                           '提示',
                                           '未找到该字符！',QMessageBox.Yes)
            if warning2 == QMessageBox.Yes:
                self.search_window.raise_()
                return False
        elif search:
            self.search_window.button_up.setEnabled(False)
            self.search_window.button_down.setEnabled(False)
            self.search_window.label.setText("1 result")
            self.editor.setCursorPosition(search[0].line - 1, 0)
            self.text_browser.setText(str(search))


    def findtext(self):
        code = self.editor.text()
        if not code:
            warning = QMessageBox.warning(self,
                                          "提示","未输入检测文本!",QMessageBox.Yes)
            if warning == QMessageBox.Yes:
                return False
        else:
            self.search_window.show()
            self.search_window.lineEditer.setText(self.editor.selectedText())
            self.search_window.label.setText("0 result")
            self.search_window.button1.clicked.connect(self.findtext2)
            self.search_window.button2.clicked.connect(self.jedifind2)

    def findtext2(self):
        self.init_i = 1
        self.text_browser.clear()
        findtext = self.search_window.lineEditer.text()
        # print(findtext)
        if not findtext:
            warning = QMessageBox.warning(self,'提示','输入字符不能为空，请重新输入！',QMessageBox.Yes)
            if warning == QMessageBox.Yes:
                return False
        code = self.editor.text()
        # print(code)
        str_count = 0
        self.lines = []
        input_str = code.splitlines()
        print(input_str)
        for i in range(len(input_str)):
            if findtext in input_str[i]:
                str_count += 1
                self.lines.append(i+1)
                self.text_browser.append("第%d行:%s"%(i+1,input_str[i]))
        self.text_browser.append("共找到%d处"%(str_count))

        if str_count > 0:
            self.search_window.label.setText("%d/%d" % (1, str_count))
            self.search_window.button_up.setEnabled(True)
            self.search_window.button_down.setEnabled(True)
        self.search_window.button_up.clicked.connect(self.find_up)
        print(len(self.lines))
        self.search_window.button_down.clicked.connect(self.find_down)
        # self.editor.ensureLineVisible(self.lines[0]-1)
        self.editor.setCursorPosition(self.lines[0]-1, 0)

    def find_up(self):
        count = len(self.lines)
        if self.init_i > 1:
            self.init_i -= 1
            self.search_window.label.setText("%d/%d" % (self.init_i, count))
            # self.editor.ensureLineVisible(self.lines[self.init_i]-1)
            self.editor.setCursorPosition(self.lines[self.init_i-1]-1, 0)
        elif self.init_i == 1:
            self.init_i = count
            self.search_window.label.setText("%d/%d" % (self.init_i, count))
            self.editor.setCursorPosition(self.lines[self.init_i-1] - 1, 0)

    def find_down(self):
        count = len(self.lines)
        if self.init_i < count:
            self.init_i += 1
            self.search_window.label.setText("%d/%d" % (self.init_i, count))
            self.editor.setCursorPosition(self.lines[self.init_i - 1] - 1, 0)
        elif self.init_i == count:
            self.init_i = 1
            self.search_window.label.setText("%d/%d" % (self.init_i, count))
            self.editor.setCursorPosition(self.lines[self.init_i-1] - 1, 0)
        pass

    def finderror(self):
        self.text_browser.clear()
        count = 0
        code = self.editor.text()
        print(code)
        script = jedi.Script(code,path='')
        errors = script.get_syntax_errors()
        print(str(errors))
        if not errors:
            self.text_browser.setText("没有发现错误")
        else:
            for i in range(len(errors)):
                count += 1
                self.text_browser.append(str(errors[i]))
            self.text_browser.append("共%d个错误"%(count))
            # self.text_browser.setText(str(errors))
        pass

    def findname(self):
        self.text_browser.clear()
        count = 0
        code = self.editor.text()
        script = jedi.Script(code,path='')
        names = script.get_names()
        print(str(names))
        if not names:
            self.text_browser.setText('没有定义的名称')
        else:
            for i in range(len(names)):
                count += 1
                self.text_browser.append(str(names[i]))
            self.text_browser.append("共%d个名称"%(count))
            # self.text_browser.setText(str(names))

    def replace_text(self):
        self.replace_window.raise_()
        self.replace_window.show()
        self.replace_window.lineEditer1.setText(self.editor.selectedText())
        self.replace_window.button.clicked.connect(self.replace_text2)
        pass

    def replace_text2(self):
        self.text_browser.clear()
        str_count = 0
        code = self.editor.text()
        replace_old = self.replace_window.lineEditer1.text()
        replace_new = self.replace_window.lineEditer2.text()
        # print(len(code))
        if not replace_old:
            r1 = QMessageBox.question(self,'提示','输入的字符不能为空，是否重新输入',QMessageBox.Yes | QMessageBox.No)
            if r1 == QMessageBox.Yes:
                return self.replace_text()
            else:
                return False
        elif replace_old in code:
            input_str = code.splitlines()
            for i in range(len(input_str)):
                if replace_old in input_str[i]:
                    str_count += 1
            str = code.replace(replace_old,replace_new)
            # print(str)
            self.editor.setText(str)
            self.text_browser.setText("%s成功替换为%s,共替换%d处"%(replace_old,replace_new,str_count))
        elif replace_old not in code:
            self.text_browser.setText('未找到%s，替换失败!'%(replace_old))
            r2 = QMessageBox.question(self, '提示', '未找到需要替换的字符,是否重新输入', QMessageBox.Yes | QMessageBox.No)
            if r2 == QMessageBox.Yes:
                return self.replace_text()
            else:
                self.replace_window.close()
                return False

    def goto(self):
        self.text_browser.clear()
        code = self.editor.text()
        script = jedi.Script(code, path='')
        line, index = self.editor.getCursorPosition()
        if not line:
            r = QMessageBox.warning(self,"提示",'未检测到鼠标位置，请重新输入',QMessageBox.Yes)
            if r == QMessageBox.Yes:
                return False
        else:
            goto = script.goto(line+1,index+1)
            if not goto:
                self.text_browser.setText("未找到声明的名称")
            else:
                # print(infer[0].line,infer[0].column)
                self.editor.setCursorPosition(goto[0].line-1, 0)
                for i in range(len(goto)):
                    self.text_browser.append(str(goto[i]))
        pass

    def infer(self):
        code = self.editor.text()
        script = jedi.Script(code, path='')
        line, index = self.editor.getCursorPosition()
        print(line,index)
        if not line:
            r = QMessageBox.warning(self,"提示",'未检测到鼠标位置，请重新输入',QMessageBox.Yes)
            if r == QMessageBox.Yes:
                return False
        else:
            infer = script.infer(line+1,index+1)
            if not infer:
                r = QMessageBox.warning(self,"提示",'类型推断失败，请重新输入',QMessageBox.Yes)
                if r == QMessageBox.Yes:
                    return False
            else:
                self.text_browser.setText(str(infer))
        pass

    def showBuiltWindow(self):
        if self.dockBuilt.isVisible():
            self.windowShowBuiltAction.setChecked(False)
            return
        self.dockBuilt.show()
        pass

    def colorselect(self):
        SettingDlg = ColorDlg(self)
        ret = SettingDlg.exec_()
        if not ret:
            return
        settings = QSettings("setting.ini",QSettings.IniFormat)
        for style in self.colorDict.keys():
            str1 = 'color/'+style
            settings.setValue(str1,self.colorDict[style])
        pass

    def getFont(self):
        font,ok = QFontDialog.getFont(self.EditFont)
        if ok:
            self.EditFont = font
            settings=QSettings("setting.ini",QSettings.IniFormat)
            settings.setIniCodec(QTextCodec.codecForName("utf-8"))
            settings.setValue("Font/Family",   font.family())
            settings.setValue("Font/pointSize",       font.pointSize())
            if font.bold():
                settings.setValue("Font/isBold",       '1')
            else:
                settings.setValue("Font/isBold",       '0')

    # def inline(self):
    #     code = self.editor.text()
    #     script = jedi.Script(code, path='')
    #     line, index = self.editor.getCursorPosition()
    #     print(line,index)
    #     if not line:
    #         r = QMessageBox.warning(self,"提示",'未检测到鼠标位置，请重新输入',QMessageBox.Yes)
    #         if r == QMessageBox.Yes:
    #             return False
    #     else:
    #         inline = script.inline(line+1,index+1)
    #         self.text_browser.setText(str(inline))
    #     pass
    def detailWindow(self):
        DetailsDlg = DetailDlg(self)
        ret = DetailsDlg.exec_()
        if not ret:
            return
        pass

def main():
    import sys
    from os import path
    app = QApplication(sys.argv)
    fname = '未命名'
    if len(sys.argv) > 1:
        if path.isfile(sys.argv[1]):
            fname = sys.argv[1]
    form = MainWindow(None, fname, fname if fname != '未命名' else None)
    form.show()
    app.exec_()

main()