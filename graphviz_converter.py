import re


TRANSITION_REGEX = r"\"(\d+)\" -> \"(\d+)\" \[.*label = \"(.+)\".*\];"
CONFIG_TEMPALTE = '''STATES = [
{}
]'''
INDENT = ' '*4

def format_statement(statement):
    return statement.replace("\\n", "").replace("*", " and ").replace("1-p", "not p")\
        .replace("1-&pi;₁", "not pi1").replace("1-&pi;₂", "not pi2")\
        .replace("&pi;₁", "pi1").replace("&pi;₂", "pi2")


def main():
    fin = open("./states.gv", "r", encoding='UTF-8')

    matches = re.finditer(TRANSITION_REGEX, "".join(fin.readlines()))

    all_states = {}

    entries = []
    for _, match in enumerate(matches):
        groups = match.groups()
        start_state = groups[0]
        end_state = groups[1]
        for statement in groups[2].split("+"):
            if format_statement(statement):
                all_states[start_state] = 0
                entries.append(INDENT + "['" + start_state + "', '" + end_state + "', lambda p, pi1, pi2: " + format_statement(statement) + "],")
    with open('states.py', 'w') as fout:
        fout.write(CONFIG_TEMPALTE.format('\n'.join(entries)))


if __name__ == '__main__':
    main()
