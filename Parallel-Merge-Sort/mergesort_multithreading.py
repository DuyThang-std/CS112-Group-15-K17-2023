import threading
import random
MAX = 1000#số phần tử có trong mảng
THREAD = 4#số luồng
part = 0
a = [0]*MAX#tạo mảng a gồm MAX phần tử


def merge(l, mid, r):
    left_arr = a[l:mid + 1]#mảng left
    right_arr = a[mid + 1:r + 1]#mảng right
    i = j = 0#i là idx mảng left,j là idx mảng right
    idx = l#chỉ số idx mảng a
    while i < len(left_arr) and j < len(right_arr):#chạy while đến khi 1 trong 2 mảng chạy hết
        if left_arr[i] <= right_arr[j]:#nếu val của left[i]<right[j]
            a[idx] = left_arr[i]#gán phần tử cho mảng left cho mảng a
            i += 1
            idx+=1
        else:#nếu val của left[i]<right[j]
            a[idx] = right_arr[j]#gán phần tử cho mảng left cho mảng a
            j += 1
            idx += 1

    while i < len(left_arr):#trường hợp mảng left chưa chạy hết
        a[idx] = left_arr[i]#gán phần tử cho mảng left cho mảng a
        i += 1
        idx += 1

    while j < len(right_arr):#trường hợp mảng right chưa chạy hết
        a[idx] = right_arr[j]#gán phần tử cho mảng right cho mảng a
        j += 1
        idx += 1
def merge_sort(l, r):
    if l < r:
        mid = (l+r)//2#chọn chỉ số giữa
        merge_sort(l, mid)#gọi đệ quy cho nửa đầu của mảng
        merge_sort(mid + 1, r)#gọi đệ quy cho nửa sau của mảng
        merge(l, mid, r)
def multi_merge_sort():
    global part#khai báo biến toàn cục cho biến part
    #tạo luồng mới
    for i in range(THREAD):
        t = threading.Thread(target=merge_sort, args=(part * (MAX // 4), (part + 1) * (MAX // 4) - 1))
        part += 1
        t.start()#bắt đầu
    # đợi các luồng hoàn thành
    for i in range(THREAD):
        t.join()

    # trộn 4 mảng lại sau khi đã được sắp xếp
    merge(0, (MAX // 2 - 1) // 2, MAX // 2 - 1)#trộn đầu
    merge(MAX // 2, MAX // 2 + (MAX - 1 - MAX // 2) // 2, MAX - 1)#trộn đuôi
    merge(0, (MAX - 1) // 2, MAX - 1)#trộn toàn bộ mảng
def creating_test_case():
    #tạo test case random số từ 0->10000
    for i in range(MAX):
        a[i] = random.randint(0, 10000)

if __name__ == '__main__':
   creating_test_case()
   multi_merge_sort()
   print("Mang da sap xep:", a)

