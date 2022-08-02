import requests

def main():
    print("hello world")
    res = requests.get("http://127.0.0.1:8000")
    print(res.headers)
    print(res.status_code)
    print(res.text)
    #


if __name__ == '__main__':
    main()