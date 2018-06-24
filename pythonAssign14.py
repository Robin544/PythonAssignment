# REGULAR EXPRESSIONS
# Importing "Regular Expression"

import re


# Extract the user id, domain name and suffix from the following email addresses.
# emails = "zuck26@facebook.com"
#           "page33@google.com"
#            "jeff42@amazon.com"
# desired_output = [('zuck26', 'facebook', 'com'),
#                   ('page33', 'google', 'com'),
#                   ('jeff42', 'amazon', 'com')]

myEmails = "zuck26@facebook.com"" ""page33@google.com"" ""jeff42@amazon.com"
req_pattern = r'(\w+)@([A-Z0-9]+)\.([A-Z]{2,4})'
print("\n", re.findall(req_pattern, myEmails, flags=re.IGNORECASE))


# Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
# text = "Betty bought a bit of butter, But the butter was so bitter,
#         So she bought some better butter, To make the bitter butter better."

myText = "Betty bought a bit of butter, But the butter was so bitter," \
         "So she bought some better butter, To make the bitter butter better."
print("\n\n", re.findall(r'(\bB\w+)', myText, flags=re.IGNORECASE))
"""
\b\B is for making 'b' as boundary and flag makes case insensitive i.e., flag will ignore the capital or small case.
"""
print("\n\n")


# Split the following irregular sentence into words
# sentence = "A, very very; irregular_sentence"
# desired_output = "A very very irregular sentence"

irregular_sentence = "A, very very; irregular_sentence"
print(" " .join(re.split(r'[;,\s_]+', irregular_sentence)))
"""
.join function joins the irregular sentence which is split by " , ; _ ".
"""


# Clean up the following tweet so that it contains only the user’s message.
# That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.
# tweet = '''Good advice! RT @TheNextWeb: What I would do differently
#           if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
# desired_output = 'Good advice What I would do differently if I was learning to code today'

tweet = '''Good advice! RT @TheNextWeb: What I would do differently 
            if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
tweet = re.sub('http\S+\s*', '', tweet)  # remove URLs
"""
.sub function will replaces the occurance of first parameter with the second parameter.
this will replaces the 'URLs' with ''(blank)
"""
tweet = re.sub('RT|cc', '', tweet)
"""
this will replaces the 'RT|cc' with ''(blank)
"""
tweet = re.sub('#\S+', '', tweet)
"""
this will replaces the 'hashtags' with ''(blank)
"""
tweet = re.sub('@\S+', '', tweet)
"""
this will replaces the 'mentions' with ''(blank)
"""
tweet = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', tweet)
"""
this will replaces the 'punctuations' with ''(blank)
"""
tweet = re.sub('\s+', ' ', tweet)
"""
this will replaces the 'extra whitespaces' with ' '(two blanks)
"""
print("\n\n", tweet)        # print the required tweet


# Finally done

print("\n\nDone")
