def factor_finder(userinput) :
        remainder = userinput % factors
        if remainder == 0 :
            factor = factors
            return factor
        else :
            return 'no_perfect_factor'
done1 = True
print()
print('             >>>>>>  Highest Common Factor calulator  <<<<<<')
print()
print('------------------------------------------------------------------------')
print()
while done1 :
       done2 = True
       factors = 1
       highest_common_factor = 1
       result1 = 'na'
       result2 = 'na'
       result3 = 'na'
       result4 = 'na'
       result5 = 'na'
       result6 = 'na'
       result7 = 'na'
       result8 = 'na'
       result9 = 'na'
       result10 = 'na'
       result11 = 'na'
       userinput1 = eval(input('>> Please enter a number : '))
       userinput2 = eval(input('>> Please enter another number : '))
       if userinput1 < userinput2 :
               smaller_number = userinput1
       else :
               smaller_number = userinput2
       userinput4 = eval(input('>> Please enter another number or enter "c" to calculate : '))
       if userinput4 == "c" :
               userinput4 = 0
               userinput5 = 0
               userinput6 = 0
               userinput7 = 0
               userinput8 = 0
               userinput9 = 0
               userinput10 = 0
               userinput11 = 0
       else :
               if smaller_number < userinput4 :
                       smaller_number = smaller_number
               else :
                       smaller_number = userinput4
               userinput5 = eval(input('>> Please enter another number or enter "c" to calculate : '))
               if userinput5 == "c" :
                       userinput5 = 0
                       userinput6 = 0
                       userinput7 = 0
                       userinput8 = 0
                       userinput9 = 0
                       userinput10 = 0
                       userinput11 = 0
               else :
                       if smaller_number < userinput5 :
                               smaller_number = smaller_number
                       else :
                               smaller_number = userinput5
                       userinput6 = eval(input('>> Please enter another number or enter "c" to calculate : '))
                       if userinput6 == "c" :
                               userinput6 = 0
                               userinput7 = 0
                               userinput8 = 0
                               userinput9 = 0
                               userinput10 = 0
                               userinput11 = 0
                       else :
                               if smaller_number < userinput6 :
                                       smaller_number = smaller_number
                               else :
                                       smaller_number = userinput6
                               userinput7 = eval(input('>> Please enter another number or enter "c" to calculate : '))
                               if userinput7 == "c" :
                                       userinput7 = 0
                                       userinput8 = 0
                                       userinput9 = 0
                                       userinput10 = 0
                                       userinput11 = 0
                               else :
                                       if smaller_number < userinput7 :
                                               smaller_number = smaller_number
                                       else :
                                               smaller_number = userinput7
                                       userinput8 = eval(input('>> Please enter another number or enter "c" to calculate : '))
                                       if userinput8 == "c" :
                                               userinput8 = 0
                                               userinput9 = 0
                                               userinput10 = 0
                                               userinput11 = 0
                                       else :
                                               if smaller_number < userinput8 :
                                                       smaller_number = smaller_number
                                               else :
                                                       smaller_number = userinput8
                                               userinput9 = eval(input('>> Please enter another number or enter "c" to calculate : '))
                                               if userinput9 == "c" :
                                                       userinput9 = 0
                                                       userinput10 = 0
                                                       userinput11 = 0
                                               else :
                                                       if smaller_number < userinput9 :
                                                               smaller_number = smaller_number
                                                       else :
                                                               smaller_number = userinput9
                                                       userinput10 = eval(input('>> Please enter another number or enter "c" to calculate : '))
                                                       if userinput10 == "c" :
                                                               userinput10 = 0
                                                               userinput11 = 0
                                                       else :
                                                               if smaller_number < userinput10 :
                                                                       smaller_number = smaller_number
                                                               else :
                                                                       smaller_number = userinput10
                                                               userinput11 = eval(input('>> Please enter another number or enter "c" to calculate : '))
                                                               if userinput11 == "c" :
                                                                       userinput11 = 0
       while factors <= smaller_number :
               result1 = factor_finder(userinput1)
               result2 = factor_finder(userinput2)
               if userinput4 != 0 :
                       result3 = factor_finder(userinput4)
               if userinput5 != 0 :
                       result4 = factor_finder(userinput5)
               if userinput6 != 0 :
                       result5 = factor_finder(userinput6)
               if userinput7 != 0 :
                       result6 = factor_finder(userinput7)
               if userinput8 != 0 :
                       result7 = factor_finder(userinput8)
               if userinput9 != 0 :
                       result8 = factor_finder(userinput9)
               if userinput10 != 0 :
                       result9 = factor_finder(userinput10)
               if userinput11 != 0 :
                       result10 = factor_finder(userinput11)
               if result1 == result2 and result1 != 'no_perfect_factor' and userinput4 == userinput5 == userinput6 == userinput7 == userinput8 == userinput9 == userinput10 == userinput11 :
                       highest_common_factor = result1
               if result1 == result2 == result3 and result1 != 'no_perfect_factor' and userinput5 == userinput6 == userinput7 == userinput8 == userinput9 == userinput10 == userinput11 :
                       highest_common_factor = result1
               if result1 == result2 == result3 == result4 and result1 != 'no_perfect_factor' and userinput6 == userinput7 == userinput8 == userinput9 == userinput10 == userinput11 :
                       highest_common_factor = result1
               if result1 == result2 == result3 == result4 == result5 and result1 != 'no_perfect_factor' and userinput7 == userinput8 == userinput9 == userinput10 == userinput11 :
                       highest_common_factor = result1
               if result1 == result2 == result3 == result4 == result5 == result6 and result1 != 'no_perfect_factor' and userinput8 == userinput9 == userinput10 == userinput11 :
                       highest_common_factor = result1
               if result1 == result2 == result3 == result4 == result5 == result6 == result7 and result1 != 'no_perfect_factor' and userinput9 == userinput10 == userinput11 :
                       highest_common_factor = result1
               if result1 == result2 == result3 == result4 == result5 == result6 == result7 == result8 and result1 != 'no_perfect_factor' and userinput10 == userinput11 :
                       highest_common_factor = result1
               if result1 == result2 == result3 == result4 == result5 == result6 == result7 == result8 == result9 and result1 != 'no_perfect_factor' and userinput11 == 0 :
                       highest_common_factor = result1
               if result1 == result2 == result3 == result4 == result5 == result6 == result7 == result8 == result9 == result10 and result1 != 'no_perfect_factor' :
                       highest_common_factor = result1
               factors = factors + 1 
       print()
       print('* Highest common factor is : ',highest_common_factor)
       print('------------------------------------------------------------------------')
       print()
       while done2 :
               userinput3 = input('>> Press C to continue or Press E to exit : ')
               if userinput3 == 'c' or userinput3 == 'C' :
                       done2 = False
                       print()
                       print('------------------------------------------------------------------------')
                       print()
               elif userinput3 == 'e' or userinput3 == 'E' :
                       print()
                       done2 = False
                       done1 = False
               else :
                       print()
                       print('                         >> Incorrect input ! <<')
                       print()
