graph = {
    "Biratnagar": {"Itahari": 22, "Rangeli": 25},
    "Itahari": {"Biratnagar": 22, "Dharan": 20, "Biratchowk": 30},
    "Dharan": {"Itahari": 20},
    "Biratchowk": {"Itahari": 30, "Kanepokhari": 10,"Biratnagar":30},
    "Kanepokhari": {"Biratchowk": 10, "Urlabari": 12, "Rangeli": 25},
    "Rangeli": {"Biratnagar": 25, "Kanepokhari": 25,"Urlabari":40},
    "Urlabari": {"Kanepokhari": 12, "Damak": 6,"Rangeli":40},
    "Damak": {"Urlabari": 6}
}


print("Graph :", graph)