def sort_by_occurrence(nums):
    num=[884462544226848]
    unique=list(set(num))

    times=[]
    for i in range(5):
        tar=num.count(unique[i])
        times.append(tar)
        newlist=sorted(times)

        print(newlist)
    

    return list



    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡


if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1, 1, 1, 2, 2, 3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板