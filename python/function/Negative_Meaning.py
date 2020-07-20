def not_string(word):
    result = word
    if word[0:3] != "not": result = "not "+ word
    return result

print(not_string('sugar'))
print(not_string('not bad'))