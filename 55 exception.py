try :
    a = int(input(" entera a num:"))
    print(a)

except Exception as e:  # particular error like value error than (except ValueError as v:)
    print(e)

print("thank you") # not show a error because exception is handle a error