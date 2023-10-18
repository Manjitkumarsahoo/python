#EXCEPTION HANDLING

def divide(no1,no2):
    print("Divide start")
    try:
        print(no1/no2)
    except:
        print("d z caught")
print("main start")
divide(10,2)
divide(10,0)
print("main end")