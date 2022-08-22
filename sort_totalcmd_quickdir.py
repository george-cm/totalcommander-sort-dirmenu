import configparser


def main():
    config = configparser.RawConfigParser()
    config.optionxform = str # type: ignore
    with open("wincmd.ini", "r", encoding="cp1251") as inf:
        config.read_file(inf)
    # print(config.sections())
    # for k, v in config["DirMenu"].items():
    #     print(k, v)
    # k = list(config['DirMenu'].keys())
    v = list(config["DirMenu"].values())
    # print(k)
    # print(v)
    menus = v[::2]
    cmds = v[1::2]
    dirs = dict(zip(menus, cmds))
    dirs = {k: dirs[k] for k in sorted(dirs, key=str.lower)}
    i = 1
    for k, v in dirs.items():
        print(f"{k}:\t'{v}'")
        config["DirMenu"][f"menu{i}"] = k
        config["DirMenu"][f"cmd{i}"] = v
        i += 1
    with open("wincmd_sorted.ini", 'w', encoding='cp1251') as f:
        config.write(f) # type: ignore


if __name__ == "__main__":
    # import timeit
    # from datetime import timedelta
    # print(str(timedelta(seconds=timeit.timeit(main, number=1))))
    main()
