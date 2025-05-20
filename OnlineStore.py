print("Welcome to Ravi's Online Store")
print("Select\n1 for Fashion\n2 for Electronics\n3 for Food")
userinput1=int(input("Enter the number: "))
if userinput1 <= 0 or userinput1 >3:
    print("Enter a valid input")  
if userinput1==1:
    print("You have selected Fashion")
    print("Select\n1 for Men\n2 for Women")
    userinput2=int(input("Enter the number: "))
    if userinput2 <= 0 or userinput2 >2:
            print("Enter a valid input") 

    if userinput2==1:
        print("You have Selected Men Fashion")
        print("Select\n1 for Shirts\n2 for trousers")
        userinput3=int(input("Enter the number: "))
        if userinput3 <= 0 or userinput3 >2:
             print("Enter a valid input")
        if userinput3==1:
            print("You have Selected Shirts")
            print("Select\n1 for Size S\n2 for Size M\n3 for Size L")
            userinput4=int(input("Enter the number: "))
            if userinput4 <= 0 or userinput4 >2:
                 print("Enter a valid input")
            elif userinput4 == 1:
                print("You have Selected Size S shirt")
            elif userinput4 == 2:
                print("You have Selected Size M shirt")
            elif userinput4 == 3:
                print("You have Selected Size L shirt")
            print("Shirt Purchased")

        elif userinput3==2:
            print("You have Selected Trousers")
            print("Select\n1 for Size 30\n2 for Size 34\n3 for Size 38")
            userinput5=int(input("Enter the number: "))
            if userinput5 <= 0 or userinput5 >2:
                print("Enter a valid input")
            if userinput5 == 1:
                print("You have Selected Size 30 trouser")
            elif userinput5 == 2:
                print("You have Selected Size 34 trouser")
            elif userinput5 == 3:
                print("You have Selected Size 38 trouser")
            print("Trouser Purchased")
    
    if userinput2==2:
        print("You have Selected Women Fashion")
        print("Select\n1 for Tops\n2 for Geans")
        userinput6=int(input("Enter the number: "))
        if userinput6 <= 0 or userinput6 >2:
             print("Enter a valid input")
        if userinput6==1:
            print("You have Selected Tops")
            print("Select\n1 for Size S\n2 for Size M\n3 for Size L")
            userinput7=int(input("Enter the number: "))
            if userinput7 <= 0 or userinput7 >2:
                 print("Enter a valid input")
            elif userinput7 == 1:
                print("You have Selected Size S Top")
            elif userinput7 == 2:
                print("You have Selected Size M Top")
            elif userinput7 == 3:
                print("You have Selected Size L Top")
            print("Top Purchased")

        elif userinput6==2:
            print("You have Selected Trousers")
            print("Select\n1 for Size 30\n2 for Size 34\n3 for Size 38")
            userinput8=int(input("Enter the number: "))
            if userinput8 <= 0 or userinput8 >2:
                print("Enter a valid input")
            if userinput8 == 1:
                print("You have Selected Size 30 trouser")
            elif userinput8 == 2:
                print("You have Selected Size 34 trouser")
            elif userinput8 == 3:
                print("You have Selected Size 38 trouser")
            print("Trouser Purchased")

if userinput1==2:
    print("You have selected Electronics")
    print("Select\n1 for Mobiles\n2 for Laptops")
    userinput9=int(input("Enter the number: "))
if userinput1 <= 0 or userinput1 >3:
    print("Enter a valid input")

if userinput9==1:
        print("You have Selected Mobiles")
        print("Select\n1 for Samsung\n2 for Oneplus\n3 for Nokia")
        userinput10=int(input("Enter the number: "))
        if userinput10 <= 0 or userinput10 >3:
             print("Enter a valid input")
        if userinput10==1:
            print("You have Selected Samsung Mobiles")
            print("Select\n1 for 4GB Ram\n2 for 8GB Ram\n3 for 16GB Ram")
            userinput11=int(input("Enter the number: "))
            if userinput11 <= 0 or userinput11 >3:
                 print("Enter a valid input")
            print("Select\n1 for 64GB Storage\n2 for 128GB Storage\n3 for 256GB Storage")
            userinput12=int(input("Enter the number: "))
            if userinput12 <= 0 or userinput12 >3:
                 print("Enter a valid input")
            elif userinput11 == 1 and userinput12 == 1:
                print("You have Selected 4GB Ram and 64GB Storage Samsung Mobile ")
            elif userinput11 == 1 and userinput12 == 2:
                print("You have Selected 4GB Ram and 128GB Storage Samsung Mobile ")
            elif userinput11 == 1 and userinput12 == 3:
                print("You have Selected 4GB Ram and 256GB Storage Samsung Mobile ")
            elif userinput11 == 2 and userinput12 == 1:
                print("You have Selected 6GB Ram and 64GB Storage Samsung Mobile ")
            elif userinput11 == 2 and userinput12 == 2:
                print("You have Selected 8GB Ram and 128GB Storage Samsung Mobile ")
            elif userinput11 == 2 and userinput12 == 3:
                print("You have Selected 16GB Ram and 256GB Storage Samsung Mobile ")
            elif userinput11 == 3 and userinput12 == 1:
                print("You have Selected 16GB Ram and 64GB Storage Samsung Mobile ")
            elif userinput11 == 3 and userinput12 == 2:
                print("You have Selected 16GB Ram and 256GB Storage Samsung Mobile ")
            elif userinput11 == 3 and userinput12 == 3:
                print("You have Selected 16GB Ram and 256GB Storage Samsung Mobile ")
            print("Samsung Mobile Purchased")
        
        if userinput10==2:
            print("You have Selected Oneplus Mobiles")
            print("Select\n1 for 4GB Ram\n2 for 8GB Ram\n3 for 16GB Ram")
            userinput13=int(input("Enter the number: "))
            if userinput13 <= 0 or userinput13 >3:
                 print("Enter a valid input")
            print("Select\n1 for 64GB Storage\n2 for 128GB Storage\n3 for 256GB Storage")
            userinput14=int(input("Enter the number: "))
            if userinput14 <= 0 or userinput14 >3:
                 print("Enter a valid input")
            elif userinput13 == 1 and userinput14 == 1:
                print("You have Selected 4GB Ram and 64GB Storage  ")
            elif userinput13 == 1 and userinput14 == 2:
                print("You have Selected 4GB Ram and 128GB Storage  ")
            elif userinput13 == 1 and userinput14 == 3:
                print("You have Selected 4GB Ram and 256GB Storage ")
            elif userinput13 == 2 and userinput14 == 1:
                print("You have Selected 6GB Ram and 64GB Storage  ")
            elif userinput13 == 2 and userinput14 == 2:
                print("You have Selected 8GB Ram and 128GB Storage  ")
            elif userinput13 == 2 and userinput14 == 3:
                print("You have Selected 16GB Ram and 256GB Storage  ")
            elif userinput13 == 3 and userinput14 == 1:
                print("You have Selected 16GB Ram and 64GB Storage ")
            elif userinput13 == 3 and userinput14 == 2:
                print("You have Selected 16GB Ram and 256GB Storage ")
            elif userinput13 == 3 and userinput14 == 3:
                print("You have Selected 16GB Ram and 256GB Storage  ")
            print("Oneplus Mobile Purchased")
        
        if userinput10==3:
            print("You have Selected Nokia Mobiles")
            print("Select\n1 for 4GB Ram\n2 for 8GB Ram\n3 for 16GB Ram")
            userinput15=int(input("Enter the number: "))
            if userinput15 <= 0 or userinput15 >3:
                 print("Enter a valid input")
            print("Select\n1 for 64GB Storage\n2 for 128GB Storage\n3 for 256GB Storage")
            userinput16=int(input("Enter the number: "))
            if userinput16 <= 0 or userinput16 >2:
                 print("Enter a valid input")
            elif userinput15 == 1 and userinput16 == 1:
                print("You have Selected 4GB Ram and 64GB Storage  ")
            elif userinput15 == 1 and userinput16 == 2:
                print("You have Selected 4GB Ram and 128GB Storage  ")
            elif userinput15 == 1 and userinput16 == 3:
                print("You have Selected 4GB Ram and 256GB Storage ")
            elif userinput15 == 2 and userinput16 == 1:
                print("You have Selected 6GB Ram and 64GB Storage  ")
            elif userinput15 == 2 and userinput16 == 2:
                print("You have Selected 8GB Ram and 128GB Storage  ")
            elif userinput15 == 2 and userinput16 == 3:
                print("You have Selected 16GB Ram and 256GB Storage  ")
            elif userinput15 == 3 and userinput16 == 1:
                print("You have Selected 16GB Ram and 64GB Storage ")
            elif userinput15 == 3 and userinput16 == 2:
                print("You have Selected 16GB Ram and 256GB Storage ")
            elif userinput15 == 3 and userinput16 == 3:
                print("You have Selected 16GB Ram and 256GB Storage  ")
            print("Nokia Mobile Purchased")

if userinput9==2:
        print("You have Selected Laptops")
        print("Select\n1 for Samsung\n2 for MacBook\n3 for Dell")
        userinput17=int(input("Enter the number: "))
        if userinput17 <= 0 or userinput17 >3:
             print("Enter a valid input")
        if userinput17==1:
            print("You have Selected Samsung Laptops")
            print("Select\n1 for 4GB Ram\n2 for 8GB Ram\n3 for 16GB Ram")
            userinput11=int(input("Enter the number: "))
            if userinput11 <= 0 or userinput11 >3:
                 print("Enter a valid input")
            print("Select\n1 for 64GB Storage\n2 for 128GB Storage\n3 for 256GB Storage")
            userinput12=int(input("Enter the number: "))
            if userinput12 <= 0 or userinput12 >3:
                 print("Enter a valid input")
            userinput11=int(input("Enter the number: "))
            if userinput11 <= 0 or userinput11 >3:
                 print("Enter a valid input")
            print("Select\n1 for Intel i3\n2 for Intel i6\n3 for Intel")
            userinput12=int(input("Enter the number: "))
            if userinput12 <= 0 or userinput12 >3:
                 print("Enter a valid input")
            elif userinput11 == 1 and userinput12 == 1:
                print("You have Selected 4GB Ram and 64GB Storage Samsung Mobile ")
            elif userinput11 == 1 and userinput12 == 2:
                print("You have Selected 4GB Ram and 128GB Storage Samsung Mobile ")
            elif userinput11 == 1 and userinput12 == 3:
                print("You have Selected 4GB Ram and 256GB Storage Samsung Mobile ")
            elif userinput11 == 2 and userinput12 == 1:
                print("You have Selected 6GB Ram and 64GB Storage Samsung Mobile ")
            elif userinput11 == 2 and userinput12 == 2:
                print("You have Selected 8GB Ram and 128GB Storage Samsung Mobile ")
            elif userinput11 == 2 and userinput12 == 3:
                print("You have Selected 16GB Ram and 256GB Storage Samsung Mobile ")
            elif userinput11 == 3 and userinput12 == 1:
                print("You have Selected 16GB Ram and 64GB Storage Samsung Mobile ")
            elif userinput11 == 3 and userinput12 == 2:
                print("You have Selected 16GB Ram and 256GB Storage Samsung Mobile ")
            elif userinput11 == 3 and userinput12 == 3:
                print("You have Selected 16GB Ram and 256GB Storage Samsung Mobile ")
            print("Samsung Mobile Purchased")
        
        if userinput10==2:
            print("You have Selected Oneplus Mobiles")
            print("Select\n1 for 4GB Ram\n2 for 8GB Ram\n3 for 16GB Ram")
            userinput13=int(input("Enter the number: "))
            if userinput13 <= 0 or userinput13 >3:
                 print("Enter a valid input")
            print("Select\n1 for 64GB Storage\n2 for 128GB Storage\n3 for 256GB Storage")
            userinput14=int(input("Enter the number: "))
            if userinput14 <= 0 or userinput14 >3:
                 print("Enter a valid input")
            elif userinput13 == 1 and userinput14 == 1:
                print("You have Selected 4GB Ram and 64GB Storage  ")
            elif userinput13 == 1 and userinput14 == 2:
                print("You have Selected 4GB Ram and 128GB Storage  ")
            elif userinput13 == 1 and userinput14 == 3:
                print("You have Selected 4GB Ram and 256GB Storage ")
            elif userinput13 == 2 and userinput14 == 1:
                print("You have Selected 6GB Ram and 64GB Storage  ")
            elif userinput13 == 2 and userinput14 == 2:
                print("You have Selected 8GB Ram and 128GB Storage  ")
            elif userinput13 == 2 and userinput14 == 3:
                print("You have Selected 16GB Ram and 256GB Storage  ")
            elif userinput13 == 3 and userinput14 == 1:
                print("You have Selected 16GB Ram and 64GB Storage ")
            elif userinput13 == 3 and userinput14 == 2:
                print("You have Selected 16GB Ram and 256GB Storage ")
            elif userinput13 == 3 and userinput14 == 3:
                print("You have Selected 16GB Ram and 256GB Storage  ")
            print("Oneplus Mobile Purchased")
        
        if userinput10==3:
            print("You have Selected Nokia Mobiles")
            print("Select\n1 for 4GB Ram\n2 for 8GB Ram\n3 for 16GB Ram")
            userinput15=int(input("Enter the number: "))
            if userinput15 <= 0 or userinput15 >3:
                 print("Enter a valid input")
            print("Select\n1 for 64GB Storage\n2 for 128GB Storage\n3 for 256GB Storage")
            userinput16=int(input("Enter the number: "))
            if userinput16 <= 0 or userinput16 >2:
                 print("Enter a valid input")
            elif userinput15 == 1 and userinput16 == 1:
                print("You have Selected 4GB Ram and 64GB Storage  ")
            elif userinput15 == 1 and userinput16 == 2:
                print("You have Selected 4GB Ram and 128GB Storage  ")
            elif userinput15 == 1 and userinput16 == 3:
                print("You have Selected 4GB Ram and 256GB Storage ")
            elif userinput15 == 2 and userinput16 == 1:
                print("You have Selected 6GB Ram and 64GB Storage  ")
            elif userinput15 == 2 and userinput16 == 2:
                print("You have Selected 8GB Ram and 128GB Storage  ")
            elif userinput15 == 2 and userinput16 == 3:
                print("You have Selected 16GB Ram and 256GB Storage  ")
            elif userinput15 == 3 and userinput16 == 1:
                print("You have Selected 16GB Ram and 64GB Storage ")
            elif userinput15 == 3 and userinput16 == 2:
                print("You have Selected 16GB Ram and 256GB Storage ")
            elif userinput15 == 3 and userinput16 == 3:
                print("You have Selected 16GB Ram and 256GB Storage  ")
            print("Nokia Mobile Purchased")
