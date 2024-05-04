# def yld123u(u):
#     prob_points = []
#     while True:
#         if len(u) == 0:
#             received = yield 0
#         else:
#             received = yield u
#         u = u if received is None else received

# gen = yld123u([1,2,3])
# v0 = next(gen)
# v1 = gen.send([])
# v2 = gen.send([2,2,2])

def yld123u(u, a=None, b=None):
    assert(u is None)
    prob_points = []
    while True:
        if u is None:
            print("u is: ", u)
            u = yield a*b
        else:
            print("u is: ", u)
            u = yield a/b

gen = yld123u(None, 1, 2)
v0 = next(gen)
v1 = gen.send(1)
v2 = gen.send(None)
v3 = gen.send(2)
v4 = next(gen)
v5 = gen.send(3)
v6 = gen.send([2,2,2])


print("things: ")
print(v0)
print(v1)
print(v2)
print(v3)
print(v4)
print(v5)
print(v6)