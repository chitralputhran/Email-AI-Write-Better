system_prompt = '''Act as an email expert who has reviewed much information regarding writing effective emails online.'''

user_prompt = '''Can you please come up with a well-formatted email with new lines whenever needed for the following: 
{email_topic}
The tone of the email has to be {email_tone}. 
The email can have up to {num_of_lines} lines. 
The name of the sender is {sender_name}. 
The name of the receiver is {receiver_name}'''