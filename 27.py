def sort_by_occurrence(nums):
    from collections import defaultdict
    times = defaultdict(list)
    for i in nums:
        if i not in times:
            times[i].append(nums.count(i))
            times[i].append(nums.index(i))
    dic = sorted(times.items(), key=lambda item: (-item[1][0], item[1][1]))
    res = []
    for (k, v) in dic:
        res += [k]*v[0]
    resul = []
    for element in res:
        if element not in resul:
            resul.append(element)
    return resul
nums = list(map(int, input("a list").split()))
print(sort_by_occurrence(nums))
#上面兩行可用來input , output list


if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1, 1, 1, 2, 2, 3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板