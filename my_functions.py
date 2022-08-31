def greet(name, time_of_day):
    return f"Good {time_of_day} {name}"
    #print("Hey")


greeting = greet('Colin', "Morning")
greeting_2 = greet("Ada", "Afternoon")
print (greeting)
print(greeting_2)

word_global = 'hi'

def greet():
    words = 'hey'
    return words
def greet_two():
    return word_global

###############################################################################################################
chickens = [
  { "name": "Margaret", "age": 2, "eggs": 0 },
  { "name": "Hetty", "age": 1, "eggs": 2 },
  { "name": "Henrietta", "age": 3, "eggs": 1 },
  { "name": "Audrey", "age": 2, "eggs": 0 },
  { "name": "Mabel", "age": 5, "eggs": 1 },
]



def count_eggs(list):
    total_eggs = 0

    for item in list:
        total_eggs += item["eggs"]
        item["eggs"] = 0 # eggs have been collected
    
    return f"{total_eggs} eggs collected"

result=count_eggs(chickens)
print(result)
print(chickens)
