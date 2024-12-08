def testDecorator(input_func):
    def output_func(*args):
        # extra logic
        count = len(args[0])
        print("-" * count)
        input_func(*args)
        # extra logic
        print("-" * count)

    return output_func

@testDecorator
def showMessage(text):
    print(text)

showMessage("Hello decorators aegaerukfgae")