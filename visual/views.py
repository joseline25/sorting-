from django.shortcuts import render, redirect
from .forms import *
from matplotlib import pyplot as plt
import io
import urllib, base64

# sorting functions

def swap(a,b):
    temp = a
    a = b
    b = temp
    return a, b


#tri par selection

def triSelection(arr):
    n = len(arr)
    for i in range(0,n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        swap(arr[min_index], arr[i])

    return arr

# tri par bulle

def bubble_sort(array):
    n = len(array)

    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break

    return array


# tri par Insertion

def insertion_sort(array):

    for i in range(1, len(array)):

        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item

    return array

# merge sort

def merge(left, right):

    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def merge_sort(array):
    if len(array) < 2:
        return array

    midpoint = len(array) // 2
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))



# tri rapide


def quicksort(array):
    if len(array) < 2:
        return array

    low, same, high = [], [], []
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
    return quicksort(low) + same + quicksort(high)


# Create your views here.



def index(request):

    return render(request, 'index.html')



def liste(request):
    listes = Liste.objects.all()
    count = listes.count()
    listes_tab = []
    for i in listes:
        listes_tab.append(i)
    context = {'listes': listes,
               'count': count,
               'listes_tab': listes_tab
               }
    return render(request, 'indexliste.html', context)



def newlist(request):
    form = createListe()
    if request.method == "POST":
        form = createListe(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste')
    context = {'form': form}

    return render(request, 'newliste.html', context)




def newTag(request, id):

    liste = Liste.objects.get(id=id)
    val = liste.taille
    tab = []
    for i in range(0, val):
        tab.append(randint(0, 1000))
    liste.tags = tab
    liste.save()

    plt.plot(liste.tags)
    #plt.bar(range(1000), liste.tags)
    #plt.show()
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    context = {'liste': liste, 'data': uri}
    return render(request, 'displayliste.html', context)





def Insertionsort(request, id):
    liste = Liste.objects.get(id=id)
    arr = liste.tags
    sortedList = insertion_sort(arr)

    plt.plot(sortedList)
    # plt.bar(range(1000), liste.tags)
    # plt.show()
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    return render(request, 'sortedList.html', {'liste': sortedList, 'data': uri})

def Selectiontionsort(request, id):
    liste = Liste.objects.get(id=id)
    arr = liste.tags
    sortedList = triSelection(arr)

    return render(request, 'sortedList1.html', {'liste': sortedList})

def Bublesort(request, id):
    liste = Liste.objects.get(id=id)
    arr = liste.tags
    sortedList = bubble_sort(arr)

    return render(request, 'sortedList2.html', {'liste': sortedList})


def Quicksort(request, id):
    liste = Liste.objects.get(id=id)
    arr = liste.tags
    sortedList = quicksort(arr)

    return render(request, 'sortedList3.html', {'liste': sortedList})


"""
def Bubblesort(request, id):
    arr = Liste.objects.get(id=id)
    n = arr.taille
    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                already_sorted = False
        if already_sorted:
            break

    return redirect(request,'index', arr)


def insertion_sort(request, id):
    arr = Liste.objects.get(id=id)
    n = arr.taille
    for i in range(1, n):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return redirect(request,'index', arr)



def merge(left, right):

    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):

        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


"""




