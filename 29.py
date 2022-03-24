def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    nums = []
    i = 0
    while i <= 9:
        total = 0
        numbers_count = []
        if input_list.count(i) == 0:                   # 判斷0 ~ 9有那些數有在input_list裡
            i += 1
            continue
        else:
            total += input_list.count(i)               # 計算input_list中出現的數字各有幾個
            numbers_count.append(i)
            numbers_count.append(total)
            nums.append(numbers_count)                 # nums print出來結果為[[數字,次數],[數字,次數],...]
            i += 1
    nums = sorted(nums,key = (lambda x:x[1]))          # 取次數做大小排列

    a = len(nums)                                      # 判斷有多少不同的數字
    j = 0
    nums1 = []
    while j < a:
        nums1.append(nums[j][0])                       # 只取數字不要次數
        j += 1
    nums = nums1    
    return nums


if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [2,0,9,8,9,2,8,2,0,9,7,9,8,2,9]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板