import sys

def generate_yareu_code(text):
    code = []
    

    byte_sequence = text.encode('utf-8')
    
    current_val = 0
    for byte in byte_sequence:
        diff = byte - current_val
        
        if diff > 0:
            code.append("야르 " * diff)
        elif diff < 0:
            code.append("야르릉 " * abs(diff))
            
        code.append("야르렁\n")
        current_val = byte
        
    code.append("\n할렐야루\n")
    return "".join(code)

def main():
    print("=== 야르랭(YareuLang) 코드 생성기 ===")
    
    file_name = input("저장할 파일 이름을 입력하세요 (예: test.yr): ").strip()
    if not file_name:
        print("오류: 파일 이름은 비워둘 수 없습니다.", file=sys.stderr)
        return

    if not file_name.endswith('.yr'):
        file_name += '.yr'
        print(f"안내: 파일 확장자가 자동으로 '.yr'로 지정되었습니다. -> {file_name}")

    print("\n변환할 문자열(내용)을 입력하세요.")
    print("입력을 모두 마치려면 빈 줄에서 엔터(Enter)를 한 번 더 누르세요:")
    
    lines = []
    while True:
        try:
            line = input()
            if line == "":
                break
            lines.append(line)
        except EOFError:
            break

    input_text = "\n".join(lines)

    if not input_text:
        print("오류: 입력된 내용이 없어 코드를 생성하지 않습니다.", file=sys.stderr)
        return

    generated_code = generate_yareu_code(input_text)

    try:
        # 파일 저장 시 반드시 utf-8 인코딩 명시
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(generated_code)
        print(f"\n성공적으로 '{file_name}' 파일에 코드가 생성 및 저장되었습니다.")
    except Exception as e:
        print(f"오류: 파일을 저장하는 도중 에러가 발생했습니다: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
