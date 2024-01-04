#!/usr/bin/python3
import dis


def print_hidden_names(module_file):
    with open(module_file, 'rb') as file:
        bytecode = file.read()
        instructions = dis.get_instructions(bytecode)
        names = set()

    for instr in instructions:
        if instr.opname == 'LOAD_NAME' and not instr.arg.startswith('__'):
            names.add(instr.arg)

    for name in sorted(names):
        print(name)


if __name__ == "__main__":
    print_hidden_names("hidden_4.pyc")
