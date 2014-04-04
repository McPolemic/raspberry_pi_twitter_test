class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def message(self, m):
        total_length = self.width * self.height
        output = []
        for line_no in range(self.height):
            offset = line_no * self.width
            end = (line_no + 1) * self.width
            line = m[offset:end]
            output.append(line)

        return "\n".join(output).strip()
