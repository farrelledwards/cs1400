class Lion:
    def __init__(self, sound="rawr!"):
        self.sound = sound

    def emote(self):
        print(self.sound)
        return self.sound


def fn(l=[0,1,2,3,4]):
    print("the id of my parameter is", id(l))
    return l.pop()
    print("This does not happen!")


print("at this time, __name__ is", __name__)

if __name__ == "__main__":
    list0 = [1, 32, 43,12, 14, 39, 19, 77]
    list1 = []
    for i in range(len(list0)):
        if list0[i] % 2 == 0:
            list1.append(list0[i])

    print("Before:", list0, id(list0))
    fn(list0)
    print("After:", list0, id(list0))
    print("and list1 is:", list1, id(list1))

    # leo = Lion(sound="arggrhhh!")
    # leo.emote()

    # words = Lion(sound="I'm a one-and-done\tkind\nof\nlion").emote().split()
    # print(words)

    # leo.emote()
