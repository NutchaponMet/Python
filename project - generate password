# Project Beginner -- Generate Password --

import random

num_low_txt = "1234567890abcdefghijklmnopqrstuvwxyz"
# lower_txt = "abcdefghijklmnopqrstuvwxyz"
upper_text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
latex = "#@.-_$%&"

def generator_Pass():
     upper_case = "".join(random.sample(upper_text, k=3))
     spacial = "".join(random.sample(latex, k=1))
     sample_space = "".join(random.sample(num_low_txt, k=11))
     password = upper_case + spacial + sample_space
     return "".join(password)

if __name__=="__main__":
     # psw = int(input("Enter lenght your password: "))
     print("This is your password:",generator_Pass())
     
