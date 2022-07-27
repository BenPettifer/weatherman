import requests

def main():
    print("hello world")
    res = requests.get("http://www.google.com")
    print(res.status_code)
    print(res.text)

if __name__ == '__main__':
    main()