import random
#Random
q = input("Ask your question and shake the ball.\n")
ans = ["Yes - definitely.","It is decidedly so.","Without a doubt.","Reply hazy, try again.","Ask again later.","Better not tell you now.","My sources say no.","Outlook not so good.","Very doubtful."]
ran = random.randint(0,8)

print(ans[ran])