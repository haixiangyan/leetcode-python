def func(ary):
    increaseCostf, decreaseCostf = 0, 0
    increaseCostb, decreaseCostb = 0, 0

    d_ary, i_ary = ary.copy(), ary.copy()

    for i in range(1, len(ary)):
        if d_ary[i] > d_ary[i - 1]:
            decreaseCostf += abs(d_ary[i] - d_ary[i - 1])
            d_ary[i] = d_ary[i - 1]
        if i_ary[i] < i_ary[i - 1]:
            increaseCostf += abs(i_ary[i] - i_ary[i - 1])
            i_ary[i] = i_ary[i - 1]
    d_ary, i_ary = ary.copy(), ary.copy()
    for i in range(len(ary) - 1, -1, -1):
        if i == 0: break
        if d_ary[i] > d_ary[i - 1]:
            decreaseCostb += abs(d_ary[i] - d_ary[i - 1])
            d_ary[i - 1] = d_ary[i]
        if i_ary[i] < i_ary[i - 1]:
            increaseCostb += abs(i_ary[i] - i_ary[i - 1])
            i_ary[i - 1] = i_ary[i]

    return min(increaseCostf, decreaseCostf, increaseCostb, decreaseCostb)