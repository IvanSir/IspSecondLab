import dill as pickl


class Pickle:

    def dump(obj, file="testpickle.pickle"):
        f = open(file, 'w')
        f.write(pickl.dumps(obj))
        f.close()

    def dumps(obj):
        return pickl.dumps(obj)

    def load(file="test.json"):
        f = open(file, 'r')
        packed = pickl.loads(f.read())
        f.close()
        return packed

    def loads(src):
        packed = pickl.loads(src)
        return packed
