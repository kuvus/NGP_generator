from random import randrange

FILE_NAME = '11F.dat'
OUT_NUMBER = 31415
IN_RANGE = (1, 10)
OUT_RANGE = (1, 10)
IN_COUNT = randrange(1, 10)
# OUT_COUNT = randrange(1, 10)
OUT_COUNT = 1

PARAMS = {
    'population_size': 100,
    'max_gen_count': 100,
    'max_depth': 5,
    'time_limit': 100,
    'fit_function': 'fitExact'
}


# fitExact / fitInclude

def generate_header(params):
    header = ', '.join(list(map(lambda x: x + "=" + str(params[x]), params.keys())))
    return header


def generate_ios(inputs_range: tuple[int, int], outputs_range: tuple[int, int], req_num: int, inputs_count: int,
                 outputs_count: int):
    count = randrange(5, 10)
    out = []
    print(inputs_count, outputs_count)
    for i in range(count):
        inputs = []
        outputs = []
        for _ in range(inputs_count):
            inputs.append(str(randrange(inputs_range[0], inputs_range[1])))
        for _ in range(outputs_count):
            outputs.append(str(randrange(outputs_range[0], outputs_range[1])))
        if req_num not in outputs:
            outputs[randrange(0, outputs_count)] = str(req_num)
        out.append((inputs, outputs))

    return out


def main(fn):
    header = generate_header(PARAMS)
    ios = generate_ios(IN_RANGE, OUT_RANGE, OUT_NUMBER, IN_COUNT, OUT_COUNT)

    with open(f'files/{fn}', 'w') as f:
        f.write(header + '\n')
        f.write(str(IN_COUNT) + '' + str(OUT_COUNT) + '\n')
        for io in ios:
            f.write(' '.join(io[0]) + ' ' + ' '.join(io[1]) + '\n')


if __name__ == '__main__':
    main(FILE_NAME)
