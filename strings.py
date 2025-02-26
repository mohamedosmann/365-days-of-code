#space communication Decoder 

def decode_message(scrambled_message):
    reversed_message = scrambled_message[::-1]
    print(f"reversed message : {reversed_message}")
    decode_message = scrambled_message.replace("@", "a").replace("!", "i").replace("$", "s")
    print(f"decoded message after character replacement {decode_message}")
    words = decode_message.split()
    print(f"words after splitting {words}")

    final_message = ' '.join(words[::-1])
    print(f"final message {final_message}")

    return final_message

scrambled_message = "@idraw!"
print(f"Scrambled message is {scrambled_message}")

decoded = decode_message(scrambled_message)
print(f"decoded message is {decoded}")