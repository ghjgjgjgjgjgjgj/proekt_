import json
file = open("works.json","w+", encoding= " utf-8" )
spisok_rabot = [
    {
        "name": "Работник дорог",
        "start_temp": "0",
        "end_temp": "30",
        "fallout": "True"
    },
    {
        "name": "Работник",
        "start_temp": "5",
        "end_temp": "10",
        "fallout": "True"
    }


]
# file.read()
json.dump(spisok_rabot,file, ensure_ascii=False)
file.close()







































