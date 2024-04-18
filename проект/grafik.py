import json
file = open("grafik.json","w+", encoding= " utf-8" )
grafik = [

  {
    "date": "16.04.2024",
    "work": "Маляр",
    "worker": "Влад"
  },
  {
    "date": "17.04.2024",
    "work": "Механик",
    "worker": "Федя"
  },
  {
    "date": "18.06.2024",
    "work": "Маляр",
    "worker": "Федя"
  }

]
# file.read()
json.dump(grafik,file, ensure_ascii=False)
file.close()
