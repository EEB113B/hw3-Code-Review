def sort_by_occurrence(nums):
    d1 ={}
    e = []
    ans = []
    for i in nums:
        if i not in d1:
            d1[i] = 1
        else:
            d1[i] += 1
    for k,s in d1.items():
        e.append([s,k])
    e = sorted(e)
    for k in e:
        c = k[1]
        ans.append(c)
    return ans


if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1, 1, 1, 2, 2, 3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板