class SystemCharacteristic:
    def update(self, current_state, p_state, pi1_state, pi2_state):
        raise NotImplementedError()

    @property
    def result(self):
        raise NotImplementedError()

    @property
    def name(self):
        raise NotImplementedError()


class AbsoluteThroughput(SystemCharacteristic):
    def __init__(self, tacts_count):
        self._result = 0
        self._tacts_count = tacts_count

    def update(self, current_state, p_state, pi1_state, pi2_state):
        if current_state[3] == '1' and not pi2_state:
            self._result += 1

    @property
    def result(self):
        return self._result / self._tacts_count

    @property
    def name(self):
        return 'A'


class RelativeThroughput(SystemCharacteristic):
    def __init__(self):
        self._input_entries = 0
        self._output_entries = 0

    def update(self, current_state, p_state, pi1_state, pi2_state):
        if current_state[0] == '0' and not p_state:
            self._input_entries += 1
        if current_state[3] == '1' and not pi2_state:
            self._output_entries += 1

    @property
    def result(self):
        return self._output_entries / self._input_entries

    @property
    def name(self):
        return 'Q'


class AverageQueueLength(SystemCharacteristic):
    def __init__(self, tacts_count):
        self._queue_length = 0
        self._tacts_count = tacts_count

    def update(self, current_state, p_state, pi1_state, pi2_state):
        if current_state[2] == '1':
            self._queue_length += 1

    @property
    def result(self):
        return self._queue_length / self._tacts_count

    @property
    def name(self):
        return 'L q'
