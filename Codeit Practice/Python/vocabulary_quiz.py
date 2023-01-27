#파일 읽고 쓰기

#단어 퀴즈
"""
프로그램은 콘솔에 한국어 뜻을 알려 줄 것이고, 사용자는 그에 맞는 영어 단어를 입력해야 합니다. 사용자가 입력한 영어 단어가 정답이면 "맞았습니다!"라고 출력하고, 틀리면 "아쉽습니다. 정답은 OOO입니다."가 출력되어야 합니다.
문제를 내는 순서는 vocabulary.txt에 정리된 순서입니다.
"""
with open('Python/vocabulary.txt','r') as f:
    for line in f:
        #단어장의 단어와 뜻을 따로 변수에 담음
        e_word, k_word = line.split(": ")
        
        #사용자로부터 값을 입력 받음
        input_word = input(f"{k_word}: ")
        
        if input_word == e_word:
            print("맞았습니다!")
        else:
            print(f"아쉽습니다. 정답은 {e_word}입니다.")
        