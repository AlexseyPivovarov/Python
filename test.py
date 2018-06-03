database = {
    "alexei": {
        "name": {"first_name": "Alexei", "second_name": "Pivovarov"},
        "tel ": ["36546341", "654654"],
        "mail": ["smaster@bigmir.net", "smaster@gmail.com"],
    },
}

test = {}
test["1"] = database["alexei"]["name"]["first_name"]
print(test)
print(database["alexei"]["name"])
