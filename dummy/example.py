from typing import Generator, Union

__all__ = ("main1", "main2")

def main1() -> Union[str, bytes]:
    return 'hello world'


def main2() -> Generator[Union[str, bytes], None, int]:
    yield "hello"
    yield " "
    yield "world"
    return 123 # size of response

def is_generator(co):
    return co.__code__.co_flags & 32


test_functions = [main1, main2]

for f in test_functions:
    response: str = ''
    if is_generator(f):
        for part in f():
            response += part
    else:
        response = f()
    
    print(response)
