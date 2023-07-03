print("hello welcome to leap year finder")
print("made by Rownak web office thingy")



year = int (input (" pls enter year"))

if (year % 4) == 0:

              if (year % 100) == 0:

                             if (year % 400) == 0:

                                            print ("The given year is a leap year")

                             else:

                                            print ("It is not a leap year")

              else:

                             print ("It is not a leap year")

else:     

            print ("It is not a leap year")