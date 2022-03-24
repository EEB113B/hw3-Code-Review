def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    num = {}                       # 建立空字典{數字:次數}
    n = []                         # 建立空集合
    ans = []
    for i in nums:
        if i not in num:
            num[i] = 1 
        else:
            num[i] += 1            # 有此數據則集合裡面 +1
            
    for k, s, in num.items():      # s是數字；k是次數
        n.append([s,k])            # append後的元素加在串列最後面
    n = sorted(n)                  # 整理集合
    for k in n:
        c = k[1]                   # 取次數
        ans.append(c)              # 在此集合後方加入各次數
    return ans                     # 回傳


if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。

    input_list = [5,5,6,6,6,6,0,1,1,1]
    output_list = sort_by_occurrence(input_list)
    print(output_list)

#留言板