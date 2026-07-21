try :  # when  try is succes or not finalyy is run.
    a = int(input(" entera a num:"))
    print(a)

except Exception as e:
    print(e)

finally:
    print("thank you")