from functools import reduce

def extract_options(argv):
    args = argv.split("--")
    return reduce(buildOption, args, {})

def buildOption(options, arg):
    if not arg or arg.count(" ") < 1:
        return options
    optName, optValue = arg.split(" ", 1)
    options[optName] = optValue
    return options