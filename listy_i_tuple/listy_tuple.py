marketing = ["loyality program", "client promotion", "market research"]
marketing.append('public relations')
print(marketing[3])
marketing.insert(2, 'investor relations')
emailMarketing = marketing.copy()
print(emailMarketing)
emailMarketing.sort()
internalEmails = ['internal communication']
emailMarketing += internalEmails
emailTuple = tuple(emailMarketing)
print(emailTuple)