
def my_function():
    K=5
    k_dict = {"d"+str(k+1):"" for k in range(K)}
    print("k dict initialized", k_dict)

    D = [1, 2, 3, 3, 2, 1]

    for d in D:
        #if k_dict.get(str(d)) is not None:
        if str(d) not in k_dict:
            print(d, "is not in", k_dict, "will add d to it")
            k_dict[str(d)] = ""
            print("after adding", k_dict)
            my_keys = list(k_dict)
            print("my keys", my_keys)
            k0 = my_keys[0]
            print("k0 is", k0)
            print("remove the first key")
            del k_dict[k0]
            print("finally the dictionary looks like", k_dict)


if __name__ == '__main__':
    my_function()
