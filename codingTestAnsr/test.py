# 암호 해독
def solution(message, code):
    code_index = ''
    str_pos = 0
    div_per = 2
    code_dict = {}
    answer = ''
    
    # message가 숫자가 아닐때 
    if message.isdigit() == False:
        for i in message:
            if code.index(i) < 9:
                code_index += ''.join('0'+str(int(code.index(i)+1)))
            else:
                code_index += ''.join(str(int(code.index(i)+1)))
        print(code_index)
    else:
        for c in code:
            if code.index(c) < 9:
                code_dict['0'+str(int(code.index(c)+1))] = c
            else:
                code_dict[str(int(code.index(c)+1))] = c
        # print(code_dict)

        while len(message) != str_pos:
            answer_code = message[str_pos:str_pos+div_per]
            str_pos += 2
            answer += ''.join(code_dict[answer_code])
        print(answer)
            




code = "abcdefghijklmnopqrstuvwxyz"
message = '20051920'
# message = 'test'


solution(message, code)
# 다 풀었는데 self 개념을 모름.. (한심)