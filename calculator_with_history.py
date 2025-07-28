HISTORY_FILE='history.txt'

def show_history():
    file=open(HISTORY_FILE,'r')
    lines=file.readlines()
    if len(lines)==0:
        print('No history found!')
    else:
        for line in reversed(lines):
            print(line.strip())
        file.close()
        
def clear_history():
    file=open(HISTORY_FILE,'w')
    file.close()
    print('History cleared!')
    
def save_to_hist(equation,result):
    file=open(HISTORY_FILE,'a')
    file.write(equation + '=' + str(result) + '\n')
    file.close()

def calculate(user_input):
    parts=user_input.split()
    if len(parts)!=3:
        print('invalid input use format: number operator (eg.8+8)')
        return

    num1=float(parts[0])
    op=parts[1]
    num2=float(parts[2])
    
    if op=='+':
        result=num1+num2
    elif op=='-':
        result=num1-num2
    elif op=='*':
        result=num1*num2
    elif op=='/':
        if num2==0:
            print('cant divide by 0')
            return
        result=num1/num2
    else:
        print('invalid operator is being used plz use form these +,-,*,/')
        