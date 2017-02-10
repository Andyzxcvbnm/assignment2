def diffWaysToCompute(self, input):
    if input.isdigit():
        return [int(input)]
    r = []
    for i in xrange(len(input)):
        if input[i] in "-+*":
            r1 = self.diffWaysToCompute(input[:i])
            r2 = self.diffWaysToCompute(input[i+1:])
            for j in r1:
                for k in r2:
                    r.append(self.helper(j, k, input[i]))
    return r
