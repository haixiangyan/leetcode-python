def numberOfTokens(expiryLimit, commands):
    expires = {}

    for command in commands:
        [cmd, id, time] = command
        # GET
        if cmd == 0:
            expires[id] = time + expiryLimit
        # RESET
        else:
            # Ignore
            if time > expires[id]:
                del expires[id]
            # Reset
            else:
                expires[id] = time + expiryLimit

    return len(expires)

expiryLimit = 4
commands = [[0, 1, 1], [0, 2, 2], [1, 1, 5], [1, 2, 7]]

print(numberOfTokens(expiryLimit, commands))