def detect_sender(message):
    has_smiley = ":)" in message
    has_frowny = ":(" in message
    print(has_smiley,has_frowny)

    if has_smiley and not has_frowny:
        return "alive"
    elif has_frowny and not has_smiley:
        return "undead"
    elif has_smiley and has_frowny:
        return "double agent"
    else:
        return "machine"

# Example usage
message = input()
result = detect_sender(message)
print(result)
