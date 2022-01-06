import tkinter, decimal

root = tkinter.Tk()
root.title('calculator')
root.resizable(0, 0)
root.geometry('320x350')

global activeStr
global stack

result = operation = None

activeStr = tkinter.StringVar()

stack = []


class buttonEvent:
    def __init__(self, buttonEvent):
        self.buttonEvent = buttonEvent


    def write(self):
        stack.append(self.buttonEvent)
        activeStr.set(''.join(stack))


    def tui(self):
        stack.pop()
        activeStr.set(''.join(stack))


    def clear(self):
        stack.clear()
        activeStr.set('')
        result = None
        operation = None


    def pn(self):
        if stack[0]:
            if stack[0] == '-':
                stack[0] = '+'
            elif stack[0] == '+':
                stack[0] = '-'
            else:
                stack.insert(0, '-')
            vartext.set(''.join(stack))


    def point(self):
        if stack.count('.') >= 1:
            pass
        else:
            if stack == []:
                stack.append('0')
            stack.append('.')
        activeStr.set(''.join(stack))


    def deal(self):
        global result, operation, result
        if activeStr.get() == '':
            pass
        else:
            number1 = decimal.Decimal(activeStr.get())
        if self.buttonEvent in ('+', '-', '×', '÷', '='):
            if operation is not None:
                number1 = decimal.Decimal(result)
                number2 = decimal.Decimal(activeStr.get())
                if operation == '+':
                    result = number1 + number2
                elif operation == '-':
                    result = number1 - number2
                elif operation == '×':
                    result = number1 * number2
                elif operation == '÷':
                    result = number1 / number2
            else:
                result = number1
            if self.buttonEvent == '=':
                operation = None
            else:
                operation = self.buttonEvent
       
        activeStr.set(str(result))
        stack.clear()


def layOut(root):
    global activeStr
    entry1 = tkinter.Label(root, width=45, height=4, background='grey', anchor='se', textvariable=activeStr)
    entry1.grid(row=0, columnspan=5)

    buttonCE = tkinter.Button(root, text='CE', width=10, height=3)
    buttonC = tkinter.Button(root, text='C', width=10, height=3, command=buttonEvent('C').clear)
    buttonDelete = tkinter.Button(root, text='DEL', width=10, height=3, command=buttonEvent('DEL').tui)
    buttonDivide = tkinter.Button(root, text='÷', width=10, height=3, command=buttonEvent('÷').deal)
    buttonCE.grid(row=1, column=0)
    buttonC.grid(row=1, column=1)
    buttonDelete.grid(row=1, column=2)
    buttonDivide.grid(row=1, column=3)

    button7 = tkinter.Button(root, text='7', width=10, height=3, command=buttonEvent('7').write)
    button8 = tkinter.Button(root, text='8', width=10, height=3, command=buttonEvent('8').write)
    button9 = tkinter.Button(root, text='9', width=10, height=3, command=buttonEvent('9').write)
    buttonMutiply = tkinter.Button(root, text='×', width=10, height=3, command=buttonEvent('×').deal)
    button7.grid(row=2, column=0)
    button8.grid(row=2, column=1)
    button9.grid(row=2, column=2)
    buttonMutiply.grid(row=2, column=3)

    button4 = tkinter.Button(root, text='4', width=10, height=3, command=buttonEvent('4').write)
    button5 = tkinter.Button(root, text='5', width=10, height=3, command=buttonEvent('5').write)
    button6 = tkinter.Button(root, text='6', width=10, height=3, command=buttonEvent('6').write)
    buttonSub = tkinter.Button(root, text='-', width=10, height=3, command=buttonEvent('-').deal)
    button4.grid(row=3, column=0)
    button5.grid(row=3, column=1)
    button6.grid(row=3, column=2)
    buttonSub.grid(row=3, column=3)

    button1 = tkinter.Button(root, text='1', width=10, height=3, command=buttonEvent('1').write)
    button2 = tkinter.Button(root, text='2', width=10, height=3, command=buttonEvent('2').write)
    button3 = tkinter.Button(root, text='3', width=10, height=3, command=buttonEvent('3').write)
    buttonPlus = tkinter.Button(root, text='+', width=10, height=3, command=buttonEvent('+').deal)
    button1.grid(row=4, column=0)
    button2.grid(row=4, column=1)
    button3.grid(row=4, column=2)
    buttonPlus.grid(row=4, column=3)

    button_ = tkinter.Button(root, text='+/-', width=10, height=3, command=buttonEvent('+/-').pn)
    button0 = tkinter.Button(root, text='0', width=10, height=3, command=buttonEvent('0').write)
    buttonPoint = tkinter.Button(root, text='.', width=10, height=3, command=buttonEvent('.').point)
    buttonEqual = tkinter.Button(root, text='=', width=10, height=3, command=buttonEvent('=').deal)
    button_.grid(row=5, column=0)
    button0.grid(row=5, column=1)
    buttonPoint.grid(row=5, column=2)
    buttonEqual.grid(row=5, column=3)


if __name__ == '__main__':
    layOut(root)
    root.mainloop()
