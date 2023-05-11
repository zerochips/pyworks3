import argparse
import os
import sys

def get_args():
    parser = argparse.ArgumentParser(
        # 여기에 생성자죠
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # 명령 인자를 추가한다
    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input string or file')

    # 외부 파일 처리 인자 추가
    parser.add_argument('-o',           # '-o' 이게 out이라는 뜻이야~
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    # return parser.parse_args() 아래 식을 한번에 나타낼 때
    args = parser.parse_args()

    if os.path.isfile(args.text):                       # 여기에 text 가 들어있냐
        # args.text = open(args.text).read()            #
        args.text = open(args.text).read().rstrip()     # rstrip() - 오른쪽 공백 제거

    return args

def main():
    # 메인에서 get_args 불러올겁니다
    args = get_args()
    # print(args.text)
    # 명령 인수가 -o 문자열을 쓰고 파일을 생성하고, 아니면 문자열을 콘솔에 출력(studout)
    # sys 모듈 - stdout(모니터 콘솔에 출력), stdin(모니터 콘솔에서 입력)
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    # out_fh.write(args.text.upper())           #
    out_fh.write(args.text.upper() + '\n')      # 대문자로 변경 출력 설정
    out_fh.close()

if __name__=="__main__":
    main()
