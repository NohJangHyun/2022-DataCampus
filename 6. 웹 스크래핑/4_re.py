#정규식 - 정해진 형태를 의미하는 식 => 주민등록번호(생년월일 - xxxxxx), 이메일 주소(xxxx@naver.com), IP주소(123.123.0.1)
import re #정규식 라이브러리 
#ca?e => 3번째 글자 기억 안난다고 가정, a~z까지 하나씩 넣어보는건 일이 많음 => 정규식 이용

p = re.compile("ca.e") 
#p : pattern을 의미
# . (ca.e) : 하나의 문자 > 한 글자만 가능
# ^ (^de) : 문자열의 시작 > desk, destiny 가능 but fade는 X)
# $ (se$) : 문자열의 끝 > case, base 가능 but face는 X

#정규식 기초 1
#def print_match(m):
#    if m:
#        print("m.group(): ", m.group()) #일치하는 문자열 반환
#    else:
#        print("매칭되지 않음")

#m = p.match("care")#패턴과 매치되는 경우, 변형 예제 : careless의 경우 주어진 문자열이 처음부터 일치하는지 확인하기 때문에 뒤에 다른 값이 있어도 일치한다고 판단하고 care 출력
#m = p.match("good care") #패턴과 매치되지 않는 경우
#print_match(m)
#print(m.group()) #매치되면 정상 출력, 매치되지 않으면 에러 발생


#정규식 기초 2
# def print_match(m):
#     if m:
#         print("m.group(): ", m.group()) #일치하는 문자열 반환
#         print("m.string: ", m.string) #입력받은 문자열 반환
#         print("m.start(): ", m.start()) #일치하는 문자열의 시작 index
#         print("m.end(): ", m.end()) #일치하는 문자열의 끝 index
#         print("m.span(): ", m.span()) #일치하는 문자열의 시작 / 끝 index 같이 출력
#     else:
#         print("매칭되지 않음")

# m = p.search("careless") #주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)


#정규식 기초 3
# lst = p.findall("good care cafe") #일치하는 모든 것을 리스트 형태로 반환, 두개인 경우 두개 출력
# print(lst) 
