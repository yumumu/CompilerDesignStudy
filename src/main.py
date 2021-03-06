#!/usr/bin/python
# -*- coding: utf-8 -*-


from simple_lexer import SimpleLexer
from simple_calculator import SimpleCalculator
from simple_script import SimpleScript

def lexter_test():
    script = "int age = 45;"
    print("parse :" + script)
    token_reader = SimpleLexer().tokenize(script)
    token_reader.dump()

    script = "inta age = 45;"
    print("parse :" + script)
    token_reader = SimpleLexer().tokenize(script)
    token_reader.dump()

    script = "in age = 45;"
    print("parse :" + script)
    token_reader = SimpleLexer().tokenize(script)
    token_reader.dump()

    script = "age >= 45;"
    print("parse :" + script)
    token_reader = SimpleLexer().tokenize(script)
    token_reader.dump()

    script = "age > 45;"
    print("parse :" + script)
    token_reader = SimpleLexer().tokenize(script)
    token_reader.dump()


def dump(code, token_reader):
    print('*' * 10 + ' ' + code + ' ' + '*' * 10)
    token_reader.dump()
    print('*' * 50)


def calculator_test():
    calculator = SimpleCalculator()

    script = "int a = b + 3;"
    print("解析变量声明语句: " + script)
    lexer = SimpleLexer()
    token_reader = lexer.tokenize(script)
    dump(script, token_reader)

    try:
        node = calculator.int_declare(token_reader)
        node.dump_ast("")
    except Exception as e:
        print('something wrong: ', e)

    script = "2+3*5"
    print("计算: " + script + "，看上去一切正常。")
    calculator.evaluate(script)

    # 测试语法错误
    # script = "2+"
    # print("\n: " + script + "，应该有语法错误。")
    # calculator.evaluate(script)

    script = "2+3+4"
    print("\n计算: " + script + "，结合性出现错误。")
    calculator.evaluate(script)


def repl_test():
    script = SimpleScript()
    script.start()


if __name__ == '__main__':
    # lexter_test()
    # calculator_test()
    repl_test()
    