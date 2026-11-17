import time

text = "This is my first Individual Project as first year student of Association In Computer Technology from CCST."

for mytext in text :
    print(mytext, end="", flush=True)
    time.sleep(0.1)

print(" ")
print("~-~"*45)
print("                              P Y T H O N   T U T O R I A L   B Y : M A N D A L  K E V I N  P E R E Z")
print("~-~"*45)
print(" ")

Strt = input("Enter the word [START] to proceed :").upper()
print(" ")
if Strt == "START" :
   print("Hello welcome! (˙ᗜ˙)/")
   print("I'm Verity, your guiding assistant in this website.")
   print("This website have some basics PYTHON TUTORIAL, where you can learn")
   print("(BASIC SYNTAX, VARIABLES, DATA TYPES, AND ETC.)")
   print("Let's start your journey and have fun, but you must Enter your name first.")
   print(" ")

else :
    print("PLEASE ENTER [START].")
    exit()
print("_-"*68)
print(" ")
Fn1 =input("First Name : ")
Fn2 =input("Last  Name : ")
print(" ")
print("_-"*68)
print(" ")
print(f"Hi {Fn1}, down below there is lessons waiting for you. You can able to choose")
print("whatever you want to learn. I'll put the code, decide either PICK or "
      "LEARN STEP BY STEP from chapter 1 - 7. You can")
print("see it down below. Also after you finished, you will get quiz,test or game.")
print("I suggest [PICK] because it has a game, quiz or test. [LSBS] Don't have one of them. ")
print("After you finish i'll ask you again if you want to repeat. Put [Y] to proceed.")
print("Put [N] and you'll see. ")
print("That's all. GOOD LUCK! (◠‿◠).")
print(" ")
print("_-"*68)
print(" ")
print(">>>>>>>>>>>>> P Y T H O N   L E S S O N S <<<<<<<<<<<<<")
print(" ")
print("CHAPTER 1 (INTRODUCTION TO PROGRAMMING         ) - [1]")
print("CHAPTER 2 (PYTHON BASIC SYNTAX                 ) - [2]")
print("CHAPTER 3 (ARITHMETIC OPERATORS AND EXPRESSIONS) - [3]")
print("CHAPTER 4 (BASIC INPUT AND OUTPUT              ) - [4]")
print("CHAPTER 5 (CONDITIONAL STATEMENT               ) - [5]")
print("CHAPTER 7 (LOGICAL OPERATOR                    ) - [6]")
print("CHAPTER 7 (LOOPS                               ) - [7]")
print("\n>>>>>>>>>>>>>>>>>> T U T O R I A L <<<<<<<<<<<<<<<<<<<")
print(" ")
print("_-"*68)
print(" ")

pick = input("You want to learn step by step? or pick a lesson? (PICK/LSBS) : ").upper()
if pick == "PICK" :
   print(" ")

   print("*"*62)
   print(" ")
   print("That's great! it means you have experience already. ꒰ঌ(˶ˆᗜˆ˵)໒꒱")
   print(" ")
   print("*"*62)

   print(" ")
   choice = input("Choose Chapter 1 to 7 :")
   print(" ")

   print("_-" * 68)
   print("GOOD LUCK AND HAVE FUN! ദ്ദി*ˊᗜˋ*)")
   print("_-" * 68)
   print(" ")

   if choice == "1" :
      print("__________________________________________________________________________________________")
      print("|                                                                                        |")
      print("|      C H A P T E R   1    I N T R O D U C T I O N    T O    P R O G R A M M I N G      |")
      print("|________________________________________________________________________________________|\n")

      print("Do you have any idea what's programming language is? if not, PROGRAMMING LANGUAGE is a special language")
      print("that computers understand and use to perform task.(。•̀ᴗ-)✧\n")
      print("Anyways PYTHON PROGRAMMING is widely used around the world because it was easy to learn, simple and readable.")
      print("It was created by Guido Van Rossum in 1991.\n")
      print("What do you need to start python?\n")
      print("_________________________________________________________________________")
      print("|`````P R O F E S S I O N A L   I D E S / C O D E S   E D I T O R S`````|")
      print("|_______________________________________________________________________|")
      print("| PYCHARM BY JET BRAINS.                                                |")
      print("| VS CODE  (VISUAL STUDIO CODE).                                        |")
      print("| JUPYTER NOTEBOOK/JUPYTER LAB.                                         |")
      print("|_______________________________________________________________________|\n")
      print("That's all for Chapter 1.")
      print("Easy Right? RIGHTTTTTTTTTTTTTTTT?. ＼(ˇ∇ˇ)／\n")
      print("_-" * 68)
      print("                                                         _________________________    ")
      print("                    /|      _____          _____       |   |     |     |    | |  |   ")
      print("     ,-----,       /  |____/__|__|_    ___/__|__|___   |___|_____|_____|____|_|___|  ")
      print("  ,--'---:---`--, /  |  _     |     `| |      |      `| |                    | |    | ")
      print(" ==(o)-----(o)==J    `(o)-------(o)=   `(o)------(o)'   `--(o)(o)--------------(o)--'  ")
      print("`````````````````````````````````````````````````````````````````````````````````````")
      print("_-" * 68)
      print("========== L O A D I N G   P L E A S E   W A I T ==========................................................")
      print("_-" * 68)
      print(" ")
      quizc1 = input("Would you like to take a quiz? (YES/NO) :").upper()


      pass_score = 3
      if quizc1 == "YES":

          score = 0
          print("[------------------------------------------------------------------------]")
          print("| This quiz has 5 items. Write T if True. F if False.                    |")
          print("|________________________________________________________________________|")

          answer = input("1. Python is not part of special language/programming language. Answer :\n").upper()
          if answer == "F" :
           score += 1
          answer = input("2.Guido van Created python in 1992. Answer :\n").upper()
          if answer == "F" :
           score += 1
          answer = input("3.Python is readable, easy to learn and simple. Answer :\n").upper()
          if answer == "T":
           score += 1
          answer = input("4.Pycharm is one of the ides and professional code editors.Answer :\n").upper()
          if answer == "T":
           score += 1
          answer = input("5.Computers don't understand programming language. Answer :\n").upper()
          if answer == "F":
           score += 1

          print(" ")
          print("_-" * 68)
          print(" ")
          print(" __________________________________________________")
          print(" |   *************************                    |")
          print(f" |   *  You got {score} / 5!       *                    |")
          print(" |   *************************                    |\n")
          print(" |________________________________________________|")


          if score >= pass_score :

              print(" | Congrats! You passed the quiz! d-(^_^)z        |")
              print(" |________________________________________________|")
              print(" ")
              print("_-" * 68)
          else :
           print(" | You Failed, Keep Going! (9'-')9                |")
           print(" |________________________________________________|")
           print(" ")
           print("_-" * 68)
      elif quizc1 == "NO" :
          print("I Understand.")
      else :
          print("Put YES or NO")

   elif choice == "2" :
       print("__________________________________________________________________________________________")
       print("|                                                                                        |")
       print("|      C H A P T E R   2    P Y T H O N   B A S I C   S Y N T A X                        |")
       print("|________________________________________________________________________________________|\n")

       print("What is SYNTAX.\n")
       print("SYNTAX refers to the set of rules that tells us how correctly write a program in Python.\n")
       print("=--PYTHON SYNTAX--=")
       print("These things is really important to understand, remember this. Python is case sensitive ")
       print("because python treats upper and lower case differently.Also Python need Indentation or called")
       print("spaces to define blocks of code.  <(-^,^-)=b \n")
       print("For example....\n")
       print("Remember the ('') Imagine this as quotation mark. Thank you for understanding!\n")
       print("__________________________________________________________________________________________")
       print("|  Python Case Sensitive.                                                                |")
       print("|                                                                                        |")
       print("|  (1). name = ''Kevin''               (2). name = ''Kevin''                             |")
       print("|       print(Name)                       print(name)                                    |")
       print("|                                                                                        |")
       print("|    The number  1 is wrong. Number 2 is correct. Why?                                   |")
       print("|    because even though the word NAME is same.                                          |")
       print("|    You can see that, 1 has lowercase variable storage.                                 |")
       print("|    But has upper case with print(Name).                                                |")
       print("|                                                                                        |")
       print("|    Keyword : If it's lower. It's lower. If it's upper. It's upper.                     |")
       print("|                                                                                        |")
       print("|  Indentations(Spaces).                                                                 |")
       print("|                                                                                        |")
       print("|   (1). age = 18                    (2). age = 18                                       |")
       print("|        if age >= 18 :                   if age >= 18 :                                 |")
       print("|          print(''Adult'')               print(''Adult'')                               |")
       print("|                                                                                        |")
       print("|   Number 2 is incorrect because it is not intended or he doesn't have spaces           |")
       print("|   to get inside the block. While number 1 has spaces that's why it's intended.         |")
       print("|                                                                                        |")
       print("|    Keyword: Use spaces and make sure it is align perfectly in your coding              |")
       print("|             to get intended.                                                           |")
       print("|________________________________________________________________________________________|\n")

       print("_-" * 68)
       print("."*136)
       print("_-" * 68)
       print("                                                      __  _")
       print("      ...........................                     | `/ |     ")
       print("      |                         |                      |__`!   ")
       print("      | PRINTING                |_  ___                / ,' `-.__________________   ")
       print("      |           OUTPUT        | -    ________________'-'|_____                LI`-.   ")
       print("      ...........................                         <____()-=O=O=O=O=O=[]====--)")
       print("                                                              `.___ ,-----,_______...-'")
       print("                                                                   /    .'")
       print("                                                                  /   .'")
       print("                                                                 /  .'  ")
       print("                                                                `-'")
       print("_-" * 68)
       print("." * 136)
       print("_-" * 68)

       print("\nNow let's proceed to PRINTING OUTPUT.\n")
       print("PRINTING OUTPUT - It displayed information through your screen.")
       print("PRINTING NUMBERS - You can put numbers without quotation marks but there's different.See")
       print("the example below.\n")
       print("Remember the ('') Imagine this as quotation mark. Thank you for understanding!\n")
       print("__________________________________________________________________________________________")
       print("|                                                                                        |")
       print("|      (1). print(100)            (2). print(''500'')                                    |")
       print("|           print(25.5)                print(''112'')                                    |")
       print("|                                                                                        |")
       print("|      1 and 2 are both correct, they just have different data types.                    |")
       print("|      The number 1 in line one is called INTEGERS. Line two is called FLOAT.            |")
       print("|      While number 2 is called STRING because it has quotation mark.                    |")
       print("|                                                                                        |")
       print("|                                                                                        |")
       print("|                                                                                        |")
       print("|________________________________________________________________________________________|\n")

       print("() - Open and close Parenthesis Is the reason why program contain to be displayed.")
       print("('') - Quotation mark is the sign for string because without quotation mark,")
       print("you get either error or variables.")
       print("Value - This is (STRING, NUMBER, VARIABLE and ETC.)\n")
       print("_-" * 68)
       print("\n                        ( -_•)ᡕᠵデᡁ᠊╾━--- P Y T H O N   C O M M E N T S.\n")
       print("_-" * 68)
       print("PYTHON COMMENTS is easy to remember just put HASHTAG (#) and that's it you have comment. ദ്ദി ˉ͈̀꒳ˉ͈́ )✧")
       print("Kidding aside. there is two types of comments.")
       print("The first one is SINGLE LINE COMMENT. The second one is MULTI LINE COMMENTS.")
       print("\nRemember the ('') Imagine this as quotation mark. Thank you for understanding!\n")
       print("__________________________________________________________________________")
       print("|``````````````````````P Y T H O N   C O M M E N T S`````````````````````|")
       print("|________________________________________________________________________|")
       print("|                                                                        |")
       print("| SINGLE LINE COMMENTS = (#)                                             |")
       print("|                                                                        |")
       print("| MULTI LINE COMMENTS = ('''''') at top and bottom                       |")
       print("|                                                                        |")
       print("|   Take note: Comments are ignored by python, and used to               |")
       print("|              explain   the code.                                       |")
       print("|________________________________________________________________________|\n")
       print("_-" * 68)
       print("." * 136)
       print("_-" * 68)
       print("\n          _  _")
       print("         ( `   )_")
       print("        (    )    `)")
       print("      (_   (_ .  _) _)")
       print("                                  V A R I A B L E S ,                                                ")
       print("                                         C O N S T A N T S ,                                     ")
       print("           _                                     A N D ")
       print("         -=|`|                         D A T A   T Y P E S.")
       print("     || ____|_|__                                                                 _")
       print("   -=|c`         L`)                                  -----                       (  )")
       print("      `~~~~~| |~~`                                                             ( `  ) . )")
       print("        -==| |                        - - - - -                              (_, _(  ,_)_)")
       print("          '-'                                                                    \n")
       print("_-" * 68)
       print("." * 136)
       print("_-" * 68)
       print("\nWhat is VARIABLES?\n")
       print("VARIABLES is the storage location where you can  keep data in program.\n")
       print("TAKE NOTE :")
       print("Variables can have short name like (a,b,c) or more like (name, total_val, char).")
       print("Variables can't start with numbers. It starts with underscore(_) or letter.")
       print("Like i said before. Python case is sensitive. If you have variable (NAME, name), ")
       print("this two variable are from different data.\n")
       print("\nRemember the ('') Imagine this as quotation mark. Thank you for understanding!\n")
       print("__________________________________________________________________________________________")
       print("| In programming we store data in variables. we put value  to variable,                  |")
       print("| using ASSIGNMENT OPERATOR.                                                             |")
       print("|                                                                                        |")
       print("| For example :                                                                          |")
       print("|                                                                                        |")
       print("|           Character_one = ''Tung Tung Sahur''                                          |")
       print("|                   ^                  ^                                                 |")
       print("|          #This is variable,     #This is Value the data we store in variable.          |")
       print("|           the  name we use to present data.             (It can be text, num and etc). |")
       print("|                                                                                        |")
       print("|           Is that Clear? <(-^,^-)=b                                                    |")
       print("|                                                                                        |")
       print("| Also you can print multiple variables using add(+) or comma(,).                        |")
       print("|                                                                                        |")
       print("| For Example :                                                                          |")
       print("|           a = ''Keep''                                                                 |")
       print("|           b = ''Going''                                                                |")
       print("|           c = ''embrace fear''                                                         |")
       print("|                                                                                        |")
       print("|           print (a + b + c) > output : Keep going embrace fear                         |")
       print("|           print (a, b, c)   > output : Keep going embrace fear                         |")
       print("|________________________________________________________________________________________|\n")
       print("_-" * 68)
       print("\n                        ( -_•)ᡕᠵデᡁ᠊╾━--- D A T A   T Y P E S   I N    P Y T H O N.\n")
       print("_-" * 68)
       print("DATA TYPES - Tells the python on what kind of variable we stored.\n")
       print("Lets focus on :\n")
       print("STRING - More on text inside quotation mark.")
       print("Example : (''Kevin'' , ''Mandal'' , ''Perez'') \n")
       print("INTEGERS(int) - More on Whole numbers. ")
       print("Example : (12, 22 , -18)\n")
       print("float - It has decimal point.")
       print("Example : (20.07, 18.22, -17.2)\n")
       print("bool(boolean) - Represent one of two value it's either TRUE or FALSE.")
       print("Example : (TRUE, FALSE)\n")
       print("This is the example of how it works.")
       print("__________________________________________________________________________________________")
       print("|                                                                                        |")
       print("|    name = ''Kevin''               >  String                                            |")
       print("|    age = 18                       >  Integers                                          |")
       print("|    grade_inpython = 61.30         >  Float                                             |")
       print("|    is_enrolled = False            >  Boolean                                           |")
       print("|                                                                                        |")
       print("|    print(name)                                                                         |")
       print("|    print(age)                                                                          |")
       print("|    print(grade_inpython)                                                               |")
       print("|    print(is_enrolled)                                                                  |")
       print("|                                                                                        |")
       print("|________________________________________________________________________________________|\n")
       print("_-" * 68)
       print("       __|__          ============================================           __|__            ")
       print("--------(_)--------   L O A D I N G    P L E A S E    W A I T.....    --------(_)--------")
       print("  O  O       O  O     ============================================      O  O       O  O            ")
       print("_-" * 68)
       print("T H A T ' S   T H E   E N D  O F   C H A P T E R   T W O ")
       print("_-" * 68)
       quizc2 = input("Would you like to take a quiz? (YES/NO) :").upper()

       pass_score = 9
       if quizc2 == "YES" :
           score = 0
           print("[------------------------------------------------------------------------]")
           print("| This quiz have 15 items. Multiple choice and identification.           |")
           print("|________________________________________________________________________|")

           print("\n1.Which one is correct, see the table below.")
           print("__________________________________________________________________________________________")
           print("|   A.                      B.                                                           |")
           print("|   Name = 'kevin'          name = ''kevin''                                             |")
           print("|   print(name)             print(name)                                                  |")
           print("__________________________________________________________________________________________\n")

           answer = input("Answer A or B? : ").upper()
           if answer == "B" :
               print("\nGreat that's Correct! {(^_^)}")
               print("__________________________________________________________________________________________\n")
               score += 1
           else:
               print("It's letter B. (-_-)")
               print("__________________________________________________________________________________________\n")

           print("\n2. You need spaces to get intended, this is called _______ .")
           answer = input("Answer : ").upper()

           if answer == "INDENTATIONS" or answer == "INDENTATION":
               print("\nGreat that's Correct! {(^_^)}")
               print("__________________________________________________________________________________________\n")
               score += 1
           else:
               print("\nWrong! The correct answer is Indentation.(-_-)")
               print("__________________________________________________________________________________________\n")

           print("\n3. Sign of multiple line comment.")
           print("A. ###")
           print("B. ''''''")
           print("C. #")

           answer = input("Answer : ").upper()
           if answer == "B" :
              print("\nGreat that's Correct! {(^_^)}")
              print("__________________________________________________________________________________________\n")
              score += 1
           else :
               print("Wrong answer. it's B. (-_-)")
               print("__________________________________________________________________________________________\n")

           print("\n4. Variables name can start with numbers.")
           print("A. Yes")
           print("B. Maybe")
           print("C. No")
           print("D. You can put whatever you like")

           answer = input("Answer : ").upper()
           if answer == "C" :
              print("\nGreat that's Correct! {(^_^)}")
              print("__________________________________________________________________________________________\n")
              score += 1
           else :
               print("\nWrong. The answer is C. (-_-)")
               print("__________________________________________________________________________________________\n")

           print("\n5. It is _________ where data can be kept in a program.")

           answer = input("Answer : ").upper()
           if answer == "VARIABLES" or answer == "VARIABLE":
               print("\nGreat that's Correct! {(^_^)}")
               print("__________________________________________________________________________________________\n")
               score += 1
           else:
               print("\nWrong! The correct answer is Variable. (-_-)")
               print("__________________________________________________________________________________________\n")

           print("\n6. It refers to the set of rules for writing a correct Python program.")
           print("A. Variables")
           print("B. Syntax")
           print("C. Comments")
           print("D. Indentation")

           answer = input("Answer : ").upper()
           if answer == "B":
               print("\nGreat that's Correct! {(^_^)}")
               print("__________________________________________________________________________________________\n")
               score += 1
           else:
               print("\nWrong! The correct answer is B. Syntax. (-_-)")
               print("__________________________________________________________________________________________\n")

           print("\n7. It is the storage location where you can keep data in a program.")
           print("A. Variable")
           print("B. String")
           print("C. Float")
           print("D. Boolean")

           answer = input("Answer : ").upper()
           if answer == "A":
               print("\nGreat that's Correct! {(^_^)}")
               print("__________________________________________________________________________________________\n")
               score += 1
           else:
               print("\nWrong! The correct answer is A. Variable. (-_-)")
               print("__________________________________________________________________________________________\n")

           print("\n8. We put value to variable using______.")
           print("A. Output")
           print("B. Integer")
           print("C. Comments")
           print("D. Assignment Operator")

           answer = input("Answer : ").upper()
           if answer == "D":
               print("\nGreat that's Correct! {(^_^)}")
               print("__________________________________________________________________________________________\n")
               score += 1
           else:
               print("\nWrong! The correct answer is D.Assignment Operator. (-_-)")
               print("__________________________________________________________________________________________\n")

           print("\n9. It represents text enclosed in quotation marks.")
           print("A. Integer")
           print("B. Boolean")
           print("C. Float")
           print("D. String")

           answer = input("Answer: ").upper()
           if answer == "D":
                print("\nGreat that's Correct! {(^_^)}")
                print("__________________________________________________________________________________________\n")
                score += 1
           else:
                print("\nWrong! The correct answer is D. String. (-_-)")
                print("__________________________________________________________________________________________\n")

           print("\n10. It represents one of two values: True or False.")
           print("A. Float")
           print("B. Boolean")
           print("C. String")
           print("D. Integer")

           answer = input("Answer : ").upper()
           if answer == "B":
               print("\nGreat that's Correct! {(^_^)}")
               print("__________________________________________________________________________________________\n")
               score += 1
           else:
               print("\nWrong! The correct answer is B. Boolean. (-_-)")
               print("__________________________________________________________________________________________\n")

           print("\n11. These are used to explain or describe code and are ignored during normal Python execution.")

           answer = input("Answer: ").upper()
           if answer == "COMMENTS" or answer == "COMMENT":
                print("Great that's Correct! {(^_^)}")
                print("__________________________________________________________________________________________\n")
                score += 1
           else:
                print("\nWrong! The correct answer is Comments.(-_-)")
                print("__________________________________________________________________________________________\n")


           print("\n12. It is a data type that has decimal point.")

           answer = input("Answer : ").upper()
           if answer == "FLOAT":
                print("\nGreat That's Correct! {(^_^)}")
                print("__________________________________________________________________________________________\n")
                score += 1
           else:
                print("\nWrong! The correct answer is float. (-_-)")
                print("__________________________________________________________________________________________\n")

           print("\n13. It's data types with whole number.")

           answer = input("Answer : ").upper()
           if answer == "INTEGERS" or answer == "INTEGER" or answer == "INT":
                print("\nGreat that's Correct! {(^_^)}")
                print("__________________________________________________________________________________________\n")
                score += 1
           else:
                print("\nWrong! The correct answer is Integer. (-_-)")
                print("__________________________________________________________________________________________\n")

           print("\n14. We store this in variable.")

           answer = input("Answer : ")
           if answer == "VALUE" or "VALUES" :
               print("\nGreat that's Correct! {(^_^)}")
               print("__________________________________________________________________________________________\n")
               score += 1
           else :
               print("\nWrong. It is VALUE (-_-)")
               print("__________________________________________________________________________________________\n")

           print("\n15. Name and name variable are same.")

           answer = input("\nAnswer (Yes/No) : ").upper
           if answer == "NO" :
               print("\nGreat that's Correct! {(^_^)}")
               print("__________________________________________________________________________________________\n")
               score += 1
           else :
               print("\nWrong. You it's not the same. (-_-)  ")
               print("__________________________________________________________________________________________\n")

           print(" ")
           print("_-" * 68)
           print(" ")
           print(" __________________________________________________")
           print(" |   *************************                    |")
           print(f" |   *  You got {score} / 15!      *                   |")
           print(" |   *************************                    |\n")
           print(" |________________________________________________|")

           if score >= pass_score:

               print(" | Congrats! You passed the quiz! d-(^_^)z        |")
               print(" |________________________________________________|")
               print(" ")
               print("_-" * 68)
           else:
               print(" | You Failed, Keep Going! (9'-')9                |")
               print(" |________________________________________________|")
               print(" ")
               print("_-" * 68)
       elif quizc2 == "N" :
           print("I understand.")
       else :
           print("Just pu YES or No.")
   elif choice == "3" :
       print("___________________________________________________________________________________________________")
       print("|                                                                                                 |")
       print("|      C H A P T E R   3    A R I T H M E T I C   O P E R A T O R   A N D   E X P R E S S I O N   |")
       print("|_________________________________________________________________________________________________|\n")

       print("What is ARITHMETIC OPERATOR?\n")
       print("ARITHMETIC OPERATOR are symbol we use in program to execute mathematical operation. (^_^) ")
       print("__________________________________________________________________________________________")
       print("|                                                                                        |")
       print("(   O P E R A T O R S   D E F I N I T I O N S   A N D   E X A M P L E S                  )")
       print("(________________________________________________________________________________________)")
       print("|                                                                                        |")
       print("|  ADDITION (+)  - Add two value  [1 + 5 = 6]                                            |")
       print("|........................................................................................|")
       print("|                                                                                        |")
       print("|  SUBTRACTION (-)   - Subtracts second value to first value  [10 - 5 = 5]               |")
       print("|........................................................................................|")
       print("|                                                                                        |")
       print("|  MULTIPLICATION (*)   - Multiply two values  [5 * 2 = 10]                              |")
       print("|........................................................................................|")
       print("|                                                                                        |")
       print("|  DIVISION(float) (/)   - Divide two value and return decimal   [5 / 2 = 2.0]           |")
       print("|........................................................................................|")
       print("|                                                                                        |")
       print("|  FLOOR DIVISION (//)   - Divide two value but return whole number  [10 // 2 = 5]       |")
       print("|........................................................................................|")
       print("|                                                                                        |")
       print("|  MODULUS (%)   - Return the remainder of division    [5 % 2 = 1]                       |")
       print("|........................................................................................|\n")
       print("Now if you think of it, What is expression?\n")
       print("EXPRESSION is the combination of values,variables and operator. It is useful everytime.\n")
       print("Let's see the example below.")
       print("__________________________________________________________________________")
       print("|`````````````````E X P R E S S I O N   I N   P Y T H O N````````````````|")
       print("|________________________________________________________________________|")
       print("|                                                                        |")
       print("| K = 12                      Take note: You can use it                  |")
       print("| P = 22                                 as long as you want.            |")
       print("| M = 27                                 But make sure it is right.      |")
       print("|                                                                        |")
       print("| tots = K + P + M                                                       |")
       print("| print(''Your total is'', tots)                                         |")
       print("|________________________________________________________________________|")
       print("|                                                                        |")
       print("| Output : Your total is 61                                              |")
       print("|........................................................................|\n")
       print("Did you know PEMDAS? |_(^_^)")
       print("PEMDAS is like combining all operators.\n")
       print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
       print("[________________________________________________________________________]")
       print("| P  for PARENTHESIS [()]   FIRST                                        |")
       print("| E  for EXPONENTS   [**]   SECOND                                       |")
       print("| M  for MULTIPLY    [*]    THIRD                                        |")
       print("| D  for DIVISION    [/]    FOURTH                                       |")
       print("| A  for ADDITION    [+]    FIFTH                                        |")
       print("| S  for SUBTRACTION [-]    SIXTH                                        |")
       print("|                                                                        |")
       print("|  Take Note: Use this by order! =(>_<)=                                 |")
       print("|                                                                        |")
       print("|                                                                        |")
       print("|........................................................................|\n")
       print("_-" * 68)
       print("      _.-'''''-._     .    H E L L O. I' M   V E R I T Y        ; ;     .      .     ,     ;                ")
       print("    .'  _     _  '.              .        L E T ' S   P L A Y             .     .                         ")
       print("   |   (o)   (o)   |       .     .   .                A         ,         ,         ;            ;          ")
       print("  |                 |                  G A M E.............           ;               ;    .               ")
       print("  |  (           )  |       ;    .    .                     ;                .                  .          ")
       print("   |  '.       .'  |                           ;                      ;          ;  ;     .       .           ")
       print("    '.  `'---'`  .'                ;                                                         ;            ")
       print("      '-._____.-'      .       ;             ;     .      ;          .      .          ;           .          ")
       print("_-" * 68)
       print(" ")
       sagot = input("Do you want to play the game? (YES/OK) : ").upper()
       if sagot == "YES" or sagot == "OK" :
           print("+------------------------------------------------------------------------+")
           print("| Sorry you can't scape me. :  )                                         |")
           print("|                                                                        |")
           print("|   In this game you have 7 life. I called this TRICKY GAME....          |")
           print("|   Alright. I know it's corny  [TvT]. In this game there are many       |")
           print("|   types of  symbol but beware because there are operators.             |")
           print("|   If the operators is familiar with you, use                           |")
           print("|   (add,minus,multiply,floor division or modulus). AT YOUR OWN RISK.    |")
           print("|                                                                        |")
           print("|    For Example : = + =                                                 |")
           print("|    Answer : 2                                                          |")
           print("|                                                                        |")
           print("|                                                                        |")
           print("|   Life Badge : Hacker - 7    Pro - 5   Average - 3                     |")
           print("|                                                                        |")
           print("+------------------------------------------------------------------------+\n")
           Life = 7

           print("     -|  |___________________________________________|  |-")
           print("    (_|  |___________________________________________|  |_)")
           print("      |  |       +-+-+-+-+-LEVEL ONE-+-+-+-+-+       |  |")
           print("      |  | 1. = + = + = + =                          |  |")
           print("      |  |                                           |  |")
           print("      |  |___________________________________________|  |")
           print("    (_|  |___________________________________________|  |_)")
           ans = input("      |  | Answer :")

           if ans == "4":
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
               print("          ( ( You win!              ( (")
               print("           ) ) Correct answer is 4.  ) )")
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
               print("__________________________________________________________________________________________\n")
           else:
               Life -= 1
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
               print("          ( ( You lost!             ( (")
               print("          ) ) Correct answer is 4.  ) )")
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
               print("__________________________________________________________________________________________\n")

           print("     -|  |___________________________________________|  |-")
           print("    (_|  |___________________________________________|  |_)")
           print("      |  |       +-+-+-+-+-LEVEL TWO-+-+-+-+-+       |  |")
           print("      |  | 2. _ - _ + _ _ _ + _ = - _ =              |  |")
           print("      |  |                                           |  |")
           print("      |  |___________________________________________|  |")
           print("    (_|  |___________________________________________|  |_)")
           ans = input("      |  | Answer :")
           if ans == "3":
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
               print("          ( ( You win!              ( (")
               print("           ) ) Correct answer is 3.  ) )")
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
               print("__________________________________________________________________________________________\n")

           else:
               Life -= 1
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
               print("          ( ( You lost!             ( (")
               print("           ) ) Correct answer is 3.  ) )")
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
               print("__________________________________________________________________________________________\n")

           print("     -|  |___________________________________________|  |-")
           print("    (_|  |___________________________________________|  |_)")
           print("      |  |       +-+-+-+-+-LEVEL THREE-+-+-+-+-+     |  |")
           print("      |  | 3. ^ ^ * _ _ _ - ! + _ _ _ - ^ ^          |  |")
           print("      |  |                                           |  |")
           print("      |  |___________________________________________|  |")
           print("    (_|  |___________________________________________|  |_)")
           ans = input("      |  | Answer :")
           if ans == "6":
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
               print("          ( ( You win!              ( (")
               print("           ) ) Correct answer is 6.  ) )")
               print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
               print("__________________________________________________________________________________________\n")

           else:
               Life -= 1
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
               print("          ( ( You lost!             ( (")
               print("           ) ) Correct answer is 6.  ) )")
               print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
               print("__________________________________________________________________________________________\n")
           print("     -|  |___________________________________________|  |-")
           print("    (_|  |___________________________________________|  |_)")
           print("      |  |       +-+-+-+-+-LEVEL FOUR-+-+-+-+-+      |  |")
           print("      |  | 4. # # # # // _ _ + = = = - $ + ! !       |  |")
           print("      |  |                                           |  |")
           print("      |  |___________________________________________|  |")
           print("    (_|  |___________________________________________|  |_)")
           ans = input("      |  | Answer :")

           if ans == "6":
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
               print("          ( ( You win!              ( (")
               print("           ) ) Correct answer is 6.  ) )")
               print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
               print("__________________________________________________________________________________________\n")

           else:
               Life -= 1
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
               print("          ( ( You lost!             ( (")
               print("           ) ) Correct answer is 6.  ) )")
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
               print("__________________________________________________________________________________________\n")

           print("     -|  |_____________________________________________|  |-")
           print("    (_|  |_____________________________________________|  |_)")
           print("      |  |       +-+-+-+-+-LEVEL FIVE-+-+-+-+-+        |  |")
           print("      |  | 5. ^ ^ ^ ^ ! $ $ $ # _ % ) _ _ + ~ ~  ~ - < |  |")
           print("      |  |                                             |  |")
           print("      |  |_____________________________________________|  |")
           print("    (_|  |_____________________________________________|  |_)")
           ans = input("      |  | Answer :")
           if ans == "3":
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
               print("          ( ( You win!              ( (")
               print("           ) ) Correct answer is 3.  ) )")
               print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
               print("__________________________________________________________________________________________\n")


           else:
               Life -= 1
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
               print("          ( ( You lost!             ( (")
               print("           ) ) Correct answer is 3.  ) )")
               print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
               print("__________________________________________________________________________________________\n")

           print("     -|  |_______________________________________________|  |-")
           print("    (_|  |_______________________________________________|  |_)")
           print("      |  |       +-+-+-+-+-LEVEL SIX-+-+-+-+-+           |  |")
           print("      |  | 6. ^ ^ _ * _ _ _ = _ + ~ ~ - ~ + > > > // [ [ |  |")
           print("      |  |                                               |  |")
           print("      |  |_______________________________________________|  |")
           print("    (_|  |_______________________________________________|  |_)")
           ans = input("      |  | Answer :")
           if ans == "17":
               print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
               print("          ( ( You win!               ( (")
               print("           ) ) Correct answer is 17.  ) )")
               print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
               print("__________________________________________________________________________________________\n")

           else:
               Life -= 1
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
               print("          ( ( You lost!             ( (")
               print("           ) ) Correct answer is 17. ) )")
               print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
               print("__________________________________________________________________________________________\n")

           print("     -|  |_______________________________________________|  |-")
           print("    (_|  |_______________________________________________|  |_)")
           print("      |  |       +-+-+-+-+-LEVEL SEVEN-+-+-+-+-+         |  |")
           print("      |  | 7. < < < + ^ ^ ^ ^ - ~ * { { - : : : : :      |  |")
           ans = input("      |  | Answer :")
           print("      |  |                                               |  |")
           print("      |  |_______________________________________________|  |")
           print("    (_|  |_______________________________________________|  |_)")
           if ans == "7":
               print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
               print("          ( ( You win!              ( (")
               print("           ) ) Correct answer is 7.  ) )")
               print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
               print("__________________________________________________________________________________________\n")

           else:
               Life -= 1
               print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
               print("          ( ( You lost!             ( (")
               print("           ) ) Correct answer is 7.  ) )")
               print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
               print("__________________________________________________________________________________________\n")
           print("_-" * 68)
           print("." * 136)
           print("_-" * 68)
           print("\n__________________________________________________")
           print(" |   *************************                    |")
           print(f" |   *  You got {Life} LIFE!      *                    |")
           print(" |   *************************                    |")
           print(" |________________________________________________|\n")
           if Life > 6 or Life >= 7:
               print("             ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
               print("             | Congrats you got Hacker Badge.|")
               print("             ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
               print("_-" * 68)
           elif Life >= 4 or Life < 5:
               print("             >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
               print("             + Congrats you got Pro Badge.+")
               print("             >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
               print("_-" * 68)
           elif Life == 3:
               print("            ================================")
               print("            Nice Try! You got Average Badge.")
               print("            ================================")
               print("_-" * 68)
           else:
               print("            ...................")
               print("            Review Chapter 3!")
               print("            ...................")
               print("_-" * 68)
               print("." * 136)
               print("_-" * 68)
           print("                    *****************")
           print("               ******               ******")
           print("           ****                           ****")
           print("        ****                                 ***")
           print("      ***                                       ***")
           print("     **           ***               ***           **")
           print("   **           *******           *******          ***")
           print("  **            *******           *******            **")
           print(" **             *******           *******             **")
           print(" **               ***               ***               **")
           print("=================================================================================")
           print("     W I N    O R    L O S E    Y O U    M U S T    T A K E    T H I S   T E S T.")
           print("=================================================================================")
           print("In this test you will just put The following operators (+, -, *, //, %).\n")
           score = 0
           print("   _.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._")
           print(".-'---      - ---     --     ---   -----   - --       ----  ----   -     ---`-.")
           print(" )  [1.] 5 _ 8 = 13         [6.] 10 _ 3 = 1                                  (")
           print("(                                                                             )")
           print(" )  [2.] 10 _ 2 = 8         [7.] 90 _ 3 = 30                                 (")
           print("(                                                                             )")
           print(" )  [3.] 8 _ 4 = 32         [8.] 500 _ 11 = 5                                (")
           print("(                                                                             )")
           print(" )  [4.] 6 _ 8 = 14                                                          (")
           print("(                                                                             )")
           print(" )  [5.] 10 _ 2 = 5                                                          (")
           print("(                                                                             )")
           print(" )                                                                           (")
           print("(___       _       _       _       _       _       _       _       _       ___)")
           print("    (__  _) ( __ _) (__  _) (__ _ ) `-._.-' ( _ __) (_  __) (_ __ ) (_  __)")
           print("    ( _ __) (_  __) (__ __) `-._.-'         `-._.-' (__ __) (__  _) (__ _ )")
           print("    (__  _) (_ _ _) `-._.-'                         `-._.-' (_ _ _) (_  __)")
           print("    (_ ___) `-._.-'                                         `-._.-' (___ _)")
           print("    `-._.-'                                                         `-._.-'\n")
           print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
           print("[1.] 5 _ 8 = 13")
           ans = input(" Answer number 1 :")
           if ans == "+":
               score += 1
           print("[2.] 10 _ 2 = 8")
           ans = input(" Answer number 2 :")
           if ans == "-":
               score += 1
           print("[3.] 8 _ 4 = 32")
           ans = input(" Answer number 3 :")
           if ans == "*":
               score += 1
           print("[4.] 6 _ 8 = 14")
           ans = input(" Answer number 4 :")
           if ans == "+":
               score += 1
           print("[5.] 10 _ 2 = 5")
           ans = input(" Answer number 5 :")
           if ans == "//":
               score += 1
           print("[6.] 10 _ 3 = 1 ")
           ans = input(" Answer number 6 :")
           if ans == "%":
               score += 1
           print("[7.] 90 _ 3 = 30")
           ans = input(" Answer number 7 :")
           if ans == "//":
               score += 1
           print("[8.] 500 _ 11 = 5")
           ans = input(" Answer number 8 :")
           if ans == "%":
               score += 1
               if score >= 6:
                   print("==============================+++++++++++++++++++++++++++++++++++++++++++++")
                   print(f"You got {score} / 8")
                   print("Congrats, That's a great work!")
                   print("==============================+++++++++++++++++++++++++++++++++++++++++++++")
               elif score > 4 or score < 5:
                   print("==============================+++++++++++++++++++++++++++++++++++++++++++++")
                   print(f"You got {score} / 8")
                   print("Nice, That's a great work!")
                   print("==============================+++++++++++++++++++++++++++++++++++++++++++++")
               else:
                   print("==============================+++++++++++++++++++++++++++++++++++++++++++++")
                   print(f"You got {score} / 8")
                   print("REVIEW THE CHAPTER 3!")
                   print("==============================+++++++++++++++++++++++++++++++++++++++++++++")
           print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
           print("**       *                                     *       **")
           print("**      **                                     **      **")
           print(
               " **   ****                                     ****   **        T H A T ' S    T H E    E N D         ")
           print(
               " **      **                                   **      **                                              ")
           print(
               "  **       ***                             ***       **                      O F                         ")
           print(
               "  **       ***                             ***       **          C H A P T E R   T W O!                                     ")
           print("     **         ******             ******         **")
           print("      ***            ***************            ***")
           print("        ****                                 ****")
           print("           ****                           ****")
           print("               ******               ******")
           print("                    *****************")
       else :
           print("+------------------------------------------------------------------------+")
           print("| Sorry you can't scape me. :  )                                         |")
           print("|                                                                        |")
           print("|   In this game you have 7 life. I called this TRICKY GAME....          |")
           print("|   Alright. I know it's corny  [TvT]. In this game there are many       |")
           print("|   types of  symbol but beware because there are operators.             |")
           print("|   If the operators is familiar with you, use                           |")
           print("|   (add,minus,multiply,floor division or modulus). AT YOUR OWN RISK.    |")
           print("|                                                                        |")
           print("|    For Example : = + =                                                 |")
           print("|    Answer : 2                                                          |")
           print("|                                                                        |")
           print("|                                                                        |")
           print("|   Life Badge : Hacker - 7    Pro - 5   Average - 3                     |")
           print("|                                                                        |")
           print("+------------------------------------------------------------------------+\n")

           Life = 7

           print("     -|  |___________________________________________|  |-")
           print("    (_|  |___________________________________________|  |_)")
           print("      |  |       +-+-+-+-+-LEVEL ONE-+-+-+-+-+       |  |")
           print("      |  | 1. = + = + = + =                          |  |")
           print("      |  |                                           |  |")
           print("      |  |___________________________________________|  |")
           print("    (_|  |___________________________________________|  |_)")
           ans = input("      |  | Answer :")

           if ans == "4" :
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
               print("          ( ( You win!              ( (")
               print("           ) ) Correct answer is 4.  ) )")
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
               print("__________________________________________________________________________________________\n")
           else :
               Life -= 1
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
               print("          ( ( You lost!             ( (")
               print("          ) ) Correct answer is 4.  ) )")
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
               print("__________________________________________________________________________________________\n")

           print("     -|  |___________________________________________|  |-")
           print("    (_|  |___________________________________________|  |_)")
           print("      |  |       +-+-+-+-+-LEVEL TWO-+-+-+-+-+       |  |")
           print("      |  | 2. _ - _ + _ _ _ + _ = - _ =              |  |")
           print("      |  |                                           |  |")
           print("      |  |___________________________________________|  |")
           print("    (_|  |___________________________________________|  |_)")
           ans = input("      |  | Answer :")
           if ans == "3":
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
               print("          ( ( You win!              ( (")
               print("           ) ) Correct answer is 3.  ) )")
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
               print("__________________________________________________________________________________________\n")

           else :
               Life -= 1
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
               print("          ( ( You lost!             ( (")
               print("           ) ) Correct answer is 3.  ) )")
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
               print("__________________________________________________________________________________________\n")

           print("     -|  |___________________________________________|  |-")
           print("    (_|  |___________________________________________|  |_)")
           print("      |  |       +-+-+-+-+-LEVEL THREE-+-+-+-+-+     |  |")
           print("      |  | 3. ^ ^ * _ _ _ - ! + _ _ _ - ^ ^          |  |")
           print("      |  |                                           |  |")
           print("      |  |___________________________________________|  |")
           print("    (_|  |___________________________________________|  |_)")
           ans = input("      |  | Answer :")
           if ans == "6":
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
               print("          ( ( You win!              ( (")
               print("           ) ) Correct answer is 6.  ) )")
               print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
               print("__________________________________________________________________________________________\n")

           else:
               Life -= 1
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
               print("          ( ( You lost!             ( (")
               print("           ) ) Correct answer is 6.  ) )")
               print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
               print("__________________________________________________________________________________________\n")
           print("     -|  |___________________________________________|  |-")
           print("    (_|  |___________________________________________|  |_)")
           print("      |  |       +-+-+-+-+-LEVEL FOUR-+-+-+-+-+      |  |")
           print("      |  | 4. # # # # // _ _ + = = = - $ + ! !       |  |")
           print("      |  |                                           |  |")
           print("      |  |___________________________________________|  |")
           print("    (_|  |___________________________________________|  |_)")
           ans = input("      |  | Answer :")

           if ans == "6":
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
               print("          ( ( You win!              ( (")
               print("           ) ) Correct answer is 6.  ) )")
               print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
               print("__________________________________________________________________________________________\n")

           else:
               Life -= 1
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
               print("          ( ( You lost!             ( (")
               print("           ) ) Correct answer is 6.  ) )")
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
               print("__________________________________________________________________________________________\n")

           print("     -|  |_____________________________________________|  |-")
           print("    (_|  |_____________________________________________|  |_)")
           print("      |  |       +-+-+-+-+-LEVEL FIVE-+-+-+-+-+        |  |")
           print("      |  | 5. ^ ^ ^ ^ ! $ $ $ # _ % ) _ _ + ~ ~  ~ - < |  |")
           print("      |  |                                             |  |")
           print("      |  |_____________________________________________|  |")
           print("    (_|  |_____________________________________________|  |_)")
           ans = input("      |  | Answer :")
           if ans == "3":
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
               print("          ( ( You win!              ( (")
               print("           ) ) Correct answer is 3.  ) )")
               print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
               print("__________________________________________________________________________________________\n")


           else:
               Life -= 1
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
               print("          ( ( You lost!             ( (")
               print("           ) ) Correct answer is 3.  ) )")
               print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
               print("__________________________________________________________________________________________\n")

           print("     -|  |_______________________________________________|  |-")
           print("    (_|  |_______________________________________________|  |_)")
           print("      |  |       +-+-+-+-+-LEVEL SIX-+-+-+-+-+           |  |")
           print("      |  | 6. ^ ^ _ * _ _ _ = _ + ~ ~ - ~ + > > > // [ [ |  |")
           print("      |  |                                               |  |")
           print("      |  |_______________________________________________|  |")
           print("    (_|  |_______________________________________________|  |_)")
           ans = input("      |  | Answer :")
           if ans == "17":
               print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
               print("          ( ( You win!               ( (")
               print("           ) ) Correct answer is 17.  ) )")
               print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
               print("__________________________________________________________________________________________\n")

           else:
               Life -= 1
               print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
               print("          ( ( You lost!             ( (")
               print("           ) ) Correct answer is 17. ) )")
               print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
               print("__________________________________________________________________________________________\n")

           print("     -|  |_______________________________________________|  |-")
           print("    (_|  |_______________________________________________|  |_)")
           print("      |  |       +-+-+-+-+-LEVEL SEVEN-+-+-+-+-+         |  |")
           print("      |  | 7. < < < + ^ ^ ^ ^ - ~ * { { - : : : : :      |  |")
           ans = input("      |  | Answer :")
           print("      |  |                                               |  |")
           print("      |  |_______________________________________________|  |")
           print("    (_|  |_______________________________________________|  |_)")
           if ans == "7":
               print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
               print("          ( ( You win!              ( (")
               print("           ) ) Correct answer is 7.  ) )")
               print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
               print("__________________________________________________________________________________________\n")

           else:
               Life -= 1
               print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
               print("          ( ( You lost!             ( (")
               print("           ) ) Correct answer is 7.  ) )")
               print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
               print("__________________________________________________________________________________________\n")
           print("_-" * 68)
           print("." * 136)
           print("_-" * 68)
           print("\n__________________________________________________")
           print(" |   *************************                    |")
           print(f" |   *  You got {Life} LIFE!      *                    |")
           print(" |   *************************                    |")
           print(" |________________________________________________|\n")
           if Life > 6 or Life >= 7 :
               print("             ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
               print("             | Congrats you got Hacker Badge.|")
               print("             ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
               print("_-" * 68)
           elif Life >= 4 or Life < 5 :
               print("             >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
               print("             + Congrats you got Pro Badge.+")
               print("             >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
               print("_-" * 68)
           elif Life == 3 :
               print("            ================================")
               print("            Nice Try! You got Average Badge.")
               print("            ================================")
               print("_-" * 68)
           else:
               print("            ...................")
               print("            Review Chapter 3!")
               print("            ...................")
               print("_-" * 68)
               print("." * 136)
               print("_-" * 68)
           print("                    *****************")
           print("               ******               ******")
           print("           ****                           ****")
           print("        ****                                 ***")
           print("      ***                                       ***")
           print("     **           ***               ***           **")
           print("   **           *******           *******          ***")
           print("  **            *******           *******            **")
           print(" **             *******           *******             **")
           print(" **               ***               ***               **")
           print("=================================================================================")
           print("     W I N    O R    L O S E    Y O U    M U S T    T A K E    T H I S   T E S T.")
           print("=================================================================================")
           print("In this test you will just put The following operators (+, -, *, //, %).\n")
           score = 0
           print("   _.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._")
           print(".-'---      - ---     --     ---   -----   - --       ----  ----   -     ---`-.")
           print(" )  [1.] 5 _ 8 = 13         [6.] 10 _ 3 = 1                                  (")
           print("(                                                                             )")
           print(" )  [2.] 10 _ 2 = 8         [7.] 90 _ 3 = 30                                 (")
           print("(                                                                             )")
           print(" )  [3.] 8 _ 4 = 32         [8.] 500 _ 11 = 5                                (")
           print("(                                                                             )")
           print(" )  [4.] 6 _ 8 = 14                                                          (")
           print("(                                                                             )")
           print(" )  [5.] 10 _ 2 = 5                                                          (")
           print("(                                                                             )")
           print(" )                                                                           (")
           print("(___       _       _       _       _       _       _       _       _       ___)")
           print("    (__  _) ( __ _) (__  _) (__ _ ) `-._.-' ( _ __) (_  __) (_ __ ) (_  __)")
           print("    ( _ __) (_  __) (__ __) `-._.-'         `-._.-' (__ __) (__  _) (__ _ )")
           print("    (__  _) (_ _ _) `-._.-'                         `-._.-' (_ _ _) (_  __)")
           print("    (_ ___) `-._.-'                                         `-._.-' (___ _)")
           print("    `-._.-'                                                         `-._.-'\n")
           print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
           print("[1.] 5 _ 8 = 13")
           ans = input(" Answer number 1 :")
           if ans == "+" :
               score += 1
           print("[2.] 10 _ 2 = 8")
           ans = input(" Answer number 2 :")
           if ans == "-":
               score += 1
           print("[3.] 8 _ 4 = 32")
           ans = input(" Answer number 3 :")
           if ans == "*":
               score += 1
           print("[4.] 6 _ 8 = 14")
           ans = input(" Answer number 4 :")
           if ans == "+":
               score += 1
           print("[5.] 10 _ 2 = 5")
           ans = input(" Answer number 5 :")
           if ans == "//":
               score += 1
           print("[6.] 10 _ 3 = 1 ")
           ans = input(" Answer number 6 :")
           if ans == "%":
               score += 1
           print("[7.] 90 _ 3 = 30")
           ans = input(" Answer number 7 :")
           if ans == "//":
               score += 1
           print("[8.] 500 _ 11 = 5")
           ans = input(" Answer number 8 :")
           if ans == "%":
               score += 1
               if score >= 6 :
                   print("==============================+++++++++++++++++++++++++++++++++++++++++++++")
                   print(f"You got {score} / 8")
                   print("Congrats, That's a great work!")
                   print("==============================+++++++++++++++++++++++++++++++++++++++++++++")
               elif score > 4 or score < 5 :
                   print("==============================+++++++++++++++++++++++++++++++++++++++++++++")
                   print(f"You got {score} / 8")
                   print("Nice, That's a great work!")
                   print("==============================+++++++++++++++++++++++++++++++++++++++++++++")
               else :
                   print("==============================+++++++++++++++++++++++++++++++++++++++++++++")
                   print(f"You got {score} / 8")
                   print("REVIEW THE CHAPTER 3!")
                   print("==============================+++++++++++++++++++++++++++++++++++++++++++++")
           print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
           print("**       *                                     *       **")
           print("**      **                                     **      **")
           print(" **   ****                                     ****   **        T H A T ' S    T H E    E N D         ")
           print(" **      **                                   **      **                                              ")
           print("  **       ***                             ***       **                      O F                         ")
           print("  **       ***                             ***       **          C H A P T E R   T W O!                                     ")
           print("     **         ******             ******         **")
           print("      ***            ***************            ***")
           print("        ****                                 ****")
           print("           ****                           ****")
           print("               ******               ******")
           print("                    *****************")

   elif choice == "4" :
       print("________________________________________________________________________________________________")
       print("|                                                                                              |")
       print("|      C H A P T E R   4    B A S I C   I N P U T   A N D   O U T P U T   I N  P Y T H O N     |")
       print("|______________________________________________________________________________________________|\n")
       print("What is INPUT?\n")
       print("This is where you want to ask something and respond.\n")
       print("Using INPUT you can able to type inside your Output. ")
       print("For example :\n")
       print("Remember the ('') Imagine this as quotation mark. Thank you for understanding!\n")
       print("                                    ____________________________")
       print("A S K * * A S K * * A S K * * A    |  ________________________  |")
       print("S                             S    | |                        | |====================================================]")
       print("K                             K    | |   Name : Kevin         | |  < You can put any names you want. But not number. ]")
       print("*  name = input(''Name :'')   *    | |   Name is Kevin        | |  < This is how it works.                           ] ")
       print("*  print(''Name is'', Name)   *    | |                        | |  < This is STRING                                  ]")
       print("A                             A    | |                        | |  ~Num1 = int(input(''Enter Number :''))            ]")
       print("S                             S    | |                        | |            ^This is for INTEGER.                   ]")
       print("K                             K    | |                        | |  ~Num2 = float(input(''Enter Number :''))          ]")
       print("*                             *    | |                        | |            ^This is for float(If you need decimal.)]")
       print("*                             *    | |________________________| |  ~ans = input(''Are you okay?(Y/N):'')             ]")
       print("A S K * * A S K * * A S K * * A    |____________________________|   is_me = ans == ''Y''                             ]")
       print("S                                                               |   print(''Status'',is_me)                          ]")
       print("K              ^                                   ^            |            ^This for Boolean using condition.      ]")
       print("*      This is your program.               This is your output. |                                                    ]")
       print("*---------------------------------------------------------------|====================================================]")
       print("*TAKE NOTE : You can Combine them together. That would be so cool!                                                   ]")
       print("---------------------------------------------------------------------------------------------------------------------]\n")
       print("_-" * 68)
       print(",---,---,---,---,---,---,---,---,---,---,---,---,---,-------,   L E T' S   T R Y   T O   ")
       print("|1/2| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 | + | ' | <-    |           M A K E   Y O U R   I N P U T   ")
       print("|---'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-----|    S Y S T E M !   U S E   T H E   F O L L O W I N G")
       print("| ->| | Q | W | E | R | T | Y | U | I | O | P | ] | ^ |     |                 DATA TYPES.")
       print("|-----',--',--',--',--',--',--',--',--',--',--',--',--'|    |")
       print("| Caps | A | S | D | F | G | H | J | K | L |   | [ | * |    |   STRING   >--------")
       print("|----,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'---'----|   INTEGERS >--------")
       print("|    | < | Z | X | C | V | B | N | M | , | . | - |          |   BOOLEAN  >--------")
       print("|----'-,-',--'--,'---'---'---'---'---'---'-,-'---',--,------|   FLOAT    >--------")
       print("| ctrl |  | alt |                          |Kevin |  | ctrl |")
       print("'------'  '-----'--------------------------'------'  '------'")
       print("_-" * 68)
       print("First to make is String. Then Int. Then float. Then Boolean(Use Conditional). Each Line, One after Another.")
       print("Use this as example :\n")
       print("''Enter Name : '' For String.\n")
       print("''Enter Number : '' For Int and float.\n")
       print("''Are you retired?(Y/N) : '' For Boolean.\n")
       print("  retired = ask == ''Y''\n")
       print("VARIABLES : [Name]STRING,[Num]INTEGER,[Num]FLOAT,[ask]BOOLEAN.")
       print("Use ('') as quotation mark.")
       print("_-" * 68)
       print("__________________________________________________________________________________________________________")
       ans1 =input("1|")
       print(" |")
       print(" |")
       print(" |")
       print(" |")
       print(" |")
       ans2 =input("2|")
       print(" |")
       print(" |")
       print(" |")
       print(" |")
       print(" |")
       ans3 =input("3|")
       print(" |")
       ans4 =input("4|")
       ans5 =input("5|")
       print(" |")
       print(" |")
       print(" |")
       print(" |")
       print(" |")
       print(" |________________________________________________________________________________________________________\n")
       if ans1 == "Name = input(''Enter Name : '')"  :
           print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - ")
           print("     ___________________________________________")
           print("()==(   LINE ONE (STRING)                      (@==()")
           print("     '_________________________________________'|")
           print("       |  You got The correct Answer.           |")
           print("       |  Name = input(''Enter Name : '')       |")
           print("     __)________________________________________|")
           print("()==(                                          (@==()")
           print("     '------------------------------------------'")
           print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - ")
       else :
           print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - ")
           print("     ___________________________________________")
           print("()==(  LINE ONE (STRING)                       (@==()")
           print("     '_________________________________________'|")
           print("       |  Wrong Answer Look down below.         |")
           print("       |  Name = input(''Enter Name : '')       |")
           print("     __)________________________________________|")
           print("()==(                                          (@==()")
           print("     '------------------------------------------'")
           print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - ")
       if ans2 == "Num = int(input(''Enter Number : ''))" :

           print("                                                   ___________________________________________")
           print("                                              ()==(  LINE TWO (INTEGER)                      (@==()")
           print("                                                   '_________________________________________'|")
           print("                                                     |  You got The correct Answer.           |")
           print("                                                     |  Num = int(input(''Enter Number : '')) |")
           print("                                                   __)________________________________________|")
           print("                                              ()==(                                          (@==()")
           print("                                                   '------------------------------------------'")
           print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - ")
       else :
           print("                                                   ___________________________________________")
           print("                                              ()==(  LINE TWO (INTEGER)                      (@==()")
           print("                                                   '_________________________________________'|")
           print("                                                     |  Wrong Answer. Look down below.        |")
           print("                                                     |  Num = int(input(''Enter Number : '')) |")
           print("                                                   __)________________________________________|")
           print("                                              ()==(                                          (@==()")
           print("                                                   '------------------------------------------'")
           print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - ")
       if ans3 == "Num = float(input(''Enter Number : ''))" :
           print("     ____________________________________________")
           print("()==(  LINE THREE (FLOAT)                       (@==()")
           print("     '__________________________________________'|")
           print("       |  You got The correct Answer.            |")
           print("       |  Num = float(input(''Enter Number : ''))|")
           print("     __)_________________________________________|")
           print("()==(                                           (@==()")
           print("     '-------------------------------------------'")
           print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - ")
       else:
            print("     ____________________________________________")
            print("()==(  LINE THREE (FLOAT)                       (@==()")
            print("     '__________________________________________'|")
            print("       |  Wrong Answer Look down below.          |")
            print("       |  Num = float(input(''Enter Number : ''))|")
            print("     __)_________________________________________|")
            print("()==(                                           (@==()")
            print("     '-------------------------------------------'")
            print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - ")
       if ans4 == "ask = input(''Are you retired?(Y/N) : '')" and ans5 == "retired = ask == ''Y''":
           print("                                                    _______________________________________________")
           print("                                               ()==(   LINE FOUR (BOOLEAN)                        (@==()")
           print("                                                    '_____________________________________________'|")
           print("                                                      |  You got The correct Answer.               |")
           print("                                                      |  ask = input(''Are you retired?(Y/N) : ''))|")
           print("                                                      |  retired = ask == ''Y''                    |")
           print("                                                    __)____________________________________________|")
           print("                                               ()==(                                              (@==()")
           print("                                                    '----------------------------------------------'")
           print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - ")
       else:
           print("                                                    _______________________________________________")
           print("                                               ()==(   LINE FOUR (BOOLEAN)                        (@==()")
           print("                                                    '_____________________________________________'|")
           print("                                                      |  Wrong Answer. Look down below.            |")
           print("                                                      |  ask = input(''Are you retired?(Y/N) : ''))|")
           print("                                                      |  retired = ask == ''Y''                    |")
           print("                                                    __)____________________________________________|")
           print("                                               ()==(                                              (@==()")
           print("                                                    '----------------------------------------------'")
           print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - ")
           print("_-" * 68)
           print("." * 136)
           print("_-" * 68)
           print("\n                          T H E     E N D    O F    C H A P T E R    F O U R!!! \n")
           print("_-" * 68)
           print("." * 136)
           print("_-" * 68)
   elif choice == "5" :
       print("__________________________________________________________________________________________")
       print("|                                                                                        |")
       print("|      C H A P T E R   5    C O N D I T I O N A L    S T A T E M E N T                   |")
       print("|________________________________________________________________________________________|\n")
       print("                                 ,     |    |      ,                                         ")
       print("                                / |    )|__|(     / |     What is CONDITIONAL STATEMENT?")
       print("                               /   |  (_|  |_)   /   |    ")
       print("                          ____/_____|__|@  @|___/_____|____  It allows the program to make decision, whether it's ")
       print("                         |              |VV|               |   TRUE or FALSE.")
       print("                         |        IF, ELSE IF, ELSE        |     ")
       print("                         |_________________________________|           if - Start to make decision.")
       print("                          |    /| |      ||       | /|    |            elif - Something else you want.")
       print("                          |  /   V        ))       V   |  |            else - when you don't have decision to make.")
       print("                          |/     `       //        '     || ")
       print("                          `              V                '\n")
       print("_-" * 68)
       print("RELATIONAL OPERATORS. If you compare two values that you used the result is always TRUE or FAlSE\n")
       print("__________________________________________________________________________________________")
       print("| OPERATORS |      DEFINITION          |           EXAMPLE           |        RESULTS     |")
       print("|___________|__________________________|_____________________________|____________________|")
       print("|   >=         Greater than or equal to      20 >= 39                        TRUE         |")
       print("|                                                                                         |")
       print("|_________________________________________________________________________________________|")
       print("|  <=          Less than or equal to         59 <= 59                        TRUE         |")
       print("|                                                                                         |")
       print("|_________________________________________________________________________________________|")
       print("|  !=          Not equal                     8 != 5                          TRUE         |")
       print("|                                                                                         |")
       print("|_________________________________________________________________________________________|")
       print("|  ==          Equal to                      6 == 6                          TRUE         |")
       print("|                                                                                         |")
       print("|_________________________________________________________________________________________|")
       print("|  >           Greater Than                  10 > 22                         FALSE        |")
       print("|                                                                                         |")
       print("|_________________________________________________________________________________________|")
       print("|  <            Less than                    88 < 100                        TRUE         |")
       print("|                                                                                         |")
       print("|_________________________________________________________________________________________|\n")
       print("```````````````````````````````````````````````````````````````````````````````````````````")
       enter = input("Enter [if] to see an example conditional : ").upper()
       if enter == "IF" :
           print(".---------------------------------. ")
           print("|  .---------------------------.  | ")
           print("|[]|  Life = 3                 |[]| <<< This is an example of using conditional statement.                ")
           print("|  |  if Life >= 2 :           |  |        - If you want to make other decision jus put,")
           print("|  |       print(''Win'')      |  |          [elif]. You can use this whanever you want. ")
           print("|  |  elif Life > 1 :          |  |")
           print("|  |       print(''Nice'')     |  |        - Make sure your conditional is intended :]")
           print("|  |  else :                   |  |        - Use [else] when you want a FALSE condition")
           print("|  |      print(''Bruh'')      |  |        - Don't forget to put this [:] with your condition.")
           print("|  |                           |  |")
           print("|  `---------------------------'  |===================================================================")
           print("|      __________________ _____   |   N E S T E D   C O N D I T I O N A L ")
           print("|     |   ___            |     |  |   It is the condition inside another condition.")
           print("|     |  |   |           |     |  |                 | ")
           print("|     |  |   |           |     |  |                 |")
           print("|     |  |   |           |     |  |                 |")
           print("|     |  |___|           |     |  |                 |")
           print("(_____|__________________|_____|__|                 |")
           print("                                                    +")
           print("          __________________________________________|_______________________________")
           print("          |```````````````````N E S T E D  C O N D I T I O N A L```````````````````|")
           print("          |________________________________________________________________________|")
           print("          |  stu = input(''Enter Mythic Glory(MG) :'')                             |")
           print("          |  rank = int(input(''Star points :'')                                   |")
           print("          |  if stu == ''MG'' :                                                    |")
           print("          |          if rank >= 100 :                                              |")
           print("          |               print(''Palong palo'')                                   |")
           print("          |          else :                                                        |")
           print("          |               print(''Low rank'')                                      |")
           print("          |  else :                                                                |")
           print("          |        print(''Lagay monga MG kahit di nag e ml'')                     |")
           print("          |________________________________________________________________________|\n")
           print("......................................................................................................")
           print("Now Let's Try what you learned About this lesson. Just write TRUE OR FALSE. Think before you answer!")
           print("Goodluck!!\n")
           score = 0
           print("+-------------+")
           print("| 1. 25 >= 15 |")
           print("+-------------+")
           answer = input("Your answer: ").upper()

           if answer == "TRUE":
               print("Correct!")
               score += 1
           elif answer == "FALSE":
               print("Wrong! The correct answer is TRUE.")
           else:
               print("I said TRUE or FALSE!")

           print("------------------------------------------")
           print("+-------------+")
           print("| 2. 30 <= 20 |")
           print("+-------------+")
           answer = input("Your answer: ").upper()

           if answer == "FALSE":
               print("Correct!")
               score += 1
           elif answer == "TRUE":
               print("Wrong! The correct answer is FALSE.")
           else:
               print("I said TRUE or FALSE!")

           print("------------------------------------------")
           print("+-------------+")
           print("| 3. 10 != 5  |")
           print("+-------------+")
           answer = input("Your answer: ").upper()

           if answer == "TRUE":
               print("Correct!")
               score += 1
           elif answer == "FALSE":
               print("Wrong! The correct answer is TRUE.")
           else:
               print("I said TRUE or FALSE!")

           print("------------------------------------------")
           print("+-------------+")
           print("| 4. 15 == 20 |")
           print("+-------------+")
           answer = input("Your answer: ").upper()

           if answer == "FALSE":
               print("Correct!")
               score += 1
           elif answer == "TRUE":
               print("Wrong! The correct answer is FALSE.")
           else:
               print("I said TRUE or FALSE!")

           print("------------------------------------------")
           print("+-------------+")
           print("| 5. 50 > 25  |")
           print("+-------------+")
           answer = input("Your answer: ").upper()

           if answer == "TRUE":
               print("Correct!")
               score += 1
           elif answer == "FALSE":
               print("Wrong! The correct answer is TRUE.")
           else:
               print("I said TRUE or FALSE!")

           print("------------------------------------------")
           print("+-------------+")
           print("| 6. 10 < 5   |")
           print("+-------------+")
           answer = input("Your answer: ").upper()

           if answer == "FALSE":
               print("Correct!")
               score += 1
           elif answer == "TRUE":
               print("Wrong! The correct answer is FALSE.")
           else:
               print("I said TRUE or FALSE!")

           print("------------------------------------------")
           print("+-------------+")
           print("| 7. 40 >= 40 |")
           print("+-------------+")
           answer = input("Your answer: ").upper()

           if answer == "TRUE":
               print("Correct!")
               score += 1
           elif answer == "FALSE":
               print("Wrong! The correct answer is TRUE.")
           else:
               print("I said TRUE or FALSE!")

           print("------------------------------------------")
           print("+-------------+")
           print("| 8. 15 <= 25 |")
           print("+-------------+")
           answer = input("Your answer: ").upper()

           if answer == "FALSE":
               print("Correct!")
               score += 1
           elif answer == "TRUE":
               print("Wrong! The correct answer is FALSE.")
           else:
               print("I said TRUE or FALSE!")

           print("------------------------------------------")
           print("+-------------+")
           print("| 9. 8 != 8   |")
           print("+-------------+")
           answer = input("Your answer: ").upper()

           if answer == "FALSE":
               print("Correct!")
               score += 1
           elif answer == "TRUE":
               print("Wrong! The correct answer is FALSE.")
           else:
               print("I said TRUE or FALSE!")

           print("------------------------------------------")
           print("+----------------+")
           print("| 10. 100 == 100 |")
           print("+----------------+")
           answer = input("Your answer: ").upper()

           if answer == "TRUE":
               print("Correct!")
               score += 1
           elif answer == "FALSE":
               print("Wrong! The correct answer is TRUE.")
           else:
               print("I said TRUE or FALSE!")

           print("   _.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._")
           print(".-'---      - ---     --     ---   -----   - --       ----  ----   -     ---`-.")
           print(" )  You got", score,"/ 10!!                                                  (")
           print("(                                                                             )")
           print(" )  Whatever the Result is, Don't give up.                                   (")
           print("(                                                                             )")
           print("_______________________________________________________________________________")
           if score >= 8:
               print("Well Done! You got that huge score! Happy seeing you improved.")
               print("_______________________________________________________________________________")
           elif score >= 5:
               print("Good job! Keep practicing. You can do it.")
               print("_______________________________________________________________________________")
           else:
               print("You failed. Study the lesson again and don't give up!")
               print("_______________________________________________________________________________")
           print(" )                                                                            (")
           print("(          T H E                                                               )")
           print(" )                   E N D                                                    (")
           print("(                             O F                                              )")
           print(" )                                   C H A P T E R                            (")
           print("(                                                    F I V E                   )")
           print(" )                                                                           (")
           print("(___       _       _       _       _       _       _       _       _       ___)")
           print("    (__  _) ( __ _) (__  _) (__ _ ) `-._.-' ( _ __) (_  __) (_ __ ) (_  __)")
           print("    ( _ __) (_  __) (__ __) `-._.-'         `-._.-' (__ __) (__  _) (__ _ )")
           print("    (__  _) (_ _ _) `-._.-'                         `-._.-' (_ _ _) (_  __)")
           print("    (_ ___) `-._.-'                                         `-._.-' (___ _)")
           print("    `-._.-'                                                         `-._.-'\n")

   elif choice == "6" :
       print("__________________________________________________________________________________________")
       print("|                                                                                        |")
       print("|      C H A P T E R   6    L O G I C A L    O P E R A T O R S                           |")
       print("|________________________________________________________________________________________|\n")
       print("What is LOGICAL OPERATORS?")
       print("Logical Operators are always used with conditional statement. They are use to reversed condition or combine.\n")
       print("__________________________________________________________________________________________")
       print("|                                                                                        |")
       print("(   L O G I C A L   O P E R A T O R S                                                    )")
       print("(________________________________________________________________________________________)")
       print("|                                                                                        |")
       print("|  and - Both Condition is TRUE                                                          |")
       print("|........................................................................................|")
       print("|                                                                                        |")
       print("|  or - One of the condition must be TRUE                                                |")
       print("|........................................................................................|")
       print("|                                                                                        |")
       print("|  not - Reverse the  result. TRUE = FALSE and FALSE = TRUE                              |")
       print("|........................................................................................|")
       print("|                                                                                        |")
       print("|  Example :                                                                             |")
       print("|                                                                                        |")
       print("|   age = 18                                     Take note : AND is all true.            |")
       print("|   got_vip = True                                           OR got atleast one true.    |")
       print("|                                                            NOT reverse the result.     |")
       print("|   if age >= 18 and got_vip :                                                           |")
       print("|      print(''Enjoy the party'')                                                        |")
       print("|   else :                                                                               |")
       print("|      print(''not allowed'')                                                            |")
       print("|                                                                                        |")
       print("|________________________________________________________________________________________|")
       print("|                                                                                        |")
       print("|   Example of NOT :                                                                     |")
       print("|                                                                                        |")
       print("|     sunny = True                                                                       |")
       print("|                                                                                        |")
       print("|     if not sunny :                                                                     |")
       print("|        print(''you can't play'')                                                       |")
       print("|     else :                                                                             |")
       print("|        print(''you can play'')                                                         |")
       print("|                                                                                        |")
       print("|________________________________________________________________________________________|\n")
       print("-+"*60)
       print("█▓▒░ LET'S PLAY A GAME : ) ░▒▓█")
       print("░ ▒ ▓ █ ░ ▒ ▓ █ ░ ▒ ▓ █ ░ ▒▓█░▒▓█░▒▓█░▒▓█")
       print("       L O G I C A L   O P E R A T O R")
       print("░ ▒ ▓ █ ░ ▒ ▓ █ ░ ▒ ▓ █ ░ ▒▓█░▒▓█░▒▓█░▒▓█")
       print("-+" * 60)

       print("==================================================================")
       print("|             LOGICAL OPERATOR CHALLENGE                         |")
       print("|================================================================|")
       print("|Welcome to the Logical Operator Challenge!                      |")
       print("|Put the number [1] or [2] to get the correct answer.            |")
       print("|You need to get at least 3 correct answers to pass.             |")
       print("|================================================================|")

       score = 0
       print("\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
       print("QUESTION 1: AND OPERATOR      ")
       print("Both conditions must be TRUE. ")
       print("x = True                      ")
       print("y = False                     ")
       print("What is the result of x and y?")
       print("[1] True                      ")
       print("[2] False                     ")
       print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")

       answer = input("Enter your answer: ")

       if answer == "2":
           print("CORRECT! Both conditions must be TRUE.")
           score = score + 1
       else:
           print("WRONG! The answer is FALSE.")
       print("\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
       print("QUESTION 2: OR OPERATOR")
       print("At least one condition must be TRUE.")
       print("x = True")
       print("y = False")
       print("What is the result of x or y?")
       print("[1] True")
       print("[2] False")
       print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
       answer = input("Enter your answer: ")

       if answer == "1":
           print("CORRECT! One condition is TRUE.")
           score = score + 1
       else:
           print("WRONG! The answer is TRUE.")
       print("\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
       print("QUESTION 3: NOT OPERATOR")
       print("The NOT operator reverses the condition.")
       print("x = True")
       print("What is the result of not x?")
       print("[1] True")
       print("[2] False")
       print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
       answer = input("Enter your answer: ")

       if answer == "2":
           print("CORRECT! NOT reverses TRUE into FALSE.")
           score = score + 1
       else:
           print("WRONG! The answer is FALSE.")
       print("\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
       print("QUESTION 4: AND OPERATOR")
       print("a = True")
       print("b = True")
       print("What is the result of a and b?")
       print("[1] True")
       print("[2] False")
       print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")

       answer = input("Enter your answer: ")

       if answer == "1":
           print("CORRECT! Both conditions are TRUE.")
           score = score + 1
       else:
           print("WRONG! The answer is TRUE.")
       print("\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
       print("QUESTION 5: OR OPERATOR")
       print("a = False")
       print("b = False")
       print("What is the result of a or b?")
       print("[1] True")
       print("[2] False")
       print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")

       answer = input("Enter your answer: ")

       if answer == "2":
           print("CORRECT! Both conditions are FALSE.")
           print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
           score = score + 1
       else:
           print("WRONG! The answer is FALSE.")
           print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
       print("==================================================================")
       print("|             PART II : MULTIPLE  CHOICE                         |")
       print("|================================================================|")
       print("|Read Carefully and put the following answer :}                  |")
       print("|================================================================|\n")
       print("1. Which operator requires BOTH conditions to be TRUE?")
       print("[A] and")
       print("[B] or")
       print("[C] not")

       answer = input("Your answer: ").lower()

       if answer == "a":
           print("Correct!\n")
           score += 1
       elif answer == "b" or answer == "c":
           print("Incorrect! The correct answer is A. and\n")
       else:
           print("Invalid answer!\n")

       print("2. Which operator requires at least ONE condition to be TRUE?")
       print("[A] and")
       print("[B] or")
       print("[C] not")

       answer = input("Your answer: ").lower()

       if answer == "b":
           print("Correct!\n")
           score += 1
       elif answer == "a" or answer == "c":
           print("Incorrect! The correct answer is B. or\n")
       else:
           print("Invalid answer!\n")

       print("3. What does the NOT operator do?")
       print("[A] Combines conditions")
       print("[B] Repeats conditions")
       print("[C] Reverses the result")

       answer = input("Your answer: ").lower()

       if answer == "c":
           print("Correct!\n")
           score += 1
       elif answer == "a" or answer == "b":
           print("Incorrect! The correct answer is C. Reverses the result\n")
       else:
           print("Invalid answer!\n")

       print("4. What is the result of True and False?")
       print("[A] True")
       print("[B] False")
       print("[C] None")

       answer = input("Your answer: ").lower()

       if answer == "b":
           print("Correct!\n")
           score += 1
       elif answer == "a" or answer == "c":
           print("Incorrect! The correct answer is B. False\n")
       else:
           print("Invalid answer!\n")

       print("5. What is the result of False or True?")
       print("[A] True")
       print("[B] False")
       print("[C] None")

       answer = input("Your answer: ").lower()

       if answer == "a":
           print("Correct!\n")
           score += 1
       elif answer == "b" or answer == "c":
           print("Incorrect! The correct answer is A. True\n")
       else:
           print("Invalid answer!\n")

       print("6. What is the result of not True?")
       print("[A] True")
       print("[B] False")
       print("[C] None")

       answer = input("Your answer: ").lower()

       if answer == "b":
           print("Correct!\n")
           score += 1
       elif answer == "a" or answer == "c":
           print("Incorrect! The correct answer is B. False\n")
       else:
           print("Invalid answer!\n")

       print("7. Which expression evaluates to TRUE?")
       print("[A] False and True")
       print("[B] True and True")
       print("[C] False or False")

       answer = input("Your answer: ").lower()

       if answer == "b":
           print("Correct!\n")
           score += 1
       elif answer == "a" or answer == "c":
           print("Incorrect! The correct answer is B. True and True\n")
       else:
           print("Invalid answer!\n")

       print("8. The AND operator needs both conditions to be TRUE.")
       print("[A] True")
       print("[B] False")

       answer = input("Your answer: ").lower()

       if answer == "a":
           print("Correct!\n")
           score += 1
       elif answer == "b":
           print("Incorrect! The correct answer is A. True\n")
       else:
           print("Invalid answer!\n")
       print("9. The NOT operator combines two conditions.")
       print("[A] True")
       print("[B] False")

       answer = input("Your answer: ").lower()

       if answer == "b":
           print("Correct!\n")
           score += 1
       elif answer == "a":
           print("Incorrect! The correct answer is B. False\n")
       else:
           print("Invalid answer!\n")

       print("10. What will be the output?")
       print("sunny = True")
       print("if not sunny:")
       print("    print('Cannot play')")
       print("else:")
       print("    print('Can play')")

       answer = input(" [A] Cannot play\n [B] Can play\nYour answer: ").lower()

       if answer == "b":
           print("Correct!\n")
           score += 1
       elif answer == "a":
           print("Incorrect! The correct answer is B. Can play\n")
       else:
           print("Invalid answer!\n")

       print("==================================================")
       print("                 QUIZ RESULT")
       print("==================================================")
       print("| Your Score:", score, "/ 15                     ")

       if score >= 10:
           print("~CONGRATULATIONS! YOU PASSED THE GAME!")
           if score == 15:
               print("~PERFECT SCORE! EXCELLENT WORK!")
           else:
               print("~GOOD JOB! KEEP LEARNING!")
       else:
           print("~SORRY! YOU FAILED.")
           print("~PLEASE REVIEW THE LESSON AND TRY AGAIN.")

       print("==================================================")
       print("      E N D   O F   C H A P T E R   S I X         ")
       print("==================================================")

   elif choice == "7" :

       print("__________________________________________________________________________________________")
       print("|                                                                                        |")
       print("|                  C H A P T E R   7   P Y T H O N   L O O P S                           |")
       print("|________________________________________________________________________________________|")
       print("|                                                                                        |")
       print("|  What are LOOPS?                                                                       |")
       print("|                                                                                        |")
       print("|  Loops are used to repeat a block of code multiple times. Instead of writing the       |")
       print("|  same code again and again, we can use loops to make our program shorter and easier.   |")
       print("|________________________________________________________________________________________|\n")

       print("__________________________________________________________________________________________")
       print("|                                                                                        |")
       print("|                                 W H I L E   L O O P                                    |")
       print("|________________________________________________________________________________________|")
       print("|                                                                                        |")
       print("|  What is WHILE LOOP?                                                                    |")
       print("|                                                                                        |")
       print("|  A WHILE LOOP repeats a block of code as long as the condition is TRUE.                |")
       print("|                                                                                        |")
       print("|  SIMPLE MEANING: Repeat while the condition is TRUE.                                   |")
       print("|________________________________________________________________________________________|\n")

       print("STEP 1: BASIC SYNTAX")
       print("------------------------------------------------------------------------------------------")
       print("while condition:")
       print("    statement")
       print("------------------------------------------------------------------------------------------")
       print("while     - Starts the loop.")
       print("condition - Checks if the condition is TRUE or FALSE.")
       print("statement - The code that will repeat.\n")

       print("STEP 2: EXAMPLE")
       print("------------------------------------------------------------------------------------------")

       print("number = 1")
       print("")
       print("while number <= 5:")
       print("    print(number)")
       print("    number += 1")

       print("------------------------------------------------------------------------------------------")
       print("OUTPUT:")

       number = 1

       while number <= 5:
           print(number)
           number += 1

       print("------------------------------------------------------------------------------------------\n")

       print("STEP 3: HOW DOES IT WORK?")
       print("------------------------------------------------------------------------------------------")
       print("1. Set the starting number: number = 1")
       print("2. Check if number <= 5.")
       print("3. If TRUE, print the number.")
       print("4. Increase the number by 1 using number += 1.")
       print("5. Repeat until the condition becomes FALSE.")
       print("------------------------------------------------------------------------------------------\n")

       print("IMPORTANT REMINDER:")
       print("Always make sure that the condition will eventually become FALSE.")
       print("Otherwise, your program may create an INFINITE LOOP.\n")

       print("__________________________________________________________________________________________")
       print("|                                                                                        |")
       print("|                           F O R   L O O P                                              |")
       print("|________________________________________________________________________________________|")
       print("|                                                                                        |")
       print("|  What is FOR LOOP?                                                                      |")
       print("|                                                                                        |")
       print("|  A FOR LOOP repeats a block of code for each item in a sequence or for a specific     |")
       print("|  number of repetitions.                                                                |")
       print("|                                                                                        |")
       print("|  SIMPLE MEANING: Repeat for every item or number in a sequence.                        |")
       print("|________________________________________________________________________________________|\n")

       print("STEP 1: BASIC SYNTAX")
       print("------------------------------------------------------------------------------------------")
       print("for variable in sequence:")
       print("    statement")
       print("------------------------------------------------------------------------------------------")
       print("for      - Starts the loop.")
       print("variable - Stores the current item.")
       print("in       - Gets an item from the sequence.")
       print("sequence - The collection or range of items.")
       print("statement- The code that will repeat.\n")

       print("STEP 2: EXAMPLE")
       print("------------------------------------------------------------------------------------------")

       print("for number in range(1, 6):")
       print("    print(number)")

       print("------------------------------------------------------------------------------------------")
       print("OUTPUT:")

       for number in range(1, 6):
           print(number)

       print("------------------------------------------------------------------------------------------\n")

       print("STEP 3: UNDERSTANDING RANGE()")
       print("------------------------------------------------------------------------------------------")
       print("range(1, 6) generates numbers from 1 up to 5.")
       print("The ending number is NOT included.")
       print("------------------------------------------------------------------------------------------\n")

       print("ANOTHER EXAMPLE:")
       print("------------------------------------------------------------------------------------------")

       print('for name in ["Kevin", "John", "Mark"]:')
       print('    print("Hello", name)')

       print("------------------------------------------------------------------------------------------")
       print("OUTPUT:")

       for name in ["Kevin", "John", "Mark"]:
           print("Hello", name)

       print("------------------------------------------------------------------------------------------\n")

       print("__________________________________________________________________________________________")
       print("|                                                                                        |")
       print("|                 D I F F E R E N C E   O F   L O O P S                                  |")
       print("|________________________________________________________________________________________|")
       print("|                                                                                        |")
       print("|  WHILE LOOP: Repeats as long as a condition is TRUE.                                   |")
       print("|                                                                                        |")
       print("|  FOR LOOP  : Repeats through a sequence of items.                                      |")
       print("|                                                                                        |")
       print("|  WHILE LOOP: Useful when the number of repetitions is not known.                       |")
       print("|                                                                                        |")
       print("|  FOR LOOP  : Useful when the number of repetitions or items is known.                  |")
       print("|________________________________________________________________________________________|\n")

       print("------------------------------------------------------------------------------------------\n")
       print("__________________________________________________________________________________________")
       print("|                                                                                        |")
       print("|      SINCE I  DIDN'T  PUT DESIGN UNLIKE OTHER CHAPTER  LET ME GIVE YOU A SUMMARY       |")
       print("|________________________________________________________________________________________|")
       print("|                                                                                        |")
       print("|  1. A loop repeats a block of code.                                                    |")
       print("|  2. A WHILE LOOP repeats while its condition is TRUE.                                  |")
       print("|  3. A FOR LOOP repeats through a sequence.                                             |")
       print("|  4. The range() function generates a sequence of numbers.                              |")
       print("|  5. Indentation is important in Python loops.                                          |")
       print("|  6. An INFINITE LOOP happens when a loop never stops.                                  |")
       print("|________________________________________________________________________________________|\n")

       print("__________________________________________________________________________________________")
       print("|                                                                                        |")
       print("|                         C H A P T E R   7   Q U I Z                                    |")
       print("|________________________________________________________________________________________|\n")

       print("INSTRUCTIONS:")
       print("Choose the correct letter.")
       print("You need 4 points out of 5 to PASS.\n")

       score = 0

       print("1. Which loop repeats while a condition is TRUE?")
       print("[A] FOR LOOP")
       print("[B] WHILE LOOP")
       print("[C] IF STATEMENT")

       answer = input("Your answer: ").upper()

       if answer == "B":
           print("CORRECT!\n")
           score += 1
       else:
           print("INCORRECT! The correct answer is B.\n")

       print("2. Which function is commonly used with a FOR LOOP to generate numbers?")
       print("[A] input()")
       print("[B] print()")
       print("[C] range()")

       answer = input("Your answer: ").upper()

       if answer == "C":
           print("CORRECT!\n")
           score += 1
       else:
           print("INCORRECT! The correct answer is C.\n")

       print("3. What is the output of range(1, 4)?")
       print("[A] 1, 2, 3")
       print("[B] 1, 2, 3, 4")
       print("[C] 0, 1, 2, 3")

       answer = input("Your answer: ").upper()

       if answer == "A":
           print("CORRECT!\n")
           score += 1
       else:
           print("INCORRECT! The correct answer is A.\n")

       print("4. What happens when a WHILE LOOP condition becomes FALSE?")
       print("[A] It repeats forever")
       print("[B] The loop stops")
       print("[C] The program restarts")

       answer = input("Your answer: ").upper()

       if answer == "B":
           print("CORRECT!\n")
           score += 1
       else:
           print("INCORRECT! The correct answer is B.\n")

       print("5. Which loop is useful for displaying every name in a list?")
       print("[A] FOR LOOP")
       print("[B] IF STATEMENT")
       print("[C] ELSE STATEMENT")

       answer = input("Your answer: ").upper()

       if answer == "A":
           print("CORRECT!\n")
           score += 1
       else:
           print("INCORRECT! The correct answer is A.\n")

       print("__________________________________________________________________________________________")
       print("|                                                                                        |")
       print("|                              Q U I Z   R E S U L T                                     |")
       print("|________________________________________________________________________________________|")

       print("YOUR SCORE:", score, "/ 5")

       if score >= 4:
           print("CONGRATULATIONS! YOU PASSED!")
           if score == 5:
               print("PERFECT SCORE! EXCELLENT WORK!")
           else:
               print("GOOD JOB! KEEP LEARNING!")
       else:
           print("SORRY! YOU FAILED.")
           print("PLEASE REVIEW THE LESSON AND TRY AGAIN.")

       print("__________________________________________________________________________________________")
       print("|                         E N D   O F   C H A P T E R   7                                |")
       print("|________________________________________________________________________________________|")

elif pick =="LSBS" :
    print("__________________________________________________________________________________________")
    print("|                                                                                        |")
    print("|      C H A P T E R   1    I N T R O D U C T I O N    T O    P R O G R A M M I N G      |")
    print("|________________________________________________________________________________________|\n")

    print("Do you have any idea what's programming language is? if not, PROGRAMMING LANGUAGE is a special language")
    print("that computers understand and use to perform task.(。•̀ᴗ-)✧\n")
    print(
        "Anyways PYTHON PROGRAMMING is widely used around the world because it was easy to learn, simple and readable.")
    print("It was created by Guido Van Rossum in 1991.\n")
    print("What do you need to start python?\n")
    print("_________________________________________________________________________")
    print("|`````P R O F E S S I O N A L   I D E S / C O D E S   E D I T O R S`````|")
    print("|_______________________________________________________________________|")
    print("| PYCHARM BY JET BRAINS.                                                |")
    print("| VS CODE  (VISUAL STUDIO CODE).                                        |")
    print("| JUPYTER NOTEBOOK/JUPYTER LAB.                                         |")
    print("|_______________________________________________________________________|\n")
    print("That's all for Chapter 1.")
    print("Easy Right? RIGHTTTTTTTTTTTTTTTT?. ＼(ˇ∇ˇ)／\n")
    print("_-" * 68)
    print("                                                         _________________________    ")
    print("                    /|      _____          _____       |   |     |     |    | |  |   ")
    print("     ,-----,       /  |____/__|__|_    ___/__|__|___   |___|_____|_____|____|_|___|  ")
    print("  ,--'---:---`--, /  |  _     |     `| |      |      `| |                    | |    | ")
    print(" ==(o)-----(o)==J    `(o)-------(o)=   `(o)------(o)'   `--(o)(o)--------------(o)--'  ")
    print("`````````````````````````````````````````````````````````````````````````````````````")
    print("_-" * 68)
    print("========== L O A D I N G   P L E A S E   W A I T ==========................................................")
    print("_-" * 68)
    print(" ")
    print("__________________________________________________________________________________________")
    print("|                                                                                        |")
    print("|      C H A P T E R   2    P Y T H O N   B A S I C   S Y N T A X                        |")
    print("|________________________________________________________________________________________|\n")

    print("What is SYNTAX.\n")
    print("SYNTAX refers to the set of rules that tells us how correctly write a program in Python.\n")
    print("=--PYTHON SYNTAX--=")
    print("These things is really important to understand, remember this. Python is case sensitive ")
    print("because python treats upper and lower case differently.Also Python need Indentation or called")
    print("spaces to define blocks of code.  <(-^,^-)=b \n")
    print("For example....\n")
    print("Remember the ('') Imagine this as quotation mark. Thank you for understanding!\n")
    print("__________________________________________________________________________________________")
    print("|  Python Case Sensitive.                                                                |")
    print("|                                                                                        |")
    print("|  (1). name = ''Kevin''               (2). name = ''Kevin''                             |")
    print("|       print(Name)                       print(name)                                    |")
    print("|                                                                                        |")
    print("|    The number  1 is wrong. Number 2 is correct. Why?                                   |")
    print("|    because even though the word NAME is same.                                          |")
    print("|    You can see that, 1 has lowercase variable storage.                                 |")
    print("|    But has upper case with print(Name).                                                |")
    print("|                                                                                        |")
    print("|    Keyword : If it's lower. It's lower. If it's upper. It's upper.                     |")
    print("|                                                                                        |")
    print("|  Indentations(Spaces).                                                                 |")
    print("|                                                                                        |")
    print("|   (1). age = 18                    (2). age = 18                                       |")
    print("|        if age >= 18 :                   if age >= 18 :                                 |")
    print("|          print(''Adult'')               print(''Adult'')                               |")
    print("|                                                                                        |")
    print("|   Number 2 is incorrect because it is not intended or he doesn't have spaces           |")
    print("|   to get inside the block. While number 1 has spaces that's why it's intended.         |")
    print("|                                                                                        |")
    print("|    Keyword: Use spaces and make sure it is align perfectly in your coding              |")
    print("|             to get intended.                                                           |")
    print("|________________________________________________________________________________________|\n")

    print("_-" * 68)
    print("." * 136)
    print("_-" * 68)
    print("                                                      __  _")
    print("      ...........................                     | `/ |     ")
    print("      |                         |                      |__`!   ")
    print("      | PRINTING                |_  ___                / ,' `-.__________________   ")
    print("      |           OUTPUT        | -    ________________'-'|_____                LI`-.   ")
    print("      ...........................                         <____()-=O=O=O=O=O=[]====--)")
    print("                                                              `.___ ,-----,_______...-'")
    print("                                                                   /    .'")
    print("                                                                  /   .'")
    print("                                                                 /  .'  ")
    print("                                                                `-'")
    print("_-" * 68)
    print("." * 136)
    print("_-" * 68)

    print("\nNow let's proceed to PRINTING OUTPUT.\n")
    print("PRINTING OUTPUT - It displayed information through your screen.")
    print("PRINTING NUMBERS - You can put numbers without quotation marks but there's different.See")
    print("the example below.\n")
    print("Remember the ('') Imagine this as quotation mark. Thank you for understanding!\n")
    print("__________________________________________________________________________________________")
    print("|                                                                                        |")
    print("|      (1). print(100)            (2). print(''500'')                                    |")
    print("|           print(25.5)                print(''112'')                                    |")
    print("|                                                                                        |")
    print("|      1 and 2 are both correct, they just have different data types.                    |")
    print("|      The number 1 in line one is called INTEGERS. Line two is called FLOAT.            |")
    print("|      While number 2 is called STRING because it has quotation mark.                    |")
    print("|                                                                                        |")
    print("|                                                                                        |")
    print("|                                                                                        |")
    print("|________________________________________________________________________________________|\n")

    print("() - Open and close Parenthesis Is the reason why program contain to be displayed.")
    print("('') - Quotation mark is the sign for string because without quotation mark,")
    print("you get either error or variables.")
    print("Value - This is (STRING, NUMBER, VARIABLE and ETC.)\n")
    print("_-" * 68)
    print("\n                        ( -_•)ᡕᠵデᡁ᠊╾━--- P Y T H O N   C O M M E N T S.\n")
    print("_-" * 68)
    print("PYTHON COMMENTS is easy to remember just put HASHTAG (#) and that's it you have comment. ദ്ദി ˉ͈̀꒳ˉ͈́ )✧")
    print("Kidding aside. there is two types of comments.")
    print("The first one is SINGLE LINE COMMENT. The second one is MULTI LINE COMMENTS.")
    print("\nRemember the ('') Imagine this as quotation mark. Thank you for understanding!\n")
    print("__________________________________________________________________________")
    print("|``````````````````````P Y T H O N   C O M M E N T S`````````````````````|")
    print("|________________________________________________________________________|")
    print("|                                                                        |")
    print("| SINGLE LINE COMMENTS = (#)                                             |")
    print("|                                                                        |")
    print("| MULTI LINE COMMENTS = ('''''') at top and bottom                       |")
    print("|                                                                        |")
    print("|   Take note: Comments are ignored by python, and used to               |")
    print("|              explain   the code.                                       |")
    print("|________________________________________________________________________|\n")
    print("_-" * 68)
    print("." * 136)
    print("_-" * 68)
    print("\n          _  _")
    print("         ( `   )_")
    print("        (    )    `)")
    print("      (_   (_ .  _) _)")
    print("                                  V A R I A B L E S ,                                                ")
    print("                                         C O N S T A N T S ,                                     ")
    print("           _                                     A N D ")
    print("         -=|`|                         D A T A   T Y P E S.")
    print("     || ____|_|__                                                                 _")
    print("   -=|c`         L`)                                  -----                       (  )")
    print("      `~~~~~| |~~`                                                             ( `  ) . )")
    print("        -==| |                        - - - - -                              (_, _(  ,_)_)")
    print("          '-'                                                                    \n")
    print("_-" * 68)
    print("." * 136)
    print("_-" * 68)
    print("\nWhat is VARIABLES?\n")
    print("VARIABLES is the storage location where you can  keep data in program.\n")
    print("TAKE NOTE :")
    print("Variables can have short name like (a,b,c) or more like (name, total_val, char).")
    print("Variables can't start with numbers. It starts with underscore(_) or letter.")
    print("Like i said before. Python case is sensitive. If you have variable (NAME, name), ")
    print("this two variable are from different data.\n")
    print("\nRemember the ('') Imagine this as quotation mark. Thank you for understanding!\n")
    print("__________________________________________________________________________________________")
    print("| In programming we store data in variables. we put value  to variable,                  |")
    print("| using ASSIGNMENT OPERATOR.                                                             |")
    print("|                                                                                        |")
    print("| For example :                                                                          |")
    print("|                                                                                        |")
    print("|           Character_one = ''Tung Tung Sahur''                                          |")
    print("|                   ^                  ^                                                 |")
    print("|          #This is variable,     #This is Value the data we store in variable.          |")
    print("|           the  name we use to present data.             (It can be text, num and etc). |")
    print("|                                                                                        |")
    print("|           Is that Clear? <(-^,^-)=b                                                    |")
    print("|                                                                                        |")
    print("| Also you can print multiple variables using add(+) or comma(,).                        |")
    print("|                                                                                        |")
    print("| For Example :                                                                          |")
    print("|           a = ''Keep''                                                                 |")
    print("|           b = ''Going''                                                                |")
    print("|           c = ''embrace fear''                                                         |")
    print("|                                                                                        |")
    print("|           print (a + b + c) > output : Keep going embrace fear                         |")
    print("|           print (a, b, c)   > output : Keep going embrace fear                         |")
    print("|________________________________________________________________________________________|\n")
    print("_-" * 68)
    print("\n                        ( -_•)ᡕᠵデᡁ᠊╾━--- D A T A   T Y P E S   I N    P Y T H O N.\n")
    print("_-" * 68)
    print("DATA TYPES - Tells the python on what kind of variable we stored.\n")
    print("Lets focus on :\n")
    print("STRING - More on text inside quotation mark.")
    print("Example : (''Kevin'' , ''Mandal'' , ''Perez'') \n")
    print("INTEGERS(int) - More on Whole numbers. ")
    print("Example : (12, 22 , -18)\n")
    print("float - It has decimal point.")
    print("Example : (20.07, 18.22, -17.2)\n")
    print("bool(boolean) - Represent one of two value it's either TRUE or FALSE.")
    print("Example : (TRUE, FALSE)\n")
    print("This is the example of how it works.")
    print("__________________________________________________________________________________________")
    print("|                                                                                        |")
    print("|    name = ''Kevin''               >  String                                            |")
    print("|    age = 18                       >  Integers                                          |")
    print("|    grade_inpython = 61.30         >  Float                                             |")
    print("|    is_enrolled = False            >  Boolean                                           |")
    print("|                                                                                        |")
    print("|    print(name)                                                                         |")
    print("|    print(age)                                                                          |")
    print("|    print(grade_inpython)                                                               |")
    print("|    print(is_enrolled)                                                                  |")
    print("|                                                                                        |")
    print("|________________________________________________________________________________________|\n")
    print("_-" * 68)
    print("       __|__          ============================================           __|__            ")
    print("--------(_)--------   L O A D I N G    P L E A S E    W A I T.....    --------(_)--------")
    print("  O  O       O  O     ============================================      O  O       O  O            ")
    print("_-" * 68)
    print("T H A T ' S   T H E   E N D  O F   C H A P T E R   T W O ")
    print("_-" * 68)
    print(" ")
    print("___________________________________________________________________________________________________")
    print("|                                                                                                 |")
    print("|      C H A P T E R   3    A R I T H M E T I C   O P E R A T O R   A N D   E X P R E S S I O N   |")
    print("|_________________________________________________________________________________________________|\n")

    print("What is ARITHMETIC OPERATOR?\n")
    print("ARITHMETIC OPERATOR are symbol we use in program to execute mathematical operation. (^_^) ")
    print("__________________________________________________________________________________________")
    print("|                                                                                        |")
    print("(   O P E R A T O R S   D E F I N I T I O N S   A N D   E X A M P L E S                  )")
    print("(________________________________________________________________________________________)")
    print("|                                                                                        |")
    print("|  ADDITION (+)  - Add two value  [1 + 5 = 6]                                            |")
    print("|........................................................................................|")
    print("|                                                                                        |")
    print("|  SUBTRACTION (-)   - Subtracts second value to first value  [10 - 5 = 5]               |")
    print("|........................................................................................|")
    print("|                                                                                        |")
    print("|  MULTIPLICATION (*)   - Multiply two values  [5 * 2 = 10]                              |")
    print("|........................................................................................|")
    print("|                                                                                        |")
    print("|  DIVISION(float) (/)   - Divide two value and return decimal   [5 / 2 = 2.0]           |")
    print("|........................................................................................|")
    print("|                                                                                        |")
    print("|  FLOOR DIVISION (//)   - Divide two value but return whole number  [10 // 2 = 5]       |")
    print("|........................................................................................|")
    print("|                                                                                        |")
    print("|  MODULUS (%)   - Return the remainder of division    [5 % 2 = 1]                       |")
    print("|........................................................................................|\n")
    print("Now if you think of it, What is expression?\n")
    print("EXPRESSION is the combination of values,variables and operator. It is useful everytime.\n")
    print("Let's see the example below.")
    print("__________________________________________________________________________")
    print("|`````````````````E X P R E S S I O N   I N   P Y T H O N````````````````|")
    print("|________________________________________________________________________|")
    print("|                                                                        |")
    print("| K = 12                      Take note: You can use it                  |")
    print("| P = 22                                 as long as you want.            |")
    print("| M = 27                                 But make sure it is right.      |")
    print("|                                                                        |")
    print("| tots = K + P + M                                                       |")
    print("| print(''Your total is'', tots)                                         |")
    print("|________________________________________________________________________|")
    print("|                                                                        |")
    print("| Output : Your total is 61                                              |")
    print("|........................................................................|\n")
    print("Did you know PEMDAS? |_(^_^)")
    print("PEMDAS is like combining all operators.\n")
    print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
    print("[________________________________________________________________________]")
    print("| P  for PARENTHESIS [()]   FIRST                                        |")
    print("| E  for EXPONENTS   [**]   SECOND                                       |")
    print("| M  for MULTIPLY    [*]    THIRD                                        |")
    print("| D  for DIVISION    [/]    FOURTH                                       |")
    print("| A  for ADDITION    [+]    FIFTH                                        |")
    print("| S  for SUBTRACTION [-]    SIXTH                                        |")
    print("|                                                                        |")
    print("|  Take Note: Use this by order! =(>_<)=                                 |")
    print("|                                                                        |")
    print("|                                                                        |")
    print("|........................................................................|\n")
    print("_-" * 68)
    print("________________________________________________________________________________________________")
    print("|                                                                                              |")
    print("|      C H A P T E R   4    B A S I C   I N P U T   A N D   O U T P U T   I N  P Y T H O N     |")
    print("|______________________________________________________________________________________________|\n")
    print("What is INPUT?\n")
    print("This is where you want to ask something and respond.\n")
    print("Using INPUT you can able to type inside your Output. ")
    print("For example :\n")
    print("Remember the ('') Imagine this as quotation mark. Thank you for understanding!\n")
    print("                                    ____________________________")
    print("A S K * * A S K * * A S K * * A    |  ________________________  |")
    print("S                             S    | |                        | |====================================================]")
    print("K                             K    | |   Name : Kevin         | |  < You can put any names you want. But not number. ]")
    print("*  name = input(''Name :'')   *    | |   Name is Kevin        | |  < This is how it works.                           ] ")
    print("*  print(''Name is'', Name)   *    | |                        | |  < This is STRING                                  ]")
    print("A                             A    | |                        | |  ~Num1 = int(input(''Enter Number :''))            ]")
    print("S                             S    | |                        | |            ^This is for INTEGER.                   ]")
    print("K                             K    | |                        | |  ~Num2 = float(input(''Enter Number :''))          ]")
    print("*                             *    | |                        | |            ^This is for float(If you need decimal.)]")
    print("*                             *    | |________________________| |  ~ans = input(''Are you okay?(Y/N):'')             ]")
    print("A S K * * A S K * * A S K * * A    |____________________________|   is_me = ans == ''Y''                             ]")
    print("S                                                               |   print(''Status'',is_me)                          ]")
    print("K              ^                                   ^            |            ^This for Boolean using condition.      ]")
    print("*      This is your program.               This is your output. |                                                    ]")
    print("*---------------------------------------------------------------|====================================================]")
    print("*TAKE NOTE : You can Combine them together. That would be so cool!                                                   ]")
    print("---------------------------------------------------------------------------------------------------------------------]\n")
    print("_-" * 68)
    print(" ")
    print("__________________________________________________________________________________________")
    print("|                                                                                        |")
    print("|      C H A P T E R   5    C O N D I T I O N A L    S T A T E M E N T                   |")
    print("|________________________________________________________________________________________|\n")
    print("                                 ,     |    |      ,                                         ")
    print("                                / |    )|__|(     / |     What is CONDITIONAL STATEMENT?")
    print("                               /   |  (_|  |_)   /   |    ")
    print("                          ____/_____|__|@  @|___/_____|____  It allows the program to make decision, whether it's ")
    print("                         |              |VV|               |   TRUE or FALSE.")
    print("                         |        IF, ELSE IF, ELSE        |     ")
    print("                         |_________________________________|           if - Start to make decision.")
    print("                          |    /| |      ||       | /|    |            elif - Something else you want.")
    print("                          |  /   V        ))       V   |  |            else - when you don't have decision to make.")
    print("                          |/     `       //        '     || ")
    print("                          `              V                '\n")
    print("_-" * 68)
    print("RELATIONAL OPERATORS. If you compare two values that you used the result is always TRUE or FAlSE\n")
    print("__________________________________________________________________________________________")
    print("| OPERATORS |      DEFINITION          |           EXAMPLE           |        RESULTS     |")
    print("|___________|__________________________|_____________________________|____________________|")
    print("|   >=         Greater than or equal to      20 >= 39                        TRUE         |")
    print("|                                                                                         |")
    print("|_________________________________________________________________________________________|")
    print("|  <=          Less than or equal to         59 <= 59                        TRUE         |")
    print("|                                                                                         |")
    print("|_________________________________________________________________________________________|")
    print("|  !=          Not equal                     8 != 5                          TRUE         |")
    print("|                                                                                         |")
    print("|_________________________________________________________________________________________|")
    print("|  ==          Equal to                      6 == 6                          TRUE         |")
    print("|                                                                                         |")
    print("|_________________________________________________________________________________________|")
    print("|  >           Greater Than                  10 > 22                         FALSE        |")
    print("|                                                                                         |")
    print("|_________________________________________________________________________________________|")
    print("|  <            Less than                    88 < 100                        TRUE         |")
    print("|                                                                                         |")
    print("|_________________________________________________________________________________________|\n")
    print("```````````````````````````````````````````````````````````````````````````````````````````")
    enter = input("Enter [if] to see an example conditional : ").upper()
    if enter == "IF":
        print(".---------------------------------. ")
        print("|  .---------------------------.  | ")
        print(
            "|[]|  Life = 3                 |[]| <<< This is an example of using conditional statement.                ")
        print("|  |  if Life >= 2 :           |  |        - If you want to make other decision jus put,")
        print("|  |       print(''Win'')      |  |          [elif]. You can use this whanever you want. ")
        print("|  |  elif Life > 1 :          |  |")
        print("|  |       print(''Nice'')     |  |        - Make sure your conditional is intended :]")
        print("|  |  else :                   |  |        - Use [else] when you want a FALSE condition")
        print("|  |      print(''Bruh'')      |  |        - Don't forget to put this [:] with your condition.")
        print("|  |                           |  |")
        print("|  `---------------------------'  |===================================================================")
        print("|      __________________ _____   |   N E S T E D   C O N D I T I O N A L ")
        print("|     |   ___            |     |  |   It is the condition inside another condition.")
        print("|     |  |   |           |     |  |                 | ")
        print("|     |  |   |           |     |  |                 |")
        print("|     |  |   |           |     |  |                 |")
        print("|     |  |___|           |     |  |                 |")
        print("(_____|__________________|_____|__|                 |")
        print("                                                    +")
        print("          __________________________________________|_______________________________")
        print("          |```````````````````N E S T E D  C O N D I T I O N A L```````````````````|")
        print("          |________________________________________________________________________|")
        print("          |  stu = input(''Enter Mythic Glory(MG) :'')                             |")
        print("          |  rank = int(input(''Star points :'')                                   |")
        print("          |  if stu == ''MG'' :                                                    |")
        print("          |          if rank >= 100 :                                              |")
        print("          |               print(''Palong palo'')                                   |")
        print("          |          else :                                                        |")
        print("          |               print(''Low rank'')                                      |")
        print("          |  else :                                                                |")
        print("          |        print(''Lagay monga MG kahit di nag e ml'')                     |")
        print("          |________________________________________________________________________|\n")
        print("......................................................................................................")
        print("__________________________________________________________________________________________")
        print("|                                                                                        |")
        print("|      C H A P T E R   6    L O G I C A L    O P E R A T O R S                           |")
        print("|________________________________________________________________________________________|\n")
        print("What is LOGICAL OPERATORS?")
        print("Logical Operators are always used with conditional statement. They are use to reversed condition or combine.\n")
        print("__________________________________________________________________________________________")
        print("|                                                                                        |")
        print("(   L O G I C A L   O P E R A T O R S                                                    )")
        print("(________________________________________________________________________________________)")
        print("|                                                                                        |")
        print("|  and - Both Condition is TRUE                                                          |")
        print("|........................................................................................|")
        print("|                                                                                        |")
        print("|  or - One of the condition must be TRUE                                                |")
        print("|........................................................................................|")
        print("|                                                                                        |")
        print("|  not - Reverse the  result. TRUE = FALSE and FALSE = TRUE                              |")
        print("|........................................................................................|")
        print("|                                                                                        |")
        print("|  Example :                                                                             |")
        print("|                                                                                        |")
        print("|   age = 18                                     Take note : AND is all true.            |")
        print("|   got_vip = True                                           OR got atleast one true.    |")
        print("|                                                            NOT reverse the result.     |")
        print("|   if age >= 18 and got_vip :                                                           |")
        print("|      print(''Enjoy the party'')                                                        |")
        print("|   else :                                                                               |")
        print("|      print(''not allowed'')                                                            |")
        print("|                                                                                        |")
        print("|________________________________________________________________________________________|")
        print("|                                                                                        |")
        print("|   Example of NOT :                                                                     |")
        print("|                                                                                        |")
        print("|     sunny = True                                                                       |")
        print("|                                                                                        |")
        print("|     if not sunny :                                                                     |")
        print("|        print(''you can't play'')                                                       |")
        print("|     else :                                                                             |")
        print("|        print(''you can play'')                                                         |")
        print("|                                                                                        |")
        print("|________________________________________________________________________________________|\n")
        print("__________________________________________________________________________________________")
        print("|                                                                                        |")
        print("|                  C H A P T E R   7   P Y T H O N   L O O P S                           |")
        print("|________________________________________________________________________________________|")
        print("|                                                                                        |")
        print("|  What are LOOPS?                                                                       |")
        print("|                                                                                        |")
        print("|  Loops are used to repeat a block of code multiple times. Instead of writing the       |")
        print("|  same code again and again, we can use loops to make our program shorter and easier.   |")
        print("|________________________________________________________________________________________|\n")

        print("__________________________________________________________________________________________")
        print("|                                                                                        |")
        print("|                                 W H I L E   L O O P                                    |")
        print("|________________________________________________________________________________________|")
        print("|                                                                                        |")
        print("|  What is WHILE LOOP?                                                                    |")
        print("|                                                                                        |")
        print("|  A WHILE LOOP repeats a block of code as long as the condition is TRUE.                |")
        print("|                                                                                        |")
        print("|  SIMPLE MEANING: Repeat while the condition is TRUE.                                   |")
        print("|________________________________________________________________________________________|\n")

        print("STEP 1: BASIC SYNTAX")
        print("------------------------------------------------------------------------------------------")
        print("while condition:")
        print("    statement")
        print("------------------------------------------------------------------------------------------")
        print("while     - Starts the loop.")
        print("condition - Checks if the condition is TRUE or FALSE.")
        print("statement - The code that will repeat.\n")

        print("STEP 2: EXAMPLE")
        print("------------------------------------------------------------------------------------------")

        print("number = 1")
        print("")
        print("while number <= 5:")
        print("    print(number)")
        print("    number += 1")

        print("------------------------------------------------------------------------------------------")
        print("OUTPUT:")

        number = 1

        while number <= 5:
            print(number)
            number += 1

        print("------------------------------------------------------------------------------------------\n")

        print("STEP 3: HOW DOES IT WORK?")
        print("------------------------------------------------------------------------------------------")
        print("1. Set the starting number: number = 1")
        print("2. Check if number <= 5.")
        print("3. If TRUE, print the number.")
        print("4. Increase the number by 1 using number += 1.")
        print("5. Repeat until the condition becomes FALSE.")
        print("------------------------------------------------------------------------------------------\n")

        print("IMPORTANT REMINDER:")
        print("Always make sure that the condition will eventually become FALSE.")
        print("Otherwise, your program may create an INFINITE LOOP.\n")

        print("__________________________________________________________________________________________")
        print("|                                                                                        |")
        print("|                           F O R   L O O P                                              |")
        print("|________________________________________________________________________________________|")
        print("|                                                                                        |")
        print("|  What is FOR LOOP?                                                                      |")
        print("|                                                                                        |")
        print("|  A FOR LOOP repeats a block of code for each item in a sequence or for a specific     |")
        print("|  number of repetitions.                                                                |")
        print("|                                                                                        |")
        print("|  SIMPLE MEANING: Repeat for every item or number in a sequence.                        |")
        print("|________________________________________________________________________________________|\n")

        print("STEP 1: BASIC SYNTAX")
        print("------------------------------------------------------------------------------------------")
        print("for variable in sequence:")
        print("    statement")
        print("------------------------------------------------------------------------------------------")
        print("for      - Starts the loop.")
        print("variable - Stores the current item.")
        print("in       - Gets an item from the sequence.")
        print("sequence - The collection or range of items.")
        print("statement- The code that will repeat.\n")

        print("STEP 2: EXAMPLE")
        print("------------------------------------------------------------------------------------------")

        print("for number in range(1, 6):")
        print("    print(number)")

        print("------------------------------------------------------------------------------------------")
        print("OUTPUT:")

        for number in range(1, 6):
            print(number)

        print("------------------------------------------------------------------------------------------\n")

        print("STEP 3: UNDERSTANDING RANGE()")
        print("------------------------------------------------------------------------------------------")
        print("range(1, 6) generates numbers from 1 up to 5.")
        print("The ending number is NOT included.")
        print("------------------------------------------------------------------------------------------\n")

        print("ANOTHER EXAMPLE:")
        print("------------------------------------------------------------------------------------------")

        print('for name in ["Kevin", "John", "Mark"]:')
        print('    print("Hello", name)')

        print("------------------------------------------------------------------------------------------")
        print("OUTPUT:")

        for name in ["Kevin", "John", "Mark"]:
            print("Hello", name)

        print("------------------------------------------------------------------------------------------\n")

        print("__________________________________________________________________________________________")
        print("|                                                                                        |")
        print("|                 D I F F E R E N C E   O F   L O O P S                                  |")
        print("|________________________________________________________________________________________|")
        print("|                                                                                        |")
        print("|  WHILE LOOP: Repeats as long as a condition is TRUE.                                   |")
        print("|                                                                                        |")
        print("|  FOR LOOP  : Repeats through a sequence of items.                                      |")
        print("|                                                                                        |")
        print("|  WHILE LOOP: Useful when the number of repetitions is not known.                       |")
        print("|                                                                                        |")
        print("|  FOR LOOP  : Useful when the number of repetitions or items is known.                  |")
        print("|________________________________________________________________________________________|\n")

        print("------------------------------------------------------------------------------------------\n")
        print("__________________________________________________________________________________________")
        print("|                                                                                        |")
        print("|      SINCE I  DIDN'T  PUT DESIGN UNLIKE OTHER CHAPTER  LET ME GIVE YOU A SUMMARY       |")
        print("|________________________________________________________________________________________|")
        print("|                                                                                        |")
        print("|  1. A loop repeats a block of code.                                                    |")
        print("|  2. A WHILE LOOP repeats while its condition is TRUE.                                  |")
        print("|  3. A FOR LOOP repeats through a sequence.                                             |")
        print("|  4. The range() function generates a sequence of numbers.                              |")
        print("|  5. Indentation is important in Python loops.                                          |")
        print("|  6. An INFINITE LOOP happens when a loop never stops.                                  |")
        print("|________________________________________________________________________________________|\n")
else :
     print("\nJust put [PICK] or [LSBS].\n")
     exit()
while True :
    choi = input("Do you want to [PICK] or [LSBS] again? (Y/N) : ").upper()
    if choi == "Y" :

        pick = input("You want to learn step by step? or pick a lesson? (PICK/LSBS) : ").upper()
        if pick == "PICK":

            print(" ")
            choice = input("Choose Chapter 1 to 7 :")
            print(" ")

            print("_-" * 68)
            print("GOOD LUCK AND HAVE FUN! ദ്ദി*ˊᗜˋ*)")
            print("_-" * 68)
            print(" ")

            if choice == "1":
                print("__________________________________________________________________________________________")
                print("|                                                                                        |")
                print("|      C H A P T E R   1    I N T R O D U C T I O N    T O    P R O G R A M M I N G      |")
                print("|________________________________________________________________________________________|\n")

                print(
                    "Do you have any idea what's programming language is? if not, PROGRAMMING LANGUAGE is a special language")
                print("that computers understand and use to perform task.(。•̀ᴗ-)✧\n")
                print(
                    "Anyways PYTHON PROGRAMMING is widely used around the world because it was easy to learn, simple and readable.")
                print("It was created by Guido Van Rossum in 1991.\n")
                print("What do you need to start python?\n")
                print("_________________________________________________________________________")
                print("|`````P R O F E S S I O N A L   I D E S / C O D E S   E D I T O R S`````|")
                print("|_______________________________________________________________________|")
                print("| PYCHARM BY JET BRAINS.                                                |")
                print("| VS CODE  (VISUAL STUDIO CODE).                                        |")
                print("| JUPYTER NOTEBOOK/JUPYTER LAB.                                         |")
                print("|_______________________________________________________________________|\n")
                print("That's all for Chapter 1.")
                print("Easy Right? RIGHTTTTTTTTTTTTTTTT?. ＼(ˇ∇ˇ)／\n")
                print("_-" * 68)
                print("                                                         _________________________    ")
                print("                    /|      _____          _____       |   |     |     |    | |  |   ")
                print("     ,-----,       /  |____/__|__|_    ___/__|__|___   |___|_____|_____|____|_|___|  ")
                print("  ,--'---:---`--, /  |  _     |     `| |      |      `| |                    | |    | ")
                print(" ==(o)-----(o)==J    `(o)-------(o)=   `(o)------(o)'   `--(o)(o)--------------(o)--'  ")
                print("`````````````````````````````````````````````````````````````````````````````````````")
                print("_-" * 68)
                print(
                    "========== L O A D I N G   P L E A S E   W A I T ==========................................................")
                print("_-" * 68)
                print(" ")
                quizc1 = input("Would you like to take a quiz? (YES/NO) :").upper()

                pass_score = 3
                if quizc1 == "YES":

                    score = 0
                    print("[------------------------------------------------------------------------]")
                    print("| This quiz has 5 items. Write T if True. F if False.                    |")
                    print("|________________________________________________________________________|")

                    answer = input("1. Python is not part of special language/programming language. Answer :\n").upper()
                    if answer == "F":
                        score += 1
                    answer = input("2.Guido van Created python in 1992. Answer :\n").upper()
                    if answer == "F":
                        score += 1
                    answer = input("3.Python is readable, easy to learn and simple. Answer :\n").upper()
                    if answer == "T":
                        score += 1
                    answer = input("4.Pycharm is one of the ides and professional code editors.Answer :\n").upper()
                    if answer == "T":
                        score += 1
                    answer = input("5.Computers don't understand programming language. Answer :\n").upper()
                    if answer == "F":
                        score += 1

                    print(" ")
                    print("_-" * 68)
                    print(" ")
                    print(" __________________________________________________")
                    print(" |   *************************                    |")
                    print(f" |   *  You got {score} / 5!       *                    |")
                    print(" |   *************************                    |\n")
                    print(" |________________________________________________|")

                    if score >= pass_score:

                        print(" | Congrats! You passed the quiz! d-(^_^)z        |")
                        print(" |________________________________________________|")
                        print(" ")
                        print("_-" * 68)
                    else:
                        print(" | You Failed, Keep Going! (9'-')9                |")
                        print(" |________________________________________________|")
                        print(" ")
                        print("_-" * 68)
                elif quizc1 == "NO" :
                    print("I understand.")
                else :
                    print("Just put YES or NO.")
            elif choice == "2":
                print("__________________________________________________________________________________________")
                print("|                                                                                        |")
                print("|      C H A P T E R   2    P Y T H O N   B A S I C   S Y N T A X                        |")
                print("|________________________________________________________________________________________|\n")

                print("What is SYNTAX.\n")
                print("SYNTAX refers to the set of rules that tells us how correctly write a program in Python.\n")
                print("=--PYTHON SYNTAX--=")
                print("These things is really important to understand, remember this. Python is case sensitive ")
                print("because python treats upper and lower case differently.Also Python need Indentation or called")
                print("spaces to define blocks of code.  <(-^,^-)=b \n")
                print("For example....\n")
                print("Remember the ('') Imagine this as quotation mark. Thank you for understanding!\n")
                print("__________________________________________________________________________________________")
                print("|  Python Case Sensitive.                                                                |")
                print("|                                                                                        |")
                print("|  (1). name = ''Kevin''               (2). name = ''Kevin''                             |")
                print("|       print(Name)                       print(name)                                    |")
                print("|                                                                                        |")
                print("|    The number  1 is wrong. Number 2 is correct. Why?                                   |")
                print("|    because even though the word NAME is same.                                          |")
                print("|    You can see that, 1 has lowercase variable storage.                                 |")
                print("|    But has upper case with print(Name).                                                |")
                print("|                                                                                        |")
                print("|    Keyword : If it's lower. It's lower. If it's upper. It's upper.                     |")
                print("|                                                                                        |")
                print("|  Indentations(Spaces).                                                                 |")
                print("|                                                                                        |")
                print("|   (1). age = 18                    (2). age = 18                                       |")
                print("|        if age >= 18 :                   if age >= 18 :                                 |")
                print("|          print(''Adult'')               print(''Adult'')                               |")
                print("|                                                                                        |")
                print("|   Number 2 is incorrect because it is not intended or he doesn't have spaces           |")
                print("|   to get inside the block. While number 1 has spaces that's why it's intended.         |")
                print("|                                                                                        |")
                print("|    Keyword: Use spaces and make sure it is align perfectly in your coding              |")
                print("|             to get intended.                                                           |")
                print("|________________________________________________________________________________________|\n")

                print("_-" * 68)
                print("." * 136)
                print("_-" * 68)
                print("                                                      __  _")
                print("      ...........................                     | `/ |     ")
                print("      |                         |                      |__`!   ")
                print("      | PRINTING                |_  ___                / ,' `-.__________________   ")
                print("      |           OUTPUT        | -    ________________'-'|_____                LI`-.   ")
                print("      ...........................                         <____()-=O=O=O=O=O=[]====--)")
                print("                                                              `.___ ,-----,_______...-'")
                print("                                                                   /    .'")
                print("                                                                  /   .'")
                print("                                                                 /  .'  ")
                print("                                                                `-'")
                print("_-" * 68)
                print("." * 136)
                print("_-" * 68)

                print("\nNow let's proceed to PRINTING OUTPUT.\n")
                print("PRINTING OUTPUT - It displayed information through your screen.")
                print("PRINTING NUMBERS - You can put numbers without quotation marks but there's different.See")
                print("the example below.\n")
                print("Remember the ('') Imagine this as quotation mark. Thank you for understanding!\n")
                print("__________________________________________________________________________________________")
                print("|                                                                                        |")
                print("|      (1). print(100)            (2). print(''500'')                                    |")
                print("|           print(25.5)                print(''112'')                                    |")
                print("|                                                                                        |")
                print("|      1 and 2 are both correct, they just have different data types.                    |")
                print("|      The number 1 in line one is called INTEGERS. Line two is called FLOAT.            |")
                print("|      While number 2 is called STRING because it has quotation mark.                    |")
                print("|                                                                                        |")
                print("|                                                                                        |")
                print("|                                                                                        |")
                print("|________________________________________________________________________________________|\n")

                print("() - Open and close Parenthesis Is the reason why program contain to be displayed.")
                print("('') - Quotation mark is the sign for string because without quotation mark,")
                print("you get either error or variables.")
                print("Value - This is (STRING, NUMBER, VARIABLE and ETC.)\n")
                print("_-" * 68)
                print("\n                        ( -_•)ᡕᠵデᡁ᠊╾━--- P Y T H O N   C O M M E N T S.\n")
                print("_-" * 68)
                print(
                    "PYTHON COMMENTS is easy to remember just put HASHTAG (#) and that's it you have comment. ദ്ദി ˉ͈̀꒳ˉ͈́ )✧")
                print("Kidding aside. there is two types of comments.")
                print("The first one is SINGLE LINE COMMENT. The second one is MULTI LINE COMMENTS.")
                print("\nRemember the ('') Imagine this as quotation mark. Thank you for understanding!\n")
                print("__________________________________________________________________________")
                print("|``````````````````````P Y T H O N   C O M M E N T S`````````````````````|")
                print("|________________________________________________________________________|")
                print("|                                                                        |")
                print("| SINGLE LINE COMMENTS = (#)                                             |")
                print("|                                                                        |")
                print("| MULTI LINE COMMENTS = ('''''') at top and bottom                       |")
                print("|                                                                        |")
                print("|   Take note: Comments are ignored by python, and used to               |")
                print("|              explain   the code.                                       |")
                print("|________________________________________________________________________|\n")
                print("_-" * 68)
                print("." * 136)
                print("_-" * 68)
                print("\n          _  _")
                print("         ( `   )_")
                print("        (    )    `)")
                print("      (_   (_ .  _) _)")
                print(
                    "                                  V A R I A B L E S ,                                                ")
                print(
                    "                                         C O N S T A N T S ,                                     ")
                print("           _                                     A N D ")
                print("         -=|`|                         D A T A   T Y P E S.")
                print("     || ____|_|__                                                                 _")
                print("   -=|c`         L`)                                  -----                       (  )")
                print("      `~~~~~| |~~`                                                             ( `  ) . )")
                print("        -==| |                        - - - - -                              (_, _(  ,_)_)")
                print("          '-'                                                                    \n")
                print("_-" * 68)
                print("." * 136)
                print("_-" * 68)
                print("\nWhat is VARIABLES?\n")
                print("VARIABLES is the storage location where you can  keep data in program.\n")
                print("TAKE NOTE :")
                print("Variables can have short name like (a,b,c) or more like (name, total_val, char).")
                print("Variables can't start with numbers. It starts with underscore(_) or letter.")
                print("Like i said before. Python case is sensitive. If you have variable (NAME, name), ")
                print("this two variable are from different data.\n")
                print("\nRemember the ('') Imagine this as quotation mark. Thank you for understanding!\n")
                print("__________________________________________________________________________________________")
                print("| In programming we store data in variables. we put value  to variable,                  |")
                print("| using ASSIGNMENT OPERATOR.                                                             |")
                print("|                                                                                        |")
                print("| For example :                                                                          |")
                print("|                                                                                        |")
                print("|           Character_one = ''Tung Tung Sahur''                                          |")
                print("|                   ^                  ^                                                 |")
                print("|          #This is variable,     #This is Value the data we store in variable.          |")
                print("|           the  name we use to present data.             (It can be text, num and etc). |")
                print("|                                                                                        |")
                print("|           Is that Clear? <(-^,^-)=b                                                    |")
                print("|                                                                                        |")
                print("| Also you can print multiple variables using add(+) or comma(,).                        |")
                print("|                                                                                        |")
                print("| For Example :                                                                          |")
                print("|           a = ''Keep''                                                                 |")
                print("|           b = ''Going''                                                                |")
                print("|           c = ''embrace fear''                                                         |")
                print("|                                                                                        |")
                print("|           print (a + b + c) > output : Keep going embrace fear                         |")
                print("|           print (a, b, c)   > output : Keep going embrace fear                         |")
                print("|________________________________________________________________________________________|\n")
                print("_-" * 68)
                print("\n                        ( -_•)ᡕᠵデᡁ᠊╾━--- D A T A   T Y P E S   I N    P Y T H O N.\n")
                print("_-" * 68)
                print("DATA TYPES - Tells the python on what kind of variable we stored.\n")
                print("Lets focus on :\n")
                print("STRING - More on text inside quotation mark.")
                print("Example : (''Kevin'' , ''Mandal'' , ''Perez'') \n")
                print("INTEGERS(int) - More on Whole numbers. ")
                print("Example : (12, 22 , -18)\n")
                print("float - It has decimal point.")
                print("Example : (20.07, 18.22, -17.2)\n")
                print("bool(boolean) - Represent one of two value it's either TRUE or FALSE.")
                print("Example : (TRUE, FALSE)\n")
                print("This is the example of how it works.")
                print("__________________________________________________________________________________________")
                print("|                                                                                        |")
                print("|    name = ''Kevin''               >  String                                            |")
                print("|    age = 18                       >  Integers                                          |")
                print("|    grade_inpython = 61.30         >  Float                                             |")
                print("|    is_enrolled = False            >  Boolean                                           |")
                print("|                                                                                        |")
                print("|    print(name)                                                                         |")
                print("|    print(age)                                                                          |")
                print("|    print(grade_inpython)                                                               |")
                print("|    print(is_enrolled)                                                                  |")
                print("|                                                                                        |")
                print("|________________________________________________________________________________________|\n")
                print("_-" * 68)
                print("       __|__          ============================================           __|__            ")
                print("--------(_)--------   L O A D I N G    P L E A S E    W A I T.....    --------(_)--------")
                print(
                    "  O  O       O  O     ============================================      O  O       O  O            ")
                print("_-" * 68)
                print("T H A T ' S   T H E   E N D  O F   C H A P T E R   T W O ")
                print("_-" * 68)
                quizc2 = input("Would you like to take a quiz? (YES/NO) :").upper()

                pass_score = 9
                if quizc2 == "YES":
                    score = 0
                    print("[------------------------------------------------------------------------]")
                    print("| This quiz have 15 items. Multiple choice and identification.           |")
                    print("|________________________________________________________________________|")

                    print("\n1.Which one is correct, see the table below.")
                    print("__________________________________________________________________________________________")
                    print("|   A.                      B.                                                           |")
                    print("|   Name = 'kevin'          name = ''kevin''                                             |")
                    print("|   print(name)             print(name)                                                  |")
                    print(
                        "__________________________________________________________________________________________\n")

                    answer = input("Answer A or B? : ").upper()
                    if answer == "B":
                        print("\nGreat that's Correct! {(^_^)}")
                        print(
                            "__________________________________________________________________________________________\n")
                        score += 1
                    else:
                        print("It's letter B. (-_-)")
                        print(
                            "__________________________________________________________________________________________\n")

                    print("\n2. You need spaces to get intended, this is called _______ .")
                    answer = input("Answer : ").upper()

                    if answer == "INDENTATIONS" or answer == "INDENTATION":
                        print("\nGreat that's Correct! {(^_^)}")
                        print(
                            "__________________________________________________________________________________________\n")
                        score += 1
                    else:
                        print("\nWrong! The correct answer is Indentation.(-_-)")
                        print(
                            "__________________________________________________________________________________________\n")

                    print("\n3. Sign of multiple line comment.")
                    print("A. ###")
                    print("B. ''''''")
                    print("C. #")

                    answer = input("Answer : ").upper()
                    if answer == "B":
                        print("\nGreat that's Correct! {(^_^)}")
                        print(
                            "__________________________________________________________________________________________\n")
                        score += 1
                    else:
                        print("Wrong answer. it's B. (-_-)")
                        print(
                            "__________________________________________________________________________________________\n")

                    print("\n4. Variables name can start with numbers.")
                    print("A. Yes")
                    print("B. Maybe")
                    print("C. No")
                    print("D. You can put whatever you like")

                    answer = input("Answer : ").upper()
                    if answer == "C":
                        print("\nGreat that's Correct! {(^_^)}")
                        print(
                            "__________________________________________________________________________________________\n")
                        score += 1
                    else:
                        print("\nWrong. The answer is C. (-_-)")
                        print(
                            "__________________________________________________________________________________________\n")

                    print("\n5. It is _________ where data can be kept in a program.")

                    answer = input("Answer : ").upper()
                    if answer == "VARIABLES" or answer == "VARIABLE":
                        print("\nGreat that's Correct! {(^_^)}")
                        print(
                            "__________________________________________________________________________________________\n")
                        score += 1
                    else:
                        print("\nWrong! The correct answer is Variable. (-_-)")
                        print(
                            "__________________________________________________________________________________________\n")

                    print("\n6. It refers to the set of rules for writing a correct Python program.")
                    print("A. Variables")
                    print("B. Syntax")
                    print("C. Comments")
                    print("D. Indentation")

                    answer = input("Answer : ").upper()
                    if answer == "B":
                        print("\nGreat that's Correct! {(^_^)}")
                        print(
                            "__________________________________________________________________________________________\n")
                        score += 1
                    else:
                        print("\nWrong! The correct answer is B. Syntax. (-_-)")
                        print(
                            "__________________________________________________________________________________________\n")

                    print("\n7. It is the storage location where you can keep data in a program.")
                    print("A. Variable")
                    print("B. String")
                    print("C. Float")
                    print("D. Boolean")

                    answer = input("Answer : ").upper()
                    if answer == "A":
                        print("\nGreat that's Correct! {(^_^)}")
                        print(
                            "__________________________________________________________________________________________\n")
                        score += 1
                    else:
                        print("\nWrong! The correct answer is A. Variable. (-_-)")
                        print(
                            "__________________________________________________________________________________________\n")

                    print("\n8. We put value to variable using______.")
                    print("A. Output")
                    print("B. Integer")
                    print("C. Comments")
                    print("D. Assignment Operator")

                    answer = input("Answer : ").upper()
                    if answer == "D":
                        print("\nGreat that's Correct! {(^_^)}")
                        print(
                            "__________________________________________________________________________________________\n")
                        score += 1
                    else:
                        print("\nWrong! The correct answer is D.Assignment Operator. (-_-)")
                        print(
                            "__________________________________________________________________________________________\n")

                    print("\n9. It represents text enclosed in quotation marks.")
                    print("A. Integer")
                    print("B. Boolean")
                    print("C. Float")
                    print("D. String")

                    answer = input("Answer: ").upper()
                    if answer == "D":
                        print("\nGreat that's Correct! {(^_^)}")
                        print(
                            "__________________________________________________________________________________________\n")
                        score += 1
                    else:
                        print("\nWrong! The correct answer is D. String. (-_-)")
                        print(
                            "__________________________________________________________________________________________\n")

                    print("\n10. It represents one of two values: True or False.")
                    print("A. Float")
                    print("B. Boolean")
                    print("C. String")
                    print("D. Integer")

                    answer = input("Answer : ").upper()
                    if answer == "B":
                        print("\nGreat that's Correct! {(^_^)}")
                        print(
                            "__________________________________________________________________________________________\n")
                        score += 1
                    else:
                        print("\nWrong! The correct answer is B. Boolean. (-_-)")
                        print(
                            "__________________________________________________________________________________________\n")

                    print(
                        "\n11. These are used to explain or describe code and are ignored during normal Python execution.")

                    answer = input("Answer: ").upper()
                    if answer == "COMMENTS" or answer == "COMMENT":
                        print("Great that's Correct! {(^_^)}")
                        print(
                            "__________________________________________________________________________________________\n")
                        score += 1
                    else:
                        print("\nWrong! The correct answer is Comments.(-_-)")
                        print(
                            "__________________________________________________________________________________________\n")

                    print("\n12. It is a data type that has decimal point.")

                    answer = input("Answer : ").upper()
                    if answer == "FLOAT":
                        print("\nGreat That's Correct! {(^_^)}")
                        print(
                            "__________________________________________________________________________________________\n")
                        score += 1
                    else:
                        print("\nWrong! The correct answer is float. (-_-)")
                        print(
                            "__________________________________________________________________________________________\n")

                    print("\n13. It's data types with whole number.")

                    answer = input("Answer : ").upper()
                    if answer == "INTEGERS" or answer == "INTEGER" or answer == "INT":
                        print("\nGreat that's Correct! {(^_^)}")
                        print(
                            "__________________________________________________________________________________________\n")
                        score += 1
                    else:
                        print("\nWrong! The correct answer is Integer. (-_-)")
                        print(
                            "__________________________________________________________________________________________\n")

                    print("\n14. We store this in variable.")

                    answer = input("Answer : ")
                    if answer == "VALUE" or "VALUES":
                        print("\nGreat that's Correct! {(^_^)}")
                        print(
                            "__________________________________________________________________________________________\n")
                        score += 1
                    else:
                        print("\nWrong. It is VALUE (-_-)")
                        print(
                            "__________________________________________________________________________________________\n")

                    print("\n15. Name and name variable are same.")

                    answer = input("\nAnswer (Yes/No) : ").upper
                    if answer == "NO":
                        print("\nGreat that's Correct! {(^_^)}")
                        print(
                            "__________________________________________________________________________________________\n")
                        score += 1
                    else:
                        print("\nWrong. You it's not the same. (-_-)  ")
                        print(
                            "__________________________________________________________________________________________\n")

                    print(" ")
                    print("_-" * 68)
                    print(" ")
                    print(" __________________________________________________")
                    print(" |   *************************                    |")
                    print(f" |   *  You got {score} / 15!      *                   |")
                    print(" |   *************************                    |\n")
                    print(" |________________________________________________|")

                    if score >= pass_score:

                        print(" | Congrats! You passed the quiz! d-(^_^)z        |")
                        print(" |________________________________________________|")
                        print(" ")
                        print("_-" * 68)
                    else:
                        print(" | You Failed, Keep Going! (9'-')9                |")
                        print(" |________________________________________________|")
                        print(" ")
                        print("_-" * 68)
                elif quizc2 == "NO" :
                    print("I understand.")
                else :
                    print("Just put YES or NO")
            elif choice == "3":
                print(
                    "___________________________________________________________________________________________________")
                print(
                    "|                                                                                                 |")
                print(
                    "|      C H A P T E R   3    A R I T H M E T I C   O P E R A T O R   A N D   E X P R E S S I O N   |")
                print(
                    "|_________________________________________________________________________________________________|\n")

                print("What is ARITHMETIC OPERATOR?\n")
                print("ARITHMETIC OPERATOR are symbol we use in program to execute mathematical operation. (^_^) ")
                print("__________________________________________________________________________________________")
                print("|                                                                                        |")
                print("(   O P E R A T O R S   D E F I N I T I O N S   A N D   E X A M P L E S                  )")
                print("(________________________________________________________________________________________)")
                print("|                                                                                        |")
                print("|  ADDITION (+)  - Add two value  [1 + 5 = 6]                                            |")
                print("|........................................................................................|")
                print("|                                                                                        |")
                print("|  SUBTRACTION (-)   - Subtracts second value to first value  [10 - 5 = 5]               |")
                print("|........................................................................................|")
                print("|                                                                                        |")
                print("|  MULTIPLICATION (*)   - Multiply two values  [5 * 2 = 10]                              |")
                print("|........................................................................................|")
                print("|                                                                                        |")
                print("|  DIVISION(float) (/)   - Divide two value and return decimal   [5 / 2 = 2.0]           |")
                print("|........................................................................................|")
                print("|                                                                                        |")
                print("|  FLOOR DIVISION (//)   - Divide two value but return whole number  [10 // 2 = 5]       |")
                print("|........................................................................................|")
                print("|                                                                                        |")
                print("|  MODULUS (%)   - Return the remainder of division    [5 % 2 = 1]                       |")
                print("|........................................................................................|\n")
                print("Now if you think of it, What is expression?\n")
                print("EXPRESSION is the combination of values,variables and operator. It is useful everytime.\n")
                print("Let's see the example below.")
                print("__________________________________________________________________________")
                print("|`````````````````E X P R E S S I O N   I N   P Y T H O N````````````````|")
                print("|________________________________________________________________________|")
                print("|                                                                        |")
                print("| K = 12                      Take note: You can use it                  |")
                print("| P = 22                                 as long as you want.            |")
                print("| M = 27                                 But make sure it is right.      |")
                print("|                                                                        |")
                print("| tots = K + P + M                                                       |")
                print("| print(''Your total is'', tots)                                         |")
                print("|________________________________________________________________________|")
                print("|                                                                        |")
                print("| Output : Your total is 61                                              |")
                print("|........................................................................|\n")
                print("Did you know PEMDAS? |_(^_^)")
                print("PEMDAS is like combining all operators.\n")
                print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
                print("[________________________________________________________________________]")
                print("| P  for PARENTHESIS [()]   FIRST                                        |")
                print("| E  for EXPONENTS   [**]   SECOND                                       |")
                print("| M  for MULTIPLY    [*]    THIRD                                        |")
                print("| D  for DIVISION    [/]    FOURTH                                       |")
                print("| A  for ADDITION    [+]    FIFTH                                        |")
                print("| S  for SUBTRACTION [-]    SIXTH                                        |")
                print("|                                                                        |")
                print("|  Take Note: Use this by order! =(>_<)=                                 |")
                print("|                                                                        |")
                print("|                                                                        |")
                print("|........................................................................|\n")
                print("_-" * 68)
                print("      _.-'''''-._     .    H E L L O. I' M   V E R I T Y        ; ;     .      .     ,     ;                ")
                print("    .'  _     _  '.              .        L E T ' S   P L A Y             .     .                         ")
                print("   |   (o)   (o)   |       .     .   .                A         ,         ,         ;            ;          ")
                print("  |                 |                  G A M E.............           ;               ;    .               ")
                print("  |  (           )  |       ;    .    .                     ;                .                  .          ")
                print("   |  '.       .'  |                           ;                      ;          ;  ;     .       .           ")
                print("    '.  `'---'`  .'                ;                                                         ;            ")
                print("      '-._____.-'      .       ;             ;     .      ;          .      .          ;           .          ")
                print("_-" * 68)
                print(" ")
                sagot = input("Do you want to play the game? (YES/OK) : ").upper()
                if sagot == "YES" or sagot == "OK":
                    print("+------------------------------------------------------------------------+")
                    print("| Sorry you can't scape me. :  )                                         |")
                    print("|                                                                        |")
                    print("|   In this game you have 7 life. I called this TRICKY GAME....          |")
                    print("|   Alright. I know it's corny  [TvT]. In this game there are many       |")
                    print("|   types of  symbol but beware because there are operators.             |")
                    print("|   If the operators is familiar with you, use                           |")
                    print("|   (add,minus,multiply,floor division or modulus). AT YOUR OWN RISK.    |")
                    print("|                                                                        |")
                    print("|    For Example : = + =                                                 |")
                    print("|    Answer : 2                                                          |")
                    print("|                                                                        |")
                    print("|                                                                        |")
                    print("|   Life Badge : Hacker - 7    Pro - 5   Average - 3                     |")
                    print("|                                                                        |")
                    print("+------------------------------------------------------------------------+\n")

                    Life = 7

                    print("     -|  |___________________________________________|  |-")
                    print("    (_|  |___________________________________________|  |_)")
                    print("      |  |       +-+-+-+-+-LEVEL ONE-+-+-+-+-+       |  |")
                    print("      |  | 1. = + = + = + =                          |  |")
                    print("      |  |                                           |  |")
                    print("      |  |___________________________________________|  |")
                    print("    (_|  |___________________________________________|  |_)")
                    ans = input("      |  | Answer :")

                    if ans == "4":
                        print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
                        print("          ( ( You win!              ( (")
                        print("           ) ) Correct answer is 4.  ) )")
                        print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
                        print(
                            "__________________________________________________________________________________________\n")
                    else:
                        Life -= 1
                        print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
                        print("          ( ( You lost!             ( (")
                        print("          ) ) Correct answer is 4.  ) )")
                        print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
                        print(
                            "__________________________________________________________________________________________\n")

                    print("     -|  |___________________________________________|  |-")
                    print("    (_|  |___________________________________________|  |_)")
                    print("      |  |       +-+-+-+-+-LEVEL TWO-+-+-+-+-+       |  |")
                    print("      |  | 2. _ - _ + _ _ _ + _ = - _ =              |  |")
                    print("      |  |                                           |  |")
                    print("      |  |___________________________________________|  |")
                    print("    (_|  |___________________________________________|  |_)")
                    ans = input("      |  | Answer :")
                    if ans == "3":
                        print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
                        print("          ( ( You win!              ( (")
                        print("           ) ) Correct answer is 3.  ) )")
                        print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
                        print(
                            "__________________________________________________________________________________________\n")

                    else:
                        Life -= 1
                        print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
                        print("          ( ( You lost!             ( (")
                        print("           ) ) Correct answer is 3.  ) )")
                        print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
                        print(
                            "__________________________________________________________________________________________\n")

                    print("     -|  |___________________________________________|  |-")
                    print("    (_|  |___________________________________________|  |_)")
                    print("      |  |       +-+-+-+-+-LEVEL THREE-+-+-+-+-+     |  |")
                    print("      |  | 3. ^ ^ * _ _ _ - ! + _ _ _ - ^ ^          |  |")
                    print("      |  |                                           |  |")
                    print("      |  |___________________________________________|  |")
                    print("    (_|  |___________________________________________|  |_)")
                    ans = input("      |  | Answer :")
                    if ans == "6":
                        print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
                        print("          ( ( You win!              ( (")
                        print("           ) ) Correct answer is 6.  ) )")
                        print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
                        print(
                            "__________________________________________________________________________________________\n")

                    else:
                        Life -= 1
                        print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
                        print("          ( ( You lost!             ( (")
                        print("           ) ) Correct answer is 6.  ) )")
                        print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
                        print(
                            "__________________________________________________________________________________________\n")
                    print("     -|  |___________________________________________|  |-")
                    print("    (_|  |___________________________________________|  |_)")
                    print("      |  |       +-+-+-+-+-LEVEL FOUR-+-+-+-+-+      |  |")
                    print("      |  | 4. # # # # // _ _ + = = = - $ + ! !       |  |")
                    print("      |  |                                           |  |")
                    print("      |  |___________________________________________|  |")
                    print("    (_|  |___________________________________________|  |_)")
                    ans = input("      |  | Answer :")

                    if ans == "6":
                        print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
                        print("          ( ( You win!              ( (")
                        print("           ) ) Correct answer is 6.  ) )")
                        print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
                        print(
                            "__________________________________________________________________________________________\n")

                    else:
                        Life -= 1
                        print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
                        print("          ( ( You lost!             ( (")
                        print("           ) ) Correct answer is 6.  ) )")
                        print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
                        print(
                            "__________________________________________________________________________________________\n")

                    print("     -|  |_____________________________________________|  |-")
                    print("    (_|  |_____________________________________________|  |_)")
                    print("      |  |       +-+-+-+-+-LEVEL FIVE-+-+-+-+-+        |  |")
                    print("      |  | 5. ^ ^ ^ ^ ! $ $ $ # _ % ) _ _ + ~ ~  ~ - < |  |")
                    print("      |  |                                             |  |")
                    print("      |  |_____________________________________________|  |")
                    print("    (_|  |_____________________________________________|  |_)")
                    ans = input("      |  | Answer :")
                    if ans == "3":
                        print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
                        print("          ( ( You win!              ( (")
                        print("           ) ) Correct answer is 3.  ) )")
                        print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
                        print(
                            "__________________________________________________________________________________________\n")


                    else:
                        Life -= 1
                        print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
                        print("          ( ( You lost!             ( (")
                        print("           ) ) Correct answer is 3.  ) )")
                        print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
                        print(
                            "__________________________________________________________________________________________\n")

                    print("     -|  |_______________________________________________|  |-")
                    print("    (_|  |_______________________________________________|  |_)")
                    print("      |  |       +-+-+-+-+-LEVEL SIX-+-+-+-+-+           |  |")
                    print("      |  | 6. ^ ^ _ * _ _ _ = _ + ~ ~ - ~ + > > > // [ [ |  |")
                    print("      |  |                                               |  |")
                    print("      |  |_______________________________________________|  |")
                    print("    (_|  |_______________________________________________|  |_)")
                    ans = input("      |  | Answer :")
                    if ans == "17":
                        print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
                        print("          ( ( You win!               ( (")
                        print("           ) ) Correct answer is 17.  ) )")
                        print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
                        print(
                            "__________________________________________________________________________________________\n")

                    else:
                        Life -= 1
                        print("          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
                        print("          ( ( You lost!             ( (")
                        print("           ) ) Correct answer is 17. ) )")
                        print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
                        print(
                            "__________________________________________________________________________________________\n")

                    print("     -|  |_______________________________________________|  |-")
                    print("    (_|  |_______________________________________________|  |_)")
                    print("      |  |       +-+-+-+-+-LEVEL SEVEN-+-+-+-+-+         |  |")
                    print("      |  | 7. < < < + ^ ^ ^ ^ - ~ * { { - : : : : :      |  |")
                    ans = input("      |  | Answer :")
                    print("      |  |                                               |  |")
                    print("      |  |_______________________________________________|  |")
                    print("    (_|  |_______________________________________________|  |_)")
                    if ans == "7":
                        print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
                        print("          ( ( You win!              ( (")
                        print("           ) ) Correct answer is 7.  ) )")
                        print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
                        print(
                            "__________________________________________________________________________________________\n")

                    else:
                        Life -= 1
                        print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
                        print("          ( ( You lost!             ( (")
                        print("           ) ) Correct answer is 7.  ) )")
                        print("           -_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
                        print(
                            "__________________________________________________________________________________________\n")
                    print("_-" * 68)
                    print("." * 136)
                    print("_-" * 68)
                    print("\n__________________________________________________")
                    print(" |   *************************                    |")
                    print(f" |   *  You got {Life} LIFE!      *                    |")
                    print(" |   *************************                    |")
                    print(" |________________________________________________|\n")
                    if Life > 6 or Life >= 7:
                        print("             ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
                        print("             | Congrats you got Hacker Badge.|")
                        print("             ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
                        print("_-" * 68)
                    elif Life >= 4 or Life < 5:
                        print("             >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        print("             + Congrats you got Pro Badge.+")
                        print("             >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        print("_-" * 68)
                    elif Life == 3:
                        print("            ================================")
                        print("            Nice Try! You got Average Badge.")
                        print("            ================================")
                        print("_-" * 68)
                    else:
                        print("            ...................")
                        print("            Review Chapter 3!")
                        print("            ...................")
                        print("_-" * 68)
                        print("." * 136)
                        print("_-" * 68)
                    print("                    *****************")
                    print("               ******               ******")
                    print("           ****                           ****")
                    print("        ****                                 ***")
                    print("      ***                                       ***")
                    print("     **           ***               ***           **")
                    print("   **           *******           *******          ***")
                    print("  **            *******           *******            **")
                    print(" **             *******           *******             **")
                    print(" **               ***               ***               **")
                    print("=================================================================================")
                    print("     W I N    O R    L O S E    Y O U    M U S T    T A K E    T H I S   T E S T.")
                    print("=================================================================================")
                    print("In this test you will just put The following operators (+, -, *, //, %).\n")
                    score = 0
                    print("   _.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._")
                    print(".-'---      - ---     --     ---   -----   - --       ----  ----   -     ---`-.")
                    print(" )  [1.] 5 _ 8 = 13         [6.] 10 _ 3 = 1                                  (")
                    print("(                                                                             )")
                    print(" )  [2.] 10 _ 2 = 8         [7.] 90 _ 3 = 30                                 (")
                    print("(                                                                             )")
                    print(" )  [3.] 8 _ 4 = 32         [8.] 500 _ 11 = 5                                (")
                    print("(                                                                             )")
                    print(" )  [4.] 6 _ 8 = 14                                                          (")
                    print("(                                                                             )")
                    print(" )  [5.] 10 _ 2 = 5                                                          (")
                    print("(                                                                             )")
                    print(" )                                                                           (")
                    print("(___       _       _       _       _       _       _       _       _       ___)")
                    print("    (__  _) ( __ _) (__  _) (__ _ ) `-._.-' ( _ __) (_  __) (_ __ ) (_  __)")
                    print("    ( _ __) (_  __) (__ __) `-._.-'         `-._.-' (__ __) (__  _) (__ _ )")
                    print("    (__  _) (_ _ _) `-._.-'                         `-._.-' (_ _ _) (_  __)")
                    print("    (_ ___) `-._.-'                                         `-._.-' (___ _)")
                    print("    `-._.-'                                                         `-._.-'\n")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                    print("[1.] 5 _ 8 = 13")
                    ans = input(" Answer number 1 :")
                    if ans == "+":
                        score += 1
                    print("[2.] 10 _ 2 = 8")
                    ans = input(" Answer number 2 :")
                    if ans == "-":
                        score += 1
                    print("[3.] 8 _ 4 = 32")
                    ans = input(" Answer number 3 :")
                    if ans == "*":
                        score += 1
                    print("[4.] 6 _ 8 = 14")
                    ans = input(" Answer number 4 :")
                    if ans == "+":
                        score += 1
                    print("[5.] 10 _ 2 = 5")
                    ans = input(" Answer number 5 :")
                    if ans == "//":
                        score += 1
                    print("[6.] 10 _ 3 = 1")
                    ans = input(" Answer number 6 :")
                    if ans == "%":
                        score += 1
                    print("[7.] 90 _ 3 = 30")
                    ans = input(" Answer number 7 :")
                    if ans == "//":
                        score += 1
                    print("[8.] 500 _ 11 = 5")
                    ans = input(" Answer number 8 :")
                    if ans == "%":
                        score += 1
                        if score >= 6:
                            print("==============================+++++++++++++++++++++++++++++++++++++++++++++")
                            print(f"You got {score} / 8")
                            print("Congrats, That's a great work!")
                            print("==============================+++++++++++++++++++++++++++++++++++++++++++++")
                        elif score > 4 or score < 5:
                            print("==============================+++++++++++++++++++++++++++++++++++++++++++++")
                            print(f"You got {score} / 8")
                            print("Nice, That's a great work!")
                            print("==============================+++++++++++++++++++++++++++++++++++++++++++++")
                        else:
                            print("==============================+++++++++++++++++++++++++++++++++++++++++++++")
                            print(f"You got {score} / 8")
                            print("REVIEW THE CHAPTER 3!")
                            print("==============================+++++++++++++++++++++++++++++++++++++++++++++")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("**       *                                     *       **")
                    print("**      **                                     **      **")
                    print(
                        " **   ****                                     ****   **        T H A T ' S    T H E    E N D         ")
                    print(
                        " **      **                                   **      **                                              ")
                    print(
                        "  **       ***                             ***       **                      O F                         ")
                    print(
                        "  **       ***                             ***       **          C H A P T E R   T W O!                                     ")
                    print("     **         ******             ******         **")
                    print("      ***            ***************            ***")
                    print("        ****                                 ****")
                    print("           ****                           ****")
                    print("               ******               ******")
                    print("                    *****************")

            elif choice == "4":
                print(
                    "________________________________________________________________________________________________")
                print(
                    "|                                                                                              |")
                print(
                    "|      C H A P T E R   4    B A S I C   I N P U T   A N D   O U T P U T   I N  P Y T H O N     |")
                print(
                    "|______________________________________________________________________________________________|\n")
                print("What is INPUT?\n")
                print("This is where you want to ask something and respond.\n")
                print("Using INPUT you can able to type inside your Output. ")
                print("For example :\n")
                print("Remember the ('') Imagine this as quotation mark. Thank you for understanding!\n")
                print("                                    ____________________________")
                print("A S K * * A S K * * A S K * * A    |  ________________________  |")
                print("S                             S    | |                        | |====================================================]")
                print("K                             K    | |   Name : Kevin         | |  < You can put any names you want. But not number. ]")
                print("*  name = input(''Name :'')   *    | |   Name is Kevin        | |  < This is how it works.                           ] ")
                print("*  print(''Name is'', Name)   *    | |                        | |  < This is STRING                                  ]")
                print("A                             A    | |                        | |  ~Num1 = int(input(''Enter Number :''))            ]")
                print("S                             S    | |                        | |            ^This is for INTEGER.                   ]")
                print("K                             K    | |                        | |  ~Num2 = float(input(''Enter Number :''))          ]")
                print("*                             *    | |                        | |            ^This is for float(If you need decimal.)]")
                print("*                             *    | |________________________| |  ~ans = input(''Are you okay?(Y/N):'')             ]")
                print("A S K * * A S K * * A S K * * A    |____________________________|   is_me = ans == ''Y''                             ]")
                print("S                                                               |   print(''Status'',is_me)                          ]")
                print("K              ^                                   ^            |            ^This for Boolean using condition.      ]")
                print("*      This is your program.               This is your output. |                                                    ]")
                print("*---------------------------------------------------------------|====================================================]")
                print("*TAKE NOTE : You can Combine them together. That would be so cool!                                                   ]")
                print("---------------------------------------------------------------------------------------------------------------------]\n")
                print("_-" * 68)
                print(",---,---,---,---,---,---,---,---,---,---,---,---,---,-------,   L E T' S   T R Y   T O   ")
                print(
                    "|1/2| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 | + | ' | <-    |           M A K E   Y O U R   I N P U T   ")
                print(
                    "|---'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-----|    S Y S T E M !   U S E   T H E   F O L L O W I N G")
                print("| ->| | Q | W | E | R | T | Y | U | I | O | P | ] | ^ |     |                 DATA TYPES.")
                print("|-----',--',--',--',--',--',--',--',--',--',--',--',--'|    |")
                print("| Caps | A | S | D | F | G | H | J | K | L |   | [ | * |    |   STRING   >--------")
                print("|----,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'---'----|   INTEGERS >--------")
                print("|    | < | Z | X | C | V | B | N | M | , | . | - |          |   BOOLEAN  >--------")
                print("|----'-,-',--'--,'---'---'---'---'---'---'-,-'---',--,------|   FLOAT    >--------")
                print("| ctrl |  | alt |                          |Kevin |  | ctrl |")
                print("'------'  '-----'--------------------------'------'  '------'")
                print("_-" * 68)
                print("First to make is String. Then Int. Then float. Then Boolean(Use Conditional). Each Line, One after Another.")
                print("Use this as example :\n")
                print("''Enter Name : '' For String.\n")
                print("''Enter Number : '' For Int and float.\n")
                print("''Are you retired?(Y/N) : '' For Boolean.\n")
                print("  retired = ask == ''Y''\n")
                print("VARIABLES : [Name]STRING,[Num]INTEGER,[Num]FLOAT,[ask]BOOLEAN.")
                print("Use ('') as quotation mark.")
                print("_-" * 68)
                print("__________________________________________________________________________________________________________")
                ans1 = input("1|")
                print(" |")
                print(" |")
                print(" |")
                print(" |")
                print(" |")
                ans2 = input("2|")
                print(" |")
                print(" |")
                print(" |")
                print(" |")
                print(" |")
                ans3 = input("3|")
                print(" |")
                ans4 = input("4|")
                ans5 = input("5|")
                print(" |")
                print(" |")
                print(" |")
                print(" |")
                print(" |")
                print(" |________________________________________________________________________________________________________\n")
                if ans1 == "Name = input(''Enter Name : '')":
                    print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - ")
                    print("     ___________________________________________")
                    print("()==(   LINE ONE (STRING)                      (@==()")
                    print("     '_________________________________________'|")
                    print("       |  You got The correct Answer.           |")
                    print("       |  Name = input(''Enter Name : '')       |")
                    print("     __)________________________________________|")
                    print("()==(                                          (@==()")
                    print("     '------------------------------------------'")
                    print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - ")
                else:
                    print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - ")
                    print("     ___________________________________________")
                    print("()==(  LINE ONE (STRING)                       (@==()")
                    print("     '_________________________________________'|")
                    print("       |  Wrong Answer Look down below.         |")
                    print("       |  Name = input(''Enter Name : '')       |")
                    print("     __)________________________________________|")
                    print("()==(                                          (@==()")
                    print("     '------------------------------------------'")
                    print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - ")
                if ans2 == "Num = int(input(''Enter Number : ''))":

                    print("                                                   ___________________________________________")
                    print("                                              ()==(  LINE TWO (INTEGER)                      (@==()")
                    print("                                                   '_________________________________________'|")
                    print("                                                     |  You got The correct Answer.           |")
                    print("                                                     |  Num = int(input(''Enter Number : '')) |")
                    print("                                                   __)________________________________________|")
                    print("                                              ()==(                                          (@==()")
                    print("                                                   '------------------------------------------'")
                    print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - ")
                else:
                    print("                                                   ___________________________________________")
                    print("                                              ()==(  LINE TWO (INTEGER)                      (@==()")
                    print("                                                   '_________________________________________'|")
                    print("                                                     |  Wrong Answer. Look down below.        |")
                    print("                                                     |  Num = int(input(''Enter Number : '')) |")
                    print("                                                   __)________________________________________|")
                    print("                                              ()==(                                          (@==()")
                    print("                                                   '------------------------------------------'")
                    print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - ")
                if ans3 == "Num = float(input(''Enter Number : ''))":
                    print("     ____________________________________________")
                    print("()==(  LINE THREE (FLOAT)                       (@==()")
                    print("     '__________________________________________'|")
                    print("       |  You got The correct Answer.            |")
                    print("       |  Num = float(input(''Enter Number : ''))|")
                    print("     __)_________________________________________|")
                    print("()==(                                           (@==()")
                    print("     '-------------------------------------------'")
                    print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - ")
                else:
                    print("     ____________________________________________")
                    print("()==(  LINE THREE (FLOAT)                       (@==()")
                    print("     '__________________________________________'|")
                    print("       |  Wrong Answer Look down below.          |")
                    print("       |  Num = float(input(''Enter Number : ''))|")
                    print("     __)_________________________________________|")
                    print("()==(                                           (@==()")
                    print("     '-------------------------------------------'")
                    print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - ")
                if ans4 == "ask = input(''Are you retired?(Y/N) : '')" and ans5 == "retired = ask == ''Y''":
                    print("                                                    _______________________________________________")
                    print("                                               ()==(   LINE FOUR (BOOLEAN)                        (@==()")
                    print("                                                    '_____________________________________________'|")
                    print("                                                      |  You got The correct Answer.               |")
                    print("                                                      |  ask = input(''Are you retired?(Y/N) : ''))|")
                    print("                                                      |  retired = ask == ''Y''                    |")
                    print("                                                    __)____________________________________________|")
                    print("                                               ()==(                                              (@==()")
                    print("                                                    '----------------------------------------------'")
                    print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - ")
                else:
                    print("                                                    _______________________________________________")
                    print("                                               ()==(   LINE FOUR (BOOLEAN)                        (@==()")
                    print("                                                    '_____________________________________________'|")
                    print("                                                      |  Wrong Answer. Look down below.            |")
                    print("                                                      |  ask = input(''Are you retired?(Y/N) : ''))|")
                    print("                                                      |  retired = ask == ''Y''                    |")
                    print("                                                    __)____________________________________________|")
                    print("                                               ()==(                                              (@==()")
                    print("                                                    '----------------------------------------------'")
                    print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - ")
                    print("_-" * 68)
                    print("." * 136)
                    print("_-" * 68)
                    print("\n                          T H E     E N D    O F    C H A P T E R    F O U R!!! \n")
                    print("_-" * 68)
                    print("." * 136)
                    print("_-" * 68)
            elif choice == "5":
                print("__________________________________________________________________________________________")
                print("|                                                                                        |")
                print("|      C H A P T E R   5    C O N D I T I O N A L    S T A T E M E N T                   |")
                print("|________________________________________________________________________________________|\n")
                print("                                 ,     |    |      ,                                         ")
                print("                                / |    )|__|(     / |     What is CONDITIONAL STATEMENT?")
                print("                               /   |  (_|  |_)   /   |    ")
                print("                          ____/_____|__|@  @|___/_____|____  It allows the program to make decision, whether it's ")
                print("                         |              |VV|               |   TRUE or FALSE.")
                print("                         |        IF, ELSE IF, ELSE        |     ")
                print("                         |_________________________________|           if - Start to make decision.")
                print("                          |    /| |      ||       | /|    |            elif - Something else you want.")
                print("                          |  /   V        ))       V   |  |            else - when you don't have decision to make.")
                print("                          |/     `       //        '     || ")
                print("                          `              V                '\n")
                print("_-" * 68)
                print("RELATIONAL OPERATORS. If you compare two values that you used the result is always TRUE or FAlSE\n")
                print("__________________________________________________________________________________________")
                print("| OPERATORS |      DEFINITION          |           EXAMPLE           |        RESULTS     |")
                print("|___________|__________________________|_____________________________|____________________|")
                print("|   >=         Greater than or equal to      20 >= 39                        TRUE         |")
                print("|                                                                                         |")
                print("|_________________________________________________________________________________________|")
                print("|  <=          Less than or equal to         59 <= 59                        TRUE         |")
                print("|                                                                                         |")
                print("|_________________________________________________________________________________________|")
                print("|  !=          Not equal                     8 != 5                          TRUE         |")
                print("|                                                                                         |")
                print("|_________________________________________________________________________________________|")
                print("|  ==          Equal to                      6 == 6                          TRUE         |")
                print("|                                                                                         |")
                print("|_________________________________________________________________________________________|")
                print("|  >           Greater Than                  10 > 22                         FALSE        |")
                print("|                                                                                         |")
                print("|_________________________________________________________________________________________|")
                print("|  <            Less than                    88 < 100                        TRUE         |")
                print("|                                                                                         |")
                print("|_________________________________________________________________________________________|\n")
                print("```````````````````````````````````````````````````````````````````````````````````````````")
                enter = input("Enter [if] to see an example conditional : ").upper()
                if enter == "IF":
                    print(".---------------------------------. ")
                    print("|  .---------------------------.  | ")
                    print("|[]|  Life = 3                 |[]| <<< This is an example of using conditional statement.                ")
                    print("|  |  if Life >= 2 :           |  |        - If you want to make other decision jus put,")
                    print("|  |       print(''Win'')      |  |          [elif]. You can use this whanever you want. ")
                    print("|  |  elif Life > 1 :          |  |")
                    print("|  |       print(''Nice'')     |  |        - Make sure your conditional is intended :]")
                    print("|  |  else :                   |  |        - Use [else] when you want a FALSE condition")
                    print("|  |      print(''Bruh'')      |  |        - Don't forget to put this [:] with your condition.")
                    print("|  |                           |  |")
                    print("|  `---------------------------'  |===================================================================")
                    print("|      __________________ _____   |   N E S T E D   C O N D I T I O N A L ")
                    print("|     |   ___            |     |  |   It is the condition inside another condition.")
                    print("|     |  |   |           |     |  |                 | ")
                    print("|     |  |   |           |     |  |                 |")
                    print("|     |  |   |           |     |  |                 |")
                    print("|     |  |___|           |     |  |                 |")
                    print("(_____|__________________|_____|__|                 |")
                    print("                                                    +")
                    print("          __________________________________________|_______________________________")
                    print("          |```````````````````N E S T E D  C O N D I T I O N A L```````````````````|")
                    print("          |________________________________________________________________________|")
                    print("          |  stu = input(''Enter Mythic Glory(MG) :'')                             |")
                    print("          |  rank = int(input(''Star points :'')                                   |")
                    print("          |  if stu == ''MG'' :                                                    |")
                    print("          |          if rank >= 100 :                                              |")
                    print("          |               print(''Palong palo'')                                   |")
                    print("          |          else :                                                        |")
                    print("          |               print(''Low rank'')                                      |")
                    print("          |  else :                                                                |")
                    print("          |        print(''Lagay monga MG kahit di nag e ml'')                     |")
                    print("          |________________________________________________________________________|\n")
                    print("......................................................................................................")
                    print("Now Let's Try what you learned About this lesson. Just write TRUE OR FALSE. Think before you answer!")
                    print("Goodluck!!\n")
                    score = 0
                    print("+-------------+")
                    print("| 1. 25 >= 15 |")
                    print("+-------------+")
                    answer = input("Your answer: ").upper()

                    if answer == "TRUE":
                        print("Correct!")
                        score += 1
                    elif answer == "FALSE":
                        print("Wrong! The correct answer is TRUE.")
                    else:
                        print("I said TRUE or FALSE!")

                    print("------------------------------------------")
                    print("+-------------+")
                    print("| 2. 30 <= 20 |")
                    print("+-------------+")
                    answer = input("Your answer: ").upper()

                    if answer == "FALSE":
                        print("Correct!")
                        score += 1
                    elif answer == "TRUE":
                        print("Wrong! The correct answer is FALSE.")
                    else:
                        print("I said TRUE or FALSE!")

                    print("------------------------------------------")
                    print("+-------------+")
                    print("| 3. 10 != 5  |")
                    print("+-------------+")
                    answer = input("Your answer: ").upper()

                    if answer == "TRUE":
                        print("Correct!")
                        score += 1
                    elif answer == "FALSE":
                        print("Wrong! The correct answer is TRUE.")
                    else:
                        print("I said TRUE or FALSE!")

                    print("------------------------------------------")
                    print("+-------------+")
                    print("| 4. 15 == 20 |")
                    print("+-------------+")
                    answer = input("Your answer: ").upper()

                    if answer == "FALSE":
                        print("Correct!")
                        score += 1
                    elif answer == "TRUE":
                        print("Wrong! The correct answer is FALSE.")
                    else:
                        print("I said TRUE or FALSE!")

                    print("------------------------------------------")
                    print("+-------------+")
                    print("| 5. 50 > 25  |")
                    print("+-------------+")
                    answer = input("Your answer: ").upper()

                    if answer == "TRUE":
                        print("Correct!")
                        score += 1
                    elif answer == "FALSE":
                        print("Wrong! The correct answer is TRUE.")
                    else:
                        print("I said TRUE or FALSE!")

                    print("------------------------------------------")
                    print("+-------------+")
                    print("| 6. 10 < 5   |")
                    print("+-------------+")
                    answer = input("Your answer: ").upper()

                    if answer == "FALSE":
                        print("Correct!")
                        score += 1
                    elif answer == "TRUE":
                        print("Wrong! The correct answer is FALSE.")
                    else:
                        print("I said TRUE or FALSE!")

                    print("------------------------------------------")
                    print("+-------------+")
                    print("| 7. 40 >= 40 |")
                    print("+-------------+")
                    answer = input("Your answer: ").upper()

                    if answer == "TRUE":
                        print("Correct!")
                        score += 1
                    elif answer == "FALSE":
                        print("Wrong! The correct answer is TRUE.")
                    else:
                        print("I said TRUE or FALSE!")

                    print("------------------------------------------")
                    print("+-------------+")
                    print("| 8. 15 <= 25 |")
                    print("+-------------+")
                    answer = input("Your answer: ").upper()

                    if answer == "FALSE":
                        print("Correct!")
                        score += 1
                    elif answer == "TRUE":
                        print("Wrong! The correct answer is FALSE.")
                    else:
                        print("I said TRUE or FALSE!")

                    print("------------------------------------------")
                    print("+-------------+")
                    print("| 9. 8 != 8   |")
                    print("+-------------+")
                    answer = input("Your answer: ").upper()

                    if answer == "FALSE":
                        print("Correct!")
                        score += 1
                    elif answer == "TRUE":
                        print("Wrong! The correct answer is FALSE.")
                    else:
                        print("I said TRUE or FALSE!")

                    print("------------------------------------------")
                    print("+----------------+")
                    print("| 10. 100 == 100 |")
                    print("+----------------+")
                    answer = input("Your answer: ").upper()

                    if answer == "TRUE":
                        print("Correct!")
                        score += 1
                    elif answer == "FALSE":
                        print("Wrong! The correct answer is TRUE.")
                    else:
                        print("I said TRUE or FALSE!")

                    print("   _.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._")
                    print(".-'---      - ---     --     ---   -----   - --       ----  ----   -     ---`-.")
                    print(" )  You got", score, "/ 10!!                                                  (")
                    print("(                                                                             )")
                    print(" )  Whatever the Result is, Don't give up.                                   (")
                    print("(                                                                             )")
                    print("_______________________________________________________________________________")
                    if score >= 8:
                        print("Well Done! You got that huge score! Happy seeing you improved.")
                        print("_______________________________________________________________________________")
                    elif score >= 5:
                        print("Good job! Keep practicing. You can do it.")
                        print("_______________________________________________________________________________")
                    else:
                        print("You failed. Study the lesson again and don't give up!")
                        print("_______________________________________________________________________________")
                    print(" )                                                                            (")
                    print("(          T H E                                                               )")
                    print(" )                   E N D                                                    (")
                    print("(                             O F                                              )")
                    print(" )                                   C H A P T E R                            (")
                    print("(                                                    F I V E                   )")
                    print(" )                                                                           (")
                    print("(___       _       _       _       _       _       _       _       _       ___)")
                    print("    (__  _) ( __ _) (__  _) (__ _ ) `-._.-' ( _ __) (_  __) (_ __ ) (_  __)")
                    print("    ( _ __) (_  __) (__ __) `-._.-'         `-._.-' (__ __) (__  _) (__ _ )")
                    print("    (__  _) (_ _ _) `-._.-'                         `-._.-' (_ _ _) (_  __)")
                    print("    (_ ___) `-._.-'                                         `-._.-' (___ _)")
                    print("    `-._.-'                                                         `-._.-'\n")

            elif choice == "6":
                print("__________________________________________________________________________________________")
                print("|                                                                                        |")
                print("|      C H A P T E R   6    L O G I C A L    O P E R A T O R S                           |")
                print("|________________________________________________________________________________________|\n")
                print("What is LOGICAL OPERATORS?")
                print(
                    "Logical Operators are always used with conditional statement. They are use to reversed condition or combine.\n")
                print("__________________________________________________________________________________________")
                print("|                                                                                        |")
                print("(   L O G I C A L   O P E R A T O R S                                                    )")
                print("(________________________________________________________________________________________)")
                print("|                                                                                        |")
                print("|  and - Both Condition is TRUE                                                          |")
                print("|........................................................................................|")
                print("|                                                                                        |")
                print("|  or - One of the condition must be TRUE                                                |")
                print("|........................................................................................|")
                print("|                                                                                        |")
                print("|  not - Reverse the  result. TRUE = FALSE and FALSE = TRUE                              |")
                print("|........................................................................................|")
                print("|                                                                                        |")
                print("|  Example :                                                                             |")
                print("|                                                                                        |")
                print("|   age = 18                                     Take note : AND is all true.            |")
                print("|   got_vip = True                                           OR got atleast one true.    |")
                print("|                                                            NOT reverse the result.     |")
                print("|   if age >= 18 and got_vip :                                                           |")
                print("|      print(''Enjoy the party'')                                                        |")
                print("|   else :                                                                               |")
                print("|      print(''not allowed'')                                                            |")
                print("|                                                                                        |")
                print("|________________________________________________________________________________________|")
                print("|                                                                                        |")
                print("|   Example of NOT :                                                                     |")
                print("|                                                                                        |")
                print("|     sunny = True                                                                       |")
                print("|                                                                                        |")
                print("|     if not sunny :                                                                     |")
                print("|        print(''you can't play'')                                                       |")
                print("|     else :                                                                             |")
                print("|        print(''you can play'')                                                         |")
                print("|                                                                                        |")
                print("|________________________________________________________________________________________|\n")
                print("-+" * 60)
                print("█▓▒░ LET'S PLAY A GAME : ) ░▒▓█")
                print("░ ▒ ▓ █ ░ ▒ ▓ █ ░ ▒ ▓ █ ░ ▒▓█░▒▓█░▒▓█░▒▓█")
                print("       L O G I C A L   O P E R A T O R")
                print("░ ▒ ▓ █ ░ ▒ ▓ █ ░ ▒ ▓ █ ░ ▒▓█░▒▓█░▒▓█░▒▓█")
                print("-+" * 60)

                print("==================================================================")
                print("|             LOGICAL OPERATOR CHALLENGE                         |")
                print("|================================================================|")
                print("|Welcome to the Logical Operator Challenge!                      |")
                print("|Put the number [1] or [2] to get the correct answer.            |")
                print("|You need to get at least 3 correct answers to pass.             |")
                print("|================================================================|")

                score = 0
                print("\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
                print("QUESTION 1: AND OPERATOR      ")
                print("Both conditions must be TRUE. ")
                print("x = True                      ")
                print("y = False                     ")
                print("What is the result of x and y?")
                print("[1] True                      ")
                print("[2] False                     ")
                print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")

                answer = input("Enter your answer: ")

                if answer == "2":
                    print("CORRECT! Both conditions must be TRUE.")
                    score = score + 1
                else:
                    print("WRONG! The answer is FALSE.")
                print("\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
                print("QUESTION 2: OR OPERATOR")
                print("At least one condition must be TRUE.")
                print("x = True")
                print("y = False")
                print("What is the result of x or y?")
                print("[1] True")
                print("[2] False")
                print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
                answer = input("Enter your answer: ")

                if answer == "1":
                    print("CORRECT! One condition is TRUE.")
                    score = score + 1
                else:
                    print("WRONG! The answer is TRUE.")
                print("\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
                print("QUESTION 3: NOT OPERATOR")
                print("The NOT operator reverses the condition.")
                print("x = True")
                print("What is the result of not x?")
                print("[1] True")
                print("[2] False")
                print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
                answer = input("Enter your answer: ")

                if answer == "2":
                    print("CORRECT! NOT reverses TRUE into FALSE.")
                    score = score + 1
                else:
                    print("WRONG! The answer is FALSE.")
                print("\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
                print("QUESTION 4: AND OPERATOR")
                print("a = True")
                print("b = True")
                print("What is the result of a and b?")
                print("[1] True")
                print("[2] False")
                print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")

                answer = input("Enter your answer: ")

                if answer == "1":
                    print("CORRECT! Both conditions are TRUE.")
                    score = score + 1
                else:
                    print("WRONG! The answer is TRUE.")
                print("\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
                print("QUESTION 5: OR OPERATOR")
                print("a = False")
                print("b = False")
                print("What is the result of a or b?")
                print("[1] True")
                print("[2] False")
                print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")

                answer = input("Enter your answer: ")

                if answer == "2":
                    print("CORRECT! Both conditions are FALSE.")
                    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
                    score = score + 1
                else:
                    print("WRONG! The answer is FALSE.")
                    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
                print("==================================================================")
                print("|             PART II : MULTIPLE  CHOICE                         |")
                print("|================================================================|")
                print("|Read Carefully and put the following answer :}                  |")
                print("|================================================================|\n")
                print("1. Which operator requires BOTH conditions to be TRUE?")
                print("[A] and")
                print("[B] or")
                print("[C] not")

                answer = input("Your answer: ").lower()

                if answer == "a":
                    print("Correct!\n")
                    score += 1
                elif answer == "b" or answer == "c":
                    print("Incorrect! The correct answer is A. and\n")
                else:
                    print("Invalid answer!\n")

                print("2. Which operator requires at least ONE condition to be TRUE?")
                print("[A] and")
                print("[B] or")
                print("[C] not")

                answer = input("Your answer: ").lower()

                if answer == "b":
                    print("Correct!\n")
                    score += 1
                elif answer == "a" or answer == "c":
                    print("Incorrect! The correct answer is B. or\n")
                else:
                    print("Invalid answer!\n")

                print("3. What does the NOT operator do?")
                print("[A] Combines conditions")
                print("[B] Repeats conditions")
                print("[C] Reverses the result")

                answer = input("Your answer: ").lower()

                if answer == "c":
                    print("Correct!\n")
                    score += 1
                elif answer == "a" or answer == "b":
                    print("Incorrect! The correct answer is C. Reverses the result\n")
                else:
                    print("Invalid answer!\n")

                print("4. What is the result of True and False?")
                print("[A] True")
                print("[B] False")
                print("[C] None")

                answer = input("Your answer: ").lower()

                if answer == "b":
                    print("Correct!\n")
                    score += 1
                elif answer == "a" or answer == "c":
                    print("Incorrect! The correct answer is B. False\n")
                else:
                    print("Invalid answer!\n")

                print("5. What is the result of False or True?")
                print("[A] True")
                print("[B] False")
                print("[C] None")

                answer = input("Your answer: ").lower()

                if answer == "a":
                    print("Correct!\n")
                    score += 1
                elif answer == "b" or answer == "c":
                    print("Incorrect! The correct answer is A. True\n")
                else:
                    print("Invalid answer!\n")

                print("6. What is the result of not True?")
                print("[A] True")
                print("[B] False")
                print("[C] None")

                answer = input("Your answer: ").lower()

                if answer == "b":
                    print("Correct!\n")
                    score += 1
                elif answer == "a" or answer == "c":
                    print("Incorrect! The correct answer is B. False\n")
                else:
                    print("Invalid answer!\n")

                print("7. Which expression evaluates to TRUE?")
                print("[A] False and True")
                print("[B] True and True")
                print("[C] False or False")

                answer = input("Your answer: ").lower()

                if answer == "b":
                    print("Correct!\n")
                    score += 1
                elif answer == "a" or answer == "c":
                    print("Incorrect! The correct answer is B. True and True\n")
                else:
                    print("Invalid answer!\n")

                print("8. The AND operator needs both conditions to be TRUE.")
                print("[A] True")
                print("[B] False")

                answer = input("Your answer: ").lower()

                if answer == "a":
                    print("Correct!\n")
                    score += 1
                elif answer == "b":
                    print("Incorrect! The correct answer is A. True\n")
                else:
                    print("Invalid answer!\n")
                print("9. The NOT operator combines two conditions.")
                print("[A] True")
                print("[B] False")

                answer = input("Your answer: ").lower()

                if answer == "b":
                    print("Correct!\n")
                    score += 1
                elif answer == "a":
                    print("Incorrect! The correct answer is B. False\n")
                else:
                    print("Invalid answer!\n")

                print("10. What will be the output?")
                print("sunny = True")
                print("if not sunny:")
                print("    print('Cannot play')")
                print("else:")
                print("    print('Can play')")

                answer = input(" [A] Cannot play\n [B] Can play\nYour answer: ").lower()

                if answer == "b":
                    print("Correct!\n")
                    score += 1
                elif answer == "a":
                    print("Incorrect! The correct answer is B. Can play\n")
                else:
                    print("Invalid answer!\n")

                print("==================================================")
                print("                 QUIZ RESULT")
                print("==================================================")
                print("| Your Score:", score, "/ 15                     ")

                if score >= 10:
                    print("~CONGRATULATIONS! YOU PASSED THE GAME!")
                    if score == 15:
                        print("~PERFECT SCORE! EXCELLENT WORK!")
                    else:
                        print("~GOOD JOB! KEEP LEARNING!")
                else:
                    print("~SORRY! YOU FAILED.")
                    print("~PLEASE REVIEW THE LESSON AND TRY AGAIN.")

                print("==================================================")
                print("      E N D   O F   C H A P T E R   S I X         ")
                print("==================================================")

            elif choice == "7":

                print("__________________________________________________________________________________________")
                print("|                                                                                        |")
                print("|                  C H A P T E R   7   P Y T H O N   L O O P S                           |")
                print("|________________________________________________________________________________________|")
                print("|                                                                                        |")
                print("|  What are LOOPS?                                                                       |")
                print("|                                                                                        |")
                print("|  Loops are used to repeat a block of code multiple times. Instead of writing the       |")
                print("|  same code again and again, we can use loops to make our program shorter and easier.   |")
                print("|________________________________________________________________________________________|\n")

                print("__________________________________________________________________________________________")
                print("|                                                                                        |")
                print("|                                 W H I L E   L O O P                                    |")
                print("|________________________________________________________________________________________|")
                print("|                                                                                        |")
                print("|  What is WHILE LOOP?                                                                    |")
                print("|                                                                                        |")
                print("|  A WHILE LOOP repeats a block of code as long as the condition is TRUE.                |")
                print("|                                                                                        |")
                print("|  SIMPLE MEANING: Repeat while the condition is TRUE.                                   |")
                print("|________________________________________________________________________________________|\n")

                print("STEP 1: BASIC SYNTAX")
                print("------------------------------------------------------------------------------------------")
                print("while condition:")
                print("    statement")
                print("------------------------------------------------------------------------------------------")
                print("while     - Starts the loop.")
                print("condition - Checks if the condition is TRUE or FALSE.")
                print("statement - The code that will repeat.\n")

                print("STEP 2: EXAMPLE")
                print("------------------------------------------------------------------------------------------")

                print("number = 1")
                print("")
                print("while number <= 5:")
                print("    print(number)")
                print("    number += 1")

                print("------------------------------------------------------------------------------------------")
                print("OUTPUT:")

                number = 1

                while number <= 5:
                    print(number)
                    number += 1

                print("------------------------------------------------------------------------------------------\n")

                print("STEP 3: HOW DOES IT WORK?")
                print("------------------------------------------------------------------------------------------")
                print("1. Set the starting number: number = 1")
                print("2. Check if number <= 5.")
                print("3. If TRUE, print the number.")
                print("4. Increase the number by 1 using number += 1.")
                print("5. Repeat until the condition becomes FALSE.")
                print("------------------------------------------------------------------------------------------\n")

                print("IMPORTANT REMINDER:")
                print("Always make sure that the condition will eventually become FALSE.")
                print("Otherwise, your program may create an INFINITE LOOP.\n")

                print("__________________________________________________________________________________________")
                print("|                                                                                        |")
                print("|                           F O R   L O O P                                              |")
                print("|________________________________________________________________________________________|")
                print("|                                                                                        |")
                print("|  What is FOR LOOP?                                                                      |")
                print("|                                                                                        |")
                print("|  A FOR LOOP repeats a block of code for each item in a sequence or for a specific     |")
                print("|  number of repetitions.                                                                |")
                print("|                                                                                        |")
                print("|  SIMPLE MEANING: Repeat for every item or number in a sequence.                        |")
                print("|________________________________________________________________________________________|\n")

                print("STEP 1: BASIC SYNTAX")
                print("------------------------------------------------------------------------------------------")
                print("for variable in sequence:")
                print("    statement")
                print("------------------------------------------------------------------------------------------")
                print("for      - Starts the loop.")
                print("variable - Stores the current item.")
                print("in       - Gets an item from the sequence.")
                print("sequence - The collection or range of items.")
                print("statement- The code that will repeat.\n")

                print("STEP 2: EXAMPLE")
                print("------------------------------------------------------------------------------------------")

                print("for number in range(1, 6):")
                print("    print(number)")

                print("------------------------------------------------------------------------------------------")
                print("OUTPUT:")

                for number in range(1, 6):
                    print(number)

                print("------------------------------------------------------------------------------------------\n")

                print("STEP 3: UNDERSTANDING RANGE()")
                print("------------------------------------------------------------------------------------------")
                print("range(1, 6) generates numbers from 1 up to 5.")
                print("The ending number is NOT included.")
                print("------------------------------------------------------------------------------------------\n")

                print("ANOTHER EXAMPLE:")
                print("------------------------------------------------------------------------------------------")

                print('for name in ["Kevin", "John", "Mark"]:')
                print('    print("Hello", name)')

                print("------------------------------------------------------------------------------------------")
                print("OUTPUT:")

                for name in ["Kevin", "John", "Mark"]:
                    print("Hello", name)

                print("------------------------------------------------------------------------------------------\n")

                print("__________________________________________________________________________________________")
                print("|                                                                                        |")
                print("|                 D I F F E R E N C E   O F   L O O P S                                  |")
                print("|________________________________________________________________________________________|")
                print("|                                                                                        |")
                print("|  WHILE LOOP: Repeats as long as a condition is TRUE.                                   |")
                print("|                                                                                        |")
                print("|  FOR LOOP  : Repeats through a sequence of items.                                      |")
                print("|                                                                                        |")
                print("|  WHILE LOOP: Useful when the number of repetitions is not known.                       |")
                print("|                                                                                        |")
                print("|  FOR LOOP  : Useful when the number of repetitions or items is known.                  |")
                print("|________________________________________________________________________________________|\n")

                print("------------------------------------------------------------------------------------------\n")
                print("__________________________________________________________________________________________")
                print("|                                                                                        |")
                print("|      SINCE I  DIDN'T  PUT DESIGN UNLIKE OTHER CHAPTER  LET ME GIVE YOU A SUMMARY       |")
                print("|________________________________________________________________________________________|")
                print("|                                                                                        |")
                print("|  1. A loop repeats a block of code.                                                    |")
                print("|  2. A WHILE LOOP repeats while its condition is TRUE.                                  |")
                print("|  3. A FOR LOOP repeats through a sequence.                                             |")
                print("|  4. The range() function generates a sequence of numbers.                              |")
                print("|  5. Indentation is important in Python loops.                                          |")
                print("|  6. An INFINITE LOOP happens when a loop never stops.                                  |")
                print("|________________________________________________________________________________________|\n")

                print("__________________________________________________________________________________________")
                print("|                                                                                        |")
                print("|                         C H A P T E R   7   Q U I Z                                    |")
                print("|________________________________________________________________________________________|\n")

                print("INSTRUCTIONS:")
                print("Choose the correct letter.")
                print("You need 4 points out of 5 to PASS.\n")

                score = 0

                print("1. Which loop repeats while a condition is TRUE?")
                print("[A] FOR LOOP")
                print("[B] WHILE LOOP")
                print("[C] IF STATEMENT")

                answer = input("Your answer: ").upper()

                if answer == "b":
                    print("CORRECT!\n")
                    score += 1
                else:
                    print("INCORRECT! The correct answer is B.\n")

                print("2. Which function is commonly used with a FOR LOOP to generate numbers?")
                print("[A] input()")
                print("[B] print()")
                print("[C] range()")

                answer = input("Your answer: ").upper()

                if answer == "c":
                    print("CORRECT!\n")
                    score += 1
                else:
                    print("INCORRECT! The correct answer is C.\n")

                print("3. What is the output of range(1, 4)?")
                print("[A] 1, 2, 3")
                print("[B] 1, 2, 3, 4")
                print("[C] 0, 1, 2, 3")

                answer = input("Your answer: ").upper()

                if answer == "A":
                    print("CORRECT!\n")
                    score += 1
                else:
                    print("INCORRECT! The correct answer is A.\n")

                print("4. What happens when a WHILE LOOP condition becomes FALSE?")
                print("[A] It repeats forever")
                print("[B] The loop stops")
                print("[C] The program restarts")

                answer = input("Your answer: ").upper()

                if answer == "B":
                    print("CORRECT!\n")
                    score += 1
                else:
                    print("INCORRECT! The correct answer is B.\n")

                print("5. Which loop is useful for displaying every name in a list?")
                print("[A] FOR LOOP")
                print("[B] IF STATEMENT")
                print("[C] ELSE STATEMENT")

                answer = input("Your answer: ").upper()

                if answer == "A":
                    print("CORRECT!\n")
                    score += 1
                else:
                    print("INCORRECT! The correct answer is A.\n")

                print("__________________________________________________________________________________________")
                print("|                                                                                        |")
                print("|                              Q U I Z   R E S U L T                                     |")
                print("|________________________________________________________________________________________|")

                print("YOUR SCORE:", score, "/ 5")

                if score >= 4:
                    print("CONGRATULATIONS! YOU PASSED!")
                    if score == 5:
                        print("PERFECT SCORE! EXCELLENT WORK!")
                    else:
                        print("GOOD JOB! KEEP LEARNING!")
                else:
                    print("SORRY! YOU FAILED.")
                    print("PLEASE REVIEW THE LESSON AND TRY AGAIN.")

                print("__________________________________________________________________________________________")
                print("|                         E N D   O F   C H A P T E R   7                                |")
                print("|________________________________________________________________________________________|")

        elif pick == "LSBS":
            print("__________________________________________________________________________________________")
            print("|                                                                                        |")
            print("|      C H A P T E R   1    I N T R O D U C T I O N    T O    P R O G R A M M I N G      |")
            print("|________________________________________________________________________________________|\n")

            print(
                "Do you have any idea what's programming language is? if not, PROGRAMMING LANGUAGE is a special language")
            print("that computers understand and use to perform task.(。•̀ᴗ-)✧\n")
            print(
                "Anyways PYTHON PROGRAMMING is widely used around the world because it was easy to learn, simple and readable.")
            print("It was created by Guido Van Rossum in 1991.\n")
            print("What do you need to start python?\n")
            print("_________________________________________________________________________")
            print("|`````P R O F E S S I O N A L   I D E S / C O D E S   E D I T O R S`````|")
            print("|_______________________________________________________________________|")
            print("| PYCHARM BY JET BRAINS.                                                |")
            print("| VS CODE  (VISUAL STUDIO CODE).                                        |")
            print("| JUPYTER NOTEBOOK/JUPYTER LAB.                                         |")
            print("|_______________________________________________________________________|\n")
            print("That's all for Chapter 1.")
            print("Easy Right? RIGHTTTTTTTTTTTTTTTT?. ＼(ˇ∇ˇ)／\n")
            print("_-" * 68)
            print("                                                         _________________________    ")
            print("                    /|      _____          _____       |   |     |     |    | |  |   ")
            print("     ,-----,       /  |____/__|__|_    ___/__|__|___   |___|_____|_____|____|_|___|  ")
            print("  ,--'---:---`--, /  |  _     |     `| |      |      `| |                    | |    | ")
            print(" ==(o)-----(o)==J    `(o)-------(o)=   `(o)------(o)'   `--(o)(o)--------------(o)--'  ")
            print("`````````````````````````````````````````````````````````````````````````````````````")
            print("_-" * 68)
            print(
                "========== L O A D I N G   P L E A S E   W A I T ==========................................................")
            print("_-" * 68)
            print(" ")
            print("__________________________________________________________________________________________")
            print("|                                                                                        |")
            print("|      C H A P T E R   2    P Y T H O N   B A S I C   S Y N T A X                        |")
            print("|________________________________________________________________________________________|\n")

            print("What is SYNTAX.\n")
            print("SYNTAX refers to the set of rules that tells us how correctly write a program in Python.\n")
            print("=--PYTHON SYNTAX--=")
            print("These things is really important to understand, remember this. Python is case sensitive ")
            print("because python treats upper and lower case differently.Also Python need Indentation or called")
            print("spaces to define blocks of code.  <(-^,^-)=b \n")
            print("For example....\n")
            print("Remember the ('') Imagine this as quotation mark. Thank you for understanding!\n")
            print("__________________________________________________________________________________________")
            print("|  Python Case Sensitive.                                                                |")
            print("|                                                                                        |")
            print("|  (1). name = ''Kevin''               (2). name = ''Kevin''                             |")
            print("|       print(Name)                       print(name)                                    |")
            print("|                                                                                        |")
            print("|    The number  1 is wrong. Number 2 is correct. Why?                                   |")
            print("|    because even though the word NAME is same.                                          |")
            print("|    You can see that, 1 has lowercase variable storage.                                 |")
            print("|    But has upper case with print(Name).                                                |")
            print("|                                                                                        |")
            print("|    Keyword : If it's lower. It's lower. If it's upper. It's upper.                     |")
            print("|                                                                                        |")
            print("|  Indentations(Spaces).                                                                 |")
            print("|                                                                                        |")
            print("|   (1). age = 18                    (2). age = 18                                       |")
            print("|        if age >= 18 :                   if age >= 18 :                                 |")
            print("|          print(''Adult'')               print(''Adult'')                               |")
            print("|                                                                                        |")
            print("|   Number 2 is incorrect because it is not intended or he doesn't have spaces           |")
            print("|   to get inside the block. While number 1 has spaces that's why it's intended.         |")
            print("|                                                                                        |")
            print("|    Keyword: Use spaces and make sure it is align perfectly in your coding              |")
            print("|             to get intended.                                                           |")
            print("|________________________________________________________________________________________|\n")

            print("_-" * 68)
            print("." * 136)
            print("_-" * 68)
            print("                                                      __  _")
            print("      ...........................                     | `/ |     ")
            print("      |                         |                      |__`!   ")
            print("      | PRINTING                |_  ___                / ,' `-.__________________   ")
            print("      |           OUTPUT        | -    ________________'-'|_____                LI`-.   ")
            print("      ...........................                         <____()-=O=O=O=O=O=[]====--)")
            print("                                                              `.___ ,-----,_______...-'")
            print("                                                                   /    .'")
            print("                                                                  /   .'")
            print("                                                                 /  .'  ")
            print("                                                                `-'")
            print("_-" * 68)
            print("." * 136)
            print("_-" * 68)

            print("\nNow let's proceed to PRINTING OUTPUT.\n")
            print("PRINTING OUTPUT - It displayed information through your screen.")
            print("PRINTING NUMBERS - You can put numbers without quotation marks but there's different.See")
            print("the example below.\n")
            print("Remember the ('') Imagine this as quotation mark. Thank you for understanding!\n")
            print("__________________________________________________________________________________________")
            print("|                                                                                        |")
            print("|      (1). print(100)            (2). print(''500'')                                    |")
            print("|           print(25.5)                print(''112'')                                    |")
            print("|                                                                                        |")
            print("|      1 and 2 are both correct, they just have different data types.                    |")
            print("|      The number 1 in line one is called INTEGERS. Line two is called FLOAT.            |")
            print("|      While number 2 is called STRING because it has quotation mark.                    |")
            print("|                                                                                        |")
            print("|                                                                                        |")
            print("|                                                                                        |")
            print("|________________________________________________________________________________________|\n")

            print("() - Open and close Parenthesis Is the reason why program contain to be displayed.")
            print("('') - Quotation mark is the sign for string because without quotation mark,")
            print("you get either error or variables.")
            print("Value - This is (STRING, NUMBER, VARIABLE and ETC.)\n")
            print("_-" * 68)
            print("\n                        ( -_•)ᡕᠵデᡁ᠊╾━--- P Y T H O N   C O M M E N T S.\n")
            print("_-" * 68)
            print(
                "PYTHON COMMENTS is easy to remember just put HASHTAG (#) and that's it you have comment. ദ്ദി ˉ͈̀꒳ˉ͈́ )✧")
            print("Kidding aside. there is two types of comments.")
            print("The first one is SINGLE LINE COMMENT. The second one is MULTI LINE COMMENTS.")
            print("\nRemember the ('') Imagine this as quotation mark. Thank you for understanding!\n")
            print("__________________________________________________________________________")
            print("|``````````````````````P Y T H O N   C O M M E N T S`````````````````````|")
            print("|________________________________________________________________________|")
            print("|                                                                        |")
            print("| SINGLE LINE COMMENTS = (#)                                             |")
            print("|                                                                        |")
            print("| MULTI LINE COMMENTS = ('''''') at top and bottom                       |")
            print("|                                                                        |")
            print("|   Take note: Comments are ignored by python, and used to               |")
            print("|              explain   the code.                                       |")
            print("|________________________________________________________________________|\n")
            print("_-" * 68)
            print("." * 136)
            print("_-" * 68)
            print("\n          _  _")
            print("         ( `   )_")
            print("        (    )    `)")
            print("      (_   (_ .  _) _)")
            print(
                "                                  V A R I A B L E S ,                                                ")
            print("                                         C O N S T A N T S ,                                     ")
            print("           _                                     A N D ")
            print("         -=|`|                         D A T A   T Y P E S.")
            print("     || ____|_|__                                                                 _")
            print("   -=|c`         L`)                                  -----                       (  )")
            print("      `~~~~~| |~~`                                                             ( `  ) . )")
            print("        -==| |                        - - - - -                              (_, _(  ,_)_)")
            print("          '-'                                                                    \n")
            print("_-" * 68)
            print("." * 136)
            print("_-" * 68)
            print("\nWhat is VARIABLES?\n")
            print("VARIABLES is the storage location where you can  keep data in program.\n")
            print("TAKE NOTE :")
            print("Variables can have short name like (a,b,c) or more like (name, total_val, char).")
            print("Variables can't start with numbers. It starts with underscore(_) or letter.")
            print("Like i said before. Python case is sensitive. If you have variable (NAME, name), ")
            print("this two variable are from different data.\n")
            print("\nRemember the ('') Imagine this as quotation mark. Thank you for understanding!\n")
            print("__________________________________________________________________________________________")
            print("| In programming we store data in variables. we put value  to variable,                  |")
            print("| using ASSIGNMENT OPERATOR.                                                             |")
            print("|                                                                                        |")
            print("| For example :                                                                          |")
            print("|                                                                                        |")
            print("|           Character_one = ''Tung Tung Sahur''                                          |")
            print("|                   ^                  ^                                                 |")
            print("|          #This is variable,     #This is Value the data we store in variable.          |")
            print("|           the  name we use to present data.             (It can be text, num and etc). |")
            print("|                                                                                        |")
            print("|           Is that Clear? <(-^,^-)=b                                                    |")
            print("|                                                                                        |")
            print("| Also you can print multiple variables using add(+) or comma(,).                        |")
            print("|                                                                                        |")
            print("| For Example :                                                                          |")
            print("|           a = ''Keep''                                                                 |")
            print("|           b = ''Going''                                                                |")
            print("|           c = ''embrace fear''                                                         |")
            print("|                                                                                        |")
            print("|           print (a + b + c) > output : Keep going embrace fear                         |")
            print("|           print (a, b, c)   > output : Keep going embrace fear                         |")
            print("|________________________________________________________________________________________|\n")
            print("_-" * 68)
            print("\n                        ( -_•)ᡕᠵデᡁ᠊╾━--- D A T A   T Y P E S   I N    P Y T H O N.\n")
            print("_-" * 68)
            print("DATA TYPES - Tells the python on what kind of variable we stored.\n")
            print("Lets focus on :\n")
            print("STRING - More on text inside quotation mark.")
            print("Example : (''Kevin'' , ''Mandal'' , ''Perez'') \n")
            print("INTEGERS(int) - More on Whole numbers. ")
            print("Example : (12, 22 , -18)\n")
            print("float - It has decimal point.")
            print("Example : (20.07, 18.22, -17.2)\n")
            print("bool(boolean) - Represent one of two value it's either TRUE or FALSE.")
            print("Example : (TRUE, FALSE)\n")
            print("This is the example of how it works.")
            print("__________________________________________________________________________________________")
            print("|                                                                                        |")
            print("|    name = ''Kevin''               >  String                                            |")
            print("|    age = 18                       >  Integers                                          |")
            print("|    grade_inpython = 61.30         >  Float                                             |")
            print("|    is_enrolled = False            >  Boolean                                           |")
            print("|                                                                                        |")
            print("|    print(name)                                                                         |")
            print("|    print(age)                                                                          |")
            print("|    print(grade_inpython)                                                               |")
            print("|    print(is_enrolled)                                                                  |")
            print("|                                                                                        |")
            print("|________________________________________________________________________________________|\n")
            print("_-" * 68)
            print("       __|__          ============================================           __|__            ")
            print("--------(_)--------   L O A D I N G    P L E A S E    W A I T.....    --------(_)--------")
            print("  O  O       O  O     ============================================      O  O       O  O            ")
            print("_-" * 68)
            print("T H A T ' S   T H E   E N D  O F   C H A P T E R   T W O ")
            print("_-" * 68)
            print(" ")
            print("___________________________________________________________________________________________________")
            print("|                                                                                                 |")
            print("|      C H A P T E R   3    A R I T H M E T I C   O P E R A T O R   A N D   E X P R E S S I O N   |")
            print(
                "|_________________________________________________________________________________________________|\n")

            print("What is ARITHMETIC OPERATOR?\n")
            print("ARITHMETIC OPERATOR are symbol we use in program to execute mathematical operation. (^_^) ")
            print("__________________________________________________________________________________________")
            print("|                                                                                        |")
            print("(   O P E R A T O R S   D E F I N I T I O N S   A N D   E X A M P L E S                  )")
            print("(________________________________________________________________________________________)")
            print("|                                                                                        |")
            print("|  ADDITION (+)  - Add two value  [1 + 5 = 6]                                            |")
            print("|........................................................................................|")
            print("|                                                                                        |")
            print("|  SUBTRACTION (-)   - Subtracts second value to first value  [10 - 5 = 5]               |")
            print("|........................................................................................|")
            print("|                                                                                        |")
            print("|  MULTIPLICATION (*)   - Multiply two values  [5 * 2 = 10]                              |")
            print("|........................................................................................|")
            print("|                                                                                        |")
            print("|  DIVISION(float) (/)   - Divide two value and return decimal   [5 / 2 = 2.0]           |")
            print("|........................................................................................|")
            print("|                                                                                        |")
            print("|  FLOOR DIVISION (//)   - Divide two value but return whole number  [10 // 2 = 5]       |")
            print("|........................................................................................|")
            print("|                                                                                        |")
            print("|  MODULUS (%)   - Return the remainder of division    [5 % 2 = 1]                       |")
            print("|........................................................................................|\n")
            print("Now if you think of it, What is expression?\n")
            print("EXPRESSION is the combination of values,variables and operator. It is useful everytime.\n")
            print("Let's see the example below.")
            print("__________________________________________________________________________")
            print("|`````````````````E X P R E S S I O N   I N   P Y T H O N````````````````|")
            print("|________________________________________________________________________|")
            print("|                                                                        |")
            print("| K = 12                      Take note: You can use it                  |")
            print("| P = 22                                 as long as you want.            |")
            print("| M = 27                                 But make sure it is right.      |")
            print("|                                                                        |")
            print("| tots = K + P + M                                                       |")
            print("| print(''Your total is'', tots)                                         |")
            print("|________________________________________________________________________|")
            print("|                                                                        |")
            print("| Output : Your total is 61                                              |")
            print("|........................................................................|\n")
            print("Did you know PEMDAS? |_(^_^)")
            print("PEMDAS is like combining all operators.\n")
            print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
            print("[________________________________________________________________________]")
            print("| P  for PARENTHESIS [()]   FIRST                                        |")
            print("| E  for EXPONENTS   [**]   SECOND                                       |")
            print("| M  for MULTIPLY    [*]    THIRD                                        |")
            print("| D  for DIVISION    [/]    FOURTH                                       |")
            print("| A  for ADDITION    [+]    FIFTH                                        |")
            print("| S  for SUBTRACTION [-]    SIXTH                                        |")
            print("|                                                                        |")
            print("|  Take Note: Use this by order! =(>_<)=                                 |")
            print("|                                                                        |")
            print("|                                                                        |")
            print("|........................................................................|\n")
            print("_-" * 68)
            print("________________________________________________________________________________________________")
            print("|                                                                                              |")
            print("|      C H A P T E R   4    B A S I C   I N P U T   A N D   O U T P U T   I N  P Y T H O N     |")
            print("|______________________________________________________________________________________________|\n")
            print("What is INPUT?\n")
            print("This is where you want to ask something and respond.\n")
            print("Using INPUT you can able to type inside your Output. ")
            print("For example :\n")
            print("Remember the ('') Imagine this as quotation mark. Thank you for understanding!\n")
            print("                                    ____________________________")
            print("A S K * * A S K * * A S K * * A    |  ________________________  |")
            print(
                "S                             S    | |                        | |====================================================]")
            print(
                "K                             K    | |   Name : Kevin         | |  < You can put any names you want. But not number. ]")
            print(
                "*  name = input(''Name :'')   *    | |   Name is Kevin        | |  < This is how it works.                           ] ")
            print(
                "*  print(''Name is'', Name)   *    | |                        | |  < This is STRING                                  ]")
            print(
                "A                             A    | |                        | |  ~Num1 = int(input(''Enter Number :''))            ]")
            print(
                "S                             S    | |                        | |            ^This is for INTEGER.                   ]")
            print(
                "K                             K    | |                        | |  ~Num2 = float(input(''Enter Number :''))          ]")
            print(
                "*                             *    | |                        | |            ^This is for float(If you need decimal.)]")
            print(
                "*                             *    | |________________________| |  ~ans = input(''Are you okay?(Y/N):'')             ]")
            print(
                "A S K * * A S K * * A S K * * A    |____________________________|   is_me = ans == ''Y''                             ]")
            print(
                "S                                                               |   print(''Status'',is_me)                          ]")
            print(
                "K              ^                                   ^            |            ^This for Boolean using condition.      ]")
            print(
                "*      This is your program.               This is your output. |                                                    ]")
            print(
                "*---------------------------------------------------------------|====================================================]")
            print(
                "*TAKE NOTE : You can Combine them together. That would be so cool!                                                   ]")
            print(
                "---------------------------------------------------------------------------------------------------------------------]\n")
            print("_-" * 68)
            print(" ")
            print("__________________________________________________________________________________________")
            print("|                                                                                        |")
            print("|      C H A P T E R   5    C O N D I T I O N A L    S T A T E M E N T                   |")
            print("|________________________________________________________________________________________|\n")
            print("                                 ,     |    |      ,                                         ")
            print("                                / |    )|__|(     / |     What is CONDITIONAL STATEMENT?")
            print("                               /   |  (_|  |_)   /   |    ")
            print(
                "                          ____/_____|__|@  @|___/_____|____  It allows the program to make decision, whether it's ")
            print("                         |              |VV|               |   TRUE or FALSE.")
            print("                         |        IF, ELSE IF, ELSE        |     ")
            print("                         |_________________________________|           if - Start to make decision.")
            print(
                "                          |    /| |      ||       | /|    |            elif - Something else you want.")
            print(
                "                          |  /   V        ))       V   |  |            else - when you don't have decision to make.")
            print("                          |/     `       //        '     || ")
            print("                          `              V                '\n")
            print("_-" * 68)
            print("RELATIONAL OPERATORS. If you compare two values that you used the result is always TRUE or FAlSE\n")
            print("__________________________________________________________________________________________")
            print("| OPERATORS |      DEFINITION          |           EXAMPLE           |        RESULTS     |")
            print("|___________|__________________________|_____________________________|____________________|")
            print("|   >=         Greater than or equal to      20 >= 39                        TRUE         |")
            print("|                                                                                         |")
            print("|_________________________________________________________________________________________|")
            print("|  <=          Less than or equal to         59 <= 59                        TRUE         |")
            print("|                                                                                         |")
            print("|_________________________________________________________________________________________|")
            print("|  !=          Not equal                     8 != 5                          TRUE         |")
            print("|                                                                                         |")
            print("|_________________________________________________________________________________________|")
            print("|  ==          Equal to                      6 == 6                          TRUE         |")
            print("|                                                                                         |")
            print("|_________________________________________________________________________________________|")
            print("|  >           Greater Than                  10 > 22                         FALSE        |")
            print("|                                                                                         |")
            print("|_________________________________________________________________________________________|")
            print("|  <            Less than                    88 < 100                        TRUE         |")
            print("|                                                                                         |")
            print("|_________________________________________________________________________________________|\n")
            print("```````````````````````````````````````````````````````````````````````````````````````````")
            enter = input("Enter [if] to see an example conditional : ").upper()
            if enter == "IF":
                print(".---------------------------------. ")
                print("|  .---------------------------.  | ")
                print(
                    "|[]|  Life = 3                 |[]| <<< This is an example of using conditional statement.                ")
                print("|  |  if Life >= 2 :           |  |        - If you want to make other decision jus put,")
                print("|  |       print(''Win'')      |  |          [elif]. You can use this whanever you want. ")
                print("|  |  elif Life > 1 :          |  |")
                print("|  |       print(''Nice'')     |  |        - Make sure your conditional is intended :]")
                print("|  |  else :                   |  |        - Use [else] when you want a FALSE condition")
                print("|  |      print(''Bruh'')      |  |        - Don't forget to put this [:] with your condition.")
                print("|  |                           |  |")
                print(
                    "|  `---------------------------'  |===================================================================")
                print("|      __________________ _____   |   N E S T E D   C O N D I T I O N A L ")
                print("|     |   ___            |     |  |   It is the condition inside another condition.")
                print("|     |  |   |           |     |  |                 | ")
                print("|     |  |   |           |     |  |                 |")
                print("|     |  |   |           |     |  |                 |")
                print("|     |  |___|           |     |  |                 |")
                print("(_____|__________________|_____|__|                 |")
                print("                                                    +")
                print("          __________________________________________|_______________________________")
                print("          |```````````````````N E S T E D  C O N D I T I O N A L```````````````````|")
                print("          |________________________________________________________________________|")
                print("          |  stu = input(''Enter Mythic Glory(MG) :'')                             |")
                print("          |  rank = int(input(''Star points :'')                                   |")
                print("          |  if stu == ''MG'' :                                                    |")
                print("          |          if rank >= 100 :                                              |")
                print("          |               print(''Palong palo'')                                   |")
                print("          |          else :                                                        |")
                print("          |               print(''Low rank'')                                      |")
                print("          |  else :                                                                |")
                print("          |        print(''Lagay monga MG kahit di nag e ml'')                     |")
                print("          |________________________________________________________________________|\n")
                print(
                    "......................................................................................................")
                print("__________________________________________________________________________________________")
                print("|                                                                                        |")
                print("|      C H A P T E R   6    L O G I C A L    O P E R A T O R S                           |")
                print("|________________________________________________________________________________________|\n")
                print("What is LOGICAL OPERATORS?")
                print(
                    "Logical Operators are always used with conditional statement. They are use to reversed condition or combine.\n")
                print("__________________________________________________________________________________________")
                print("|                                                                                        |")
                print("(   L O G I C A L   O P E R A T O R S                                                    )")
                print("(________________________________________________________________________________________)")
                print("|                                                                                        |")
                print("|  and - Both Condition is TRUE                                                          |")
                print("|........................................................................................|")
                print("|                                                                                        |")
                print("|  or - One of the condition must be TRUE                                                |")
                print("|........................................................................................|")
                print("|                                                                                        |")
                print("|  not - Reverse the  result. TRUE = FALSE and FALSE = TRUE                              |")
                print("|........................................................................................|")
                print("|                                                                                        |")
                print("|  Example :                                                                             |")
                print("|                                                                                        |")
                print("|   age = 18                                     Take note : AND is all true.            |")
                print("|   got_vip = True                                           OR got atleast one true.    |")
                print("|                                                            NOT reverse the result.     |")
                print("|   if age >= 18 and got_vip :                                                           |")
                print("|      print(''Enjoy the party'')                                                        |")
                print("|   else :                                                                               |")
                print("|      print(''not allowed'')                                                            |")
                print("|                                                                                        |")
                print("|________________________________________________________________________________________|")
                print("|                                                                                        |")
                print("|   Example of NOT :                                                                     |")
                print("|                                                                                        |")
                print("|     sunny = True                                                                       |")
                print("|                                                                                        |")
                print("|     if not sunny :                                                                     |")
                print("|        print(''you can't play'')                                                       |")
                print("|     else :                                                                             |")
                print("|        print(''you can play'')                                                         |")
                print("|                                                                                        |")
                print("|________________________________________________________________________________________|\n")
                print("__________________________________________________________________________________________")
                print("|                                                                                        |")
                print("|                  C H A P T E R   7   P Y T H O N   L O O P S                           |")
                print("|________________________________________________________________________________________|")
                print("|                                                                                        |")
                print("|  What are LOOPS?                                                                       |")
                print("|                                                                                        |")
                print("|  Loops are used to repeat a block of code multiple times. Instead of writing the       |")
                print("|  same code again and again, we can use loops to make our program shorter and easier.   |")
                print("|________________________________________________________________________________________|\n")

                print("__________________________________________________________________________________________")
                print("|                                                                                        |")
                print("|                                 W H I L E   L O O P                                    |")
                print("|________________________________________________________________________________________|")
                print("|                                                                                        |")
                print("|  What is WHILE LOOP?                                                                    |")
                print("|                                                                                        |")
                print("|  A WHILE LOOP repeats a block of code as long as the condition is TRUE.                |")
                print("|                                                                                        |")
                print("|  SIMPLE MEANING: Repeat while the condition is TRUE.                                   |")
                print("|________________________________________________________________________________________|\n")

                print("STEP 1: BASIC SYNTAX")
                print("------------------------------------------------------------------------------------------")
                print("while condition:")
                print("    statement")
                print("------------------------------------------------------------------------------------------")
                print("while     - Starts the loop.")
                print("condition - Checks if the condition is TRUE or FALSE.")
                print("statement - The code that will repeat.\n")

                print("STEP 2: EXAMPLE")
                print("------------------------------------------------------------------------------------------")

                print("number = 1")
                print("")
                print("while number <= 5:")
                print("    print(number)")
                print("    number += 1")

                print("------------------------------------------------------------------------------------------")
                print("OUTPUT:")

                number = 1

                while number <= 5:
                    print(number)
                    number += 1

                print("------------------------------------------------------------------------------------------\n")

                print("STEP 3: HOW DOES IT WORK?")
                print("------------------------------------------------------------------------------------------")
                print("1. Set the starting number: number = 1")
                print("2. Check if number <= 5.")
                print("3. If TRUE, print the number.")
                print("4. Increase the number by 1 using number += 1.")
                print("5. Repeat until the condition becomes FALSE.")
                print("------------------------------------------------------------------------------------------\n")

                print("IMPORTANT REMINDER:")
                print("Always make sure that the condition will eventually become FALSE.")
                print("Otherwise, your program may create an INFINITE LOOP.\n")

                print("__________________________________________________________________________________________")
                print("|                                                                                        |")
                print("|                           F O R   L O O P                                              |")
                print("|________________________________________________________________________________________|")
                print("|                                                                                        |")
                print("|  What is FOR LOOP?                                                                      |")
                print("|                                                                                        |")
                print("|  A FOR LOOP repeats a block of code for each item in a sequence or for a specific     |")
                print("|  number of repetitions.                                                                |")
                print("|                                                                                        |")
                print("|  SIMPLE MEANING: Repeat for every item or number in a sequence.                        |")
                print("|________________________________________________________________________________________|\n")

                print("STEP 1: BASIC SYNTAX")
                print("------------------------------------------------------------------------------------------")
                print("for variable in sequence:")
                print("    statement")
                print("------------------------------------------------------------------------------------------")
                print("for      - Starts the loop.")
                print("variable - Stores the current item.")
                print("in       - Gets an item from the sequence.")
                print("sequence - The collection or range of items.")
                print("statement- The code that will repeat.\n")

                print("STEP 2: EXAMPLE")
                print("------------------------------------------------------------------------------------------")

                print("for number in range(1, 6):")
                print("    print(number)")

                print("------------------------------------------------------------------------------------------")
                print("OUTPUT:")

                for number in range(1, 6):
                    print(number)

                print("------------------------------------------------------------------------------------------\n")

                print("STEP 3: UNDERSTANDING RANGE()")
                print("------------------------------------------------------------------------------------------")
                print("range(1, 6) generates numbers from 1 up to 5.")
                print("The ending number is NOT included.")
                print("------------------------------------------------------------------------------------------\n")

                print("ANOTHER EXAMPLE:")
                print("------------------------------------------------------------------------------------------")

                print('for name in ["Kevin", "John", "Mark"]:')
                print('    print("Hello", name)')

                print("------------------------------------------------------------------------------------------")
                print("OUTPUT:")

                for name in ["Kevin", "John", "Mark"]:
                    print("Hello", name)

                print("------------------------------------------------------------------------------------------\n")

                print("__________________________________________________________________________________________")
                print("|                                                                                        |")
                print("|                 D I F F E R E N C E   O F   L O O P S                                  |")
                print("|________________________________________________________________________________________|")
                print("|                                                                                        |")
                print("|  WHILE LOOP: Repeats as long as a condition is TRUE.                                   |")
                print("|                                                                                        |")
                print("|  FOR LOOP  : Repeats through a sequence of items.                                      |")
                print("|                                                                                        |")
                print("|  WHILE LOOP: Useful when the number of repetitions is not known.                       |")
                print("|                                                                                        |")
                print("|  FOR LOOP  : Useful when the number of repetitions or items is known.                  |")
                print("|________________________________________________________________________________________|\n")

                print("------------------------------------------------------------------------------------------\n")
                print("__________________________________________________________________________________________")
                print("|                                                                                        |")
                print("|      SINCE I  DIDN'T  PUT DESIGN UNLIKE OTHER CHAPTER  LET ME GIVE YOU A SUMMARY       |")
                print("|________________________________________________________________________________________|")
                print("|                                                                                        |")
                print("|  1. A loop repeats a block of code.                                                    |")
                print("|  2. A WHILE LOOP repeats while its condition is TRUE.                                  |")
                print("|  3. A FOR LOOP repeats through a sequence.                                             |")
                print("|  4. The range() function generates a sequence of numbers.                              |")
                print("|  5. Indentation is important in Python loops.                                          |")
                print("|  6. An INFINITE LOOP happens when a loop never stops.                                  |")
                print("|________________________________________________________________________________________|\n")
        else :
            print("\nJust put [PICK] or [LSBS].\n")
    elif choi == "N" :
         print(".---..--------------------------------------------------------------------------------------------..---.")
         print("|   ||.------------------------------------------------------------------------------------------.||   |")
         print("| o |||    Thank you, for using this website! again am verity A.K.A Kevin :)                      || o |")
         print("| _ |||    My dream is to become a Web Developer someday! But to be honest am not good at coding. || _ |")
         print("|(_)|||    My grade is suck y'know, the only thing is whatever the result. Don't Give Up.         ||(_)|")
         print("|   |||    In this past few weeks i've been doing this project and yes proud to get this far >.<. ||   |")
         print("|.-.|||    I'm proud that me, myself and i finished this kind of project.                         || o |")
         print("|`-'|||    From what i learned. Don't compete with others. Maybe it's not your time yet. Maybe    ||`-'|")
         print("|   |||    Someday it was worth the risk than not taking risk. Keep learning. Keep Improving.     ||   |")
         print("|.-.|||    Mind set is, If you give up.You Lose.                                                  ||.-.|")
         print("| O |||                                                              Kevs -                       || O |")
         print("|`-'||`-------------------------------------------------------------------------------------------||`-'|")
         print("|`-'||`-------------------------------------------------------------------------------------------||`-'|")
         break
    else :

        print("\nPLEASE PUT (Y/N)!\n")




























