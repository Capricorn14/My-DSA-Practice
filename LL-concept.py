#Linked list using dictionaries
head = {
        "value" : 11,
        "next" : {
            "value" : 3,
            "next" : {
                "value" : 5,
                "next" : None

            }
        }
}

print(head['next']['next']['value'])

