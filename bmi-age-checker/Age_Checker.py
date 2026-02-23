from datetime import date 
try:
    birth=list(map(int, input("Enter The date of birthday (DD-MM-YYYY) ").split("-")))
    day,month,year=birth

    curent_time=date.today()
    age=curent_time.year-year
    if (curent_time.month,curent_time.day)<(month,day):
         age-=1
    print("Enter The Your BOB:",birth)
    if age < 18:
         print(f"Category: Child and age={age}")
    elif age < 60:
     print(f"Category: Adult and age={age}")
    else: 
     print(f"Category: Senior Citizen age={age}")
except ValueError:
   print("your are inter the involed bob")