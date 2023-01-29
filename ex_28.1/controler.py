import view

main_d = {}
st_d = []
pr_d = []


def start():
    while True:
        op = view.get_str()
        if op == 1:
            st = view.input_st()
            if st not in st_d:
                main_d[st] = {}
                st_d.append(st)
                if pr_d:
                    for pr in pr_d:
                        main_d[st][pr] = []
        elif op == 2:
            pr = view.input_pr()
            pr_d.append(pr)
            for name in st_d:
                main_d[name][pr] = []
        elif op == 3:
            name, pr, mark = view.input_mark()
            main_d[name][pr].append(mark)
        elif op == 4:
            print(main_d)
        elif op == 5:
            name = view.get_name()
            print(f'Marks {name} - {main_d[name]}')
        elif op == 6:
            break
        print(main_d)
