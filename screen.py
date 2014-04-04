class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def message(self, m, single_line=False):
        if single_line:
            lines = 1
        else:
            lines = self.height

        output = []
        for line_no in range(lines):
            offset = line_no * self.width
            end = (line_no + 1) * self.width
            line = m[offset:end]
            output.append(line)

        return "\n".join(output).strip()

    def multi_message(self, messages):
        messages = [self.message(m, single_line=True) for m in messages[:self.height]]

        return "\n".join(messages)

    def scroll_message(self, message):
        output = []
        animation_frames = len(message) - self.width + 1
        for offset in range(animation_frames):
            output.append(self.message(message[offset:], single_line=True))
        return output
