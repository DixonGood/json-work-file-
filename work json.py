import json

dict = {
    312456:("Astin", 17),
    134567:("Bob", 21),
    324512:("Martin", 27),
    534123:("Meddison",12),
    456789: ("David", 40),
    567890: ("Emma", 45),
}

with open('homework1', "w") as file:
    json.dump(dict, file)