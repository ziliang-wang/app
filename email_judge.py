# 子良原创代码--严格捡查email是否正确有效
correct_list = []
incorrect_list = []

def check_email(s):
    '''check email'''
    suffix = ['com', 'net', 'org', 'idv', 'xyz', 'mobi']
    if s.find('@') >= 1 and s.find('.') >= 3:
        if s.count('@') == 1 and s.count('.') == 1:
            if s[s.find('.')+1:] in suffix:
                correct_list.append(s)
                return 'Correct!'
            incorrect_list.append(s)
            return 'Incorrect!'
    else:
        incorrect_list.append(s)
        return 'Incorrect!'

def main():
    while True:
        email = input('请输入您的email, (按\'q\'结束): ')
        if email == 'q':
            if len(correct_list) == 0 and len(incorrect_list) != 0:
                print(), print('Invalid list:'), print('==========')
                for invalid in incorrect_list:
                    print(invalid)
                print()                   
                break
            elif len(correct_list) != 0 and len(incorrect_list) == 0:
                print(), print('Valid list: '), print('==========')
                for valid in correct_list:
                    print(valid)
                print()                   
                break
            elif len(correct_list) != 0 and len(incorrect_list) != 0:
                print(), print('Valid list: '), print('==========')
                for valid in correct_list:
                    print(valid)
                print(), print('Invalid list:'), print('==========')
                for invalid in incorrect_list:
                    print(invalid)
                print()                    
                break
            break
        elif email == '':
            print('请输入e-mail!')
            continue
        elif email.count(' ') >= 1:
            print('不允许输入空白符!')
            continue 
        res = check_email(email)
        print(res)

if __name__ == '__main__':
    main()
