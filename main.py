from re import I
import requests

def inputgetter():
    text = input("is this cool?")
    if text == "yes":
        return True
    else:
        return False

def APIpicker(isCool):
    Starwarsapi = "https://swapi.dev/api/people/3"
    PokemonAPI = "https://pokeapi.co/api/v2/pokemon/ditto"
    URL = ""

    if isCool:
        URL = PokemonAPI
    else:
        URL = Starwarsapi
    return URL

def starwars_multiple_API_calls():
    print("get first five")
    for i in range(5):
        res = requests.get("https://swapi.dev/api/people/"+str(i+1))
        json = res.json() 
        if int(json['height']) > 171:
            templatestring = json['name'] + " " + json['height'] + " cm"
            print(templatestring)
            
def normal(ChosenAPI):
    print("requesting API")
    res = requests.get(ChosenAPI)
    print(res.headers)
    print(res.status_code)
    print(res.text)

def main():
    isCool = inputgetter()
    ChosenAPI = APIpicker(isCool)
    if isCool == False:
       starwars_multiple_API_calls()
    else:
        normal(ChosenAPI)

if __name__ == '__main__':
    main()
