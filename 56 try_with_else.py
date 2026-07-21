try :  # when only try is succesfull then code run.
    a = int(input(" entera a num:"))
    print(a)

except Exception as e:
    print(e)

else:
    print("thank you")