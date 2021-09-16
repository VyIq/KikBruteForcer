# Why you can't brute force Kik
This is only a proof of concept to show why people who say they brute force kik are _**dirty liars**_, and people who get "cracked" are just gullible.

If you were to connect this script with a captcha solving service, it could be _THEORETICALLY_ possible to brute force an account.

However....

- You may be IP banned in many cases, and kik will block attempts from flagged IPs. (Most VPNs have flagged IPs.) But even if you make your own VPN to avoid this, and write a script for it to change IPs every time you get banned...

- Each captcha gets harder, and takes longer to solve. If you are using a captcha solving service, this means it would _cost more_ to solve too. 

- You can only dish out a few attempts a second, this is not a code limitation, this has to do with Kik's servers. Kik can only handle so many login attempts at once!

It could take _literal lifetimes_ to crack an average password. So unless you already know the person and have hints on what types of passwords the account holder may use...

Kik "brute forcers" are full of shit.

# How people fake it
So now you may be saying "Oh but I've seen cracked accounts!"

Thats because it is possible to take over Kik accounts. There are two popular methods!

- People often used their real name on kik accounts, and emails that are along the lines of johnsmith@gmail.com. Knowing this, they use kik's password reset page on generic accounts, and if they can guess the email (it shows you part of the email, like j-------h@g----.com) then they will either attack the email if its an easy domain, or use password leak websites such as Dehashed in hopes of "cracking" the email, changing the password, and obtaining the Kik account. 

- When a user is active, it is possible to use a phishing attack against them. The most common one is fake unbrickers, but when this doesn't work you can get pretty inventive with it. Such as spoofing yourself as @kikteam and fooling the user to give up their details, using a fake password reset site, or a password reset/unbrick bot.

People who do this like to claim that they are actually brute forcing accounts, but this is not true.

If you have any questions, comments, or concerns, shoot me an email anytime! StethoSpasm@Gmail.com

# Usage
If you want to try out the bruteforcer anyways, use `git clone https://github.com/StethoSaysHello/KikBruteForcer`

Add your password guesses to Passlist.txt.

Then run BruteForce.py and enter the username you would like to brute force when prompted.

It will attempt to login with each password on the list until it works, you get a captcha, or you get IP banned.
