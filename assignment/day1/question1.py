# Using any of the conditional statement learnt to write a simple Python program that will
# output the score and remark eg “Your score is 76 and this is Excellence” using the algorithm
# below. Make sure that invalid score such value greater than 100 or less than 1 are detected
# and reported
#  0 – 34 = Fail
#  35 – 44 = Pass
#  45 – 49 = Fair
#  50 – 59 = Good
#  60 – 69 = Very Good
#  70 – 100 = Excellence

score = int(input('Enter score: '))


if score >=0 and score < 35:
    print('Your score is '+str(score)+' and this is Fail')
elif score >= 35 and score < 45:
    print('Your score is '+str(score)+' and this is Pass')
elif score >= 45 and score < 50:
    print('Your score is '+str(score)+' and this is Fair')
elif score >= 50 and score < 60:
    print('Your score is '+str(score)+' and this is Good')
elif score >= 60 and score < 70:
    print('Your score is '+str(score)+' and this is Very Good')
elif score >= 70 and score <= 100:
    print('Your score is '+str(score)+' and this is Excellence')
else:
    print('invalid score')
