from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import simpledialog
import tkinter.scrolledtext as scrolledtext
import timeit
import matplotlib.pyplot as plt
from memory_profiler import memory_usage
memories = []
t1 = 0
t2 = 0
t3 = 0
t4 = 0
t5 = 0
mem1 = 0
mem2 = 0
mem3 = 0
mem4 = 0
mem5 = 0
op1 = 0
op2 = 0
op3 = 0
op4 = 0
op5 = 0


def get_memory(mem, ended):
    global m2
    global m1
    if ended:
        highest_mem = max(mem)
        m2 = highest_mem
    else:
        memories.append(mem)


full_com = 0
oper = 0


def button_click6():
    global oper
    global full_com
    new_combobox.set('')
    new_combobox.config(state=NORMAL)
    new_submit.config(state=NORMAL)
    list2.delete(0, END)
    list1.delete(0, END)
    time_entry.delete(0, 'end')
    space_entry.delete(0, 'end')
    size_entry.config(state=DISABLED)
    new_submit2.config(state=DISABLED)
    new_submit3.config(state=DISABLED)
    new_submit4.config(state=DISABLED)
    new_submit5.config(state=DISABLED)
    new_submit6.config(state=DISABLED)
    new_submit7.config(state=DISABLED)
    oper = 1
    if (op1 == 1):
        full_com = full_com + 1
    elif (op2 == 1):
        full_com = full_com + 1
    elif (op3 == 1):
        full_com = full_com + 1
    elif (op4 == 1):
        full_com = full_com + 1
    elif (op5 == 1):
        full_com = full_com + 1


def result():
    global answer1, op1, op2, op3, op4, op5
    answer1 = messagebox.askquestion(
        "Sorting tecnique", "do you really want to submit")
    if answer1 == 'yes':
        list2.config(state=NORMAL)
        if sort_var == "Bubble Sort":
            if (op1 == 0):
                list2.insert(1, "def bubble_sort(sort_list):")
                list2.insert(2, "\t \t for j in range(len(sort_list)):")
                list2.insert(
                    3, "\t \t \t for k in range(len(sort_list) - 1): ")
                list2.insert(
                    4, "\t \t \t \t if sort_list[k] > sort_list[k + 1]:")
                list2.insert(
                    5, "\t \t \t \t \t sort_list[k], sort_list[k + 1] = sort_list[k + 1], sort_list[k] ")
                list2.insert(6, "\t \t  print(sort_list) ")
                op1 = op1 + 1
            else:
                messagebox.showerror(
                    "Error", "Please choose the other sorting techniques")
        elif sort_var == "Insertion Sort":
            if (op2 == 0):
                list2.insert(1, "def insertion_sort(sort_list):")
                list2.insert(2, "\t \t for i in range(1, len(sort_list)):")
                list2.insert(3, "\t \t \t key = sort_list[i] ")
                list2.insert(4, "\t \t \t j = i - 1")
                list2.insert(
                    5, "\t \t \t while j >= 0 and key < sort_list[j]: ")
                list2.insert(6, "\t \t \t \t sort_list[j + 1] = sort_list[j]")
                list2.insert(7, "\t \t \t \t j -= 1")
                list2.insert(8, "\t \t \t sort_list[j + 1] = key ")
                list2.insert(
                    9, "\t \t  print('\nThe sorted list: \t', sort_list)")
                list2.insert(10, "\t \t print('\n')")
                op2 = op2 + 1
            else:
                messagebox.showerror(
                    "Error", "Please choose the other sorting techniques")
        elif sort_var == "Selection Sort":
            if (op3 == 0):
                list2.insert(1, "def selection_sort(sort_list):")
                list2.insert(2, "\t \t for i in range(len(sort_list)):")
                list2.insert(
                    3, "\t \t \t smallest_element = min(sort_list[i:])")
                list2.insert(
                    4, "\t \t \t index_of_smallest = sort_list.index(smallest_element)")
                list2.insert(
                    5, "\t \t \t sort_list[i], sort_list[index_of_smallest] = sort_list[index_of_smallest], sort_list[i] ")
                list2.insert(
                    6, "\t \t print ('\n\nThe sorted list: \t', sort_list)")
                op3 = op3 + 1
            else:
                messagebox.showerror(
                    "Error", "Please choose the sorting techniques")
        elif sort_var == "Quick sort":
            if (op4 == 0):
                list2.insert(1, "def partition(sort_list, low, high):")
                list2.insert(2, "\t \t i = (low -1)")
                list2.insert(3, "\t \t pivot = sort_list[high]")
                list2.insert(4, "\t \t for j in range(low, high):")
                list2.insert(5, "\t \t \t if sort_list[j] <= pivot:")
                list2.insert(6, "\t \t \t \t i += 1")
                list2.insert(
                    7, "\t \t \t \t sort_list[i], sort_list[j] = sort_list[j], sort_list[i]")
                list2.insert(
                    8, "\t \t sort_list[i+1],sort_list[high] = sort_list[high], sort_list[i+1] ")
                list2.insert(9, "\t \t return (i+1)")
                list2.insert(10, "def quick_sort(sort_list, low, high):")
                list2.insert(11, "\t \t if low < high:")
                list2.insert(
                    12, "\t \t \t pi = partition(sort_list, low, high)")
                list2.insert(13, "\t \t \t quick_sort(sort_list, low, pi-1)")
                list2.insert(14, "\t \t \t quick_sort(sort_list, pi+1, high)")
                op4 = op4 + 1
            else:
                messagebox.showerror(
                    "Error", "Please choose the other sorting techniques")
        elif sort_var == "Merge Sort":
            if (op5 == 0):
                list2.insert(1, "def mergeSort(nlist):")
                list2.insert(2, "\t \t if len(nlist)>1:")
                list2.insert(3, "\t \t \t mid = len(nlist)//2")
                list2.insert(4, "\t \t \t lefthalf = nlist[:mid]")
                list2.insert(5, "\t \t \t righthalf = nlist[mid:]")
                list2.insert(6, "\t \t \t mergeSort(lefthalf)")
                list2.insert(7, "\t \t \t mergeSort(righthalf)")
                list2.insert(8, "\t \t \t i=j=k=0")
                list2.insert(
                    9, "\t \t \t while i < len(lefthalf) and j < len(righthalf):")
                list2.insert(10, "\t \t \t \t if lefthalf[i] < righthalf[j]:")
                list2.insert(11, "\t \t \t \t \t nlist[k]=lefthalf[i]")
                list2.insert(12, "\t \t \t \t \t i=i+1")
                list2.insert(13, "\t \t \t \t else:")
                list2.insert(14, "\t \t \t \t \t nlist[k]=righthalf[j]")
                list2.insert(15, "\t \t \t \t \t j=j+1")
                list2.insert(16, "\t \t \t \t k=k+1")
                list2.insert(17, "\t \t \t while i < len(lefthalf):")
                list2.insert(18, "\t \t \t \t nlist[k]=lefthalf[i]")
                list2.insert(19, "\t \t \t \t i=i+1")
                list2.insert(20, "\t \t \t \t k=k+1")
                list2.insert(21, "\t \t \t while j < len(righthalf):")
                list2.insert(22, "\t \t \t \t nlist[k]=righthalf[j]")
                list2.insert(23, "\t \t \t \t j=j+1")
                list2.insert(24, "\t \t \t \t k=k+1")
                list2.insert(25, "\t \t print('Merging',nlist)")
                op5 = op5 + 1
            else:
                messagebox.showerror(
                    "Error", "Please choose the other sorting techniques")


def call_me():
    global sort_var
    sort_var = sorting_name.get()
    if (oper == 1):
        size_entry.config(state=DISABLED)
        new_submit2.config(state=DISABLED)
        result()
        if answer1 == 'yes':
            new_combobox.config(state=DISABLED)
            new_submit.config(state=DISABLED)
            new_submit4.config(state=NORMAL)
            new_submit5.config(state=NORMAL)
            new_submit6.config(state=NORMAL)
            new_submit7.config(state=NORMAL)
        else:
            messagebox.showerror(
                "Error", "Please choose the sorting techniques")
    elif (oper == 0):
        result()
        if answer1 == 'yes':
            size_entry.config(state=NORMAL)
            new_submit2.config(state=NORMAL)
            new_combobox.config(state=DISABLED)
            new_submit.config(state=DISABLED)
        elif answer1 == 'no':
            messagebox.showerror(
                "Error", "Please choose the sorting techniques")


def button_click2():
    global size
    size = size_var.get()
    if (size <= 30000):
        answer1 = messagebox.askquestion(
            "Size of Array ", "do you really want to fixed size of input")
        if answer1 == 'yes':
            new_submit3.config(state=NORMAL)
            size_entry.config(state=DISABLED)
            new_submit2.config(state=DISABLED)
    else:
        messagebox.showerror("Error", "please size insert under 1 to 30000")


lst = []


def button_click3():
    new_submit4.config(state=NORMAL)
    for i in range(size):
        element_val = simpledialog.askinteger(
            "input integer", "Please Enter The Values")
        lst.append(element_val)
    new_submit3.config(state=DISABLED)


def button_click4():
    global t1, t2, t3, t4, t5
    global mem1, mem2, mem3, mem4, mem5
    time_entry.config(state=NORMAL)
    space_entry.config(state=NORMAL)
    new_submit5.config(state=NORMAL)
    new_submit6.config(state=NORMAL)
    new_submit7.config(state=NORMAL)
    if sort_var == "Bubble Sort":
        def bubble_sort(sort_list):
            for j in range(len(sort_list)):
                for k in range(len(sort_list) - 1):
                    if sort_list[k] > sort_list[k + 1]:
                        sort_list[k], sort_list[k +
                                                1] = sort_list[k + 1], sort_list[k]
            out_list = sort_list
            list1.insert(END, out_list)
            ended = False
            get_memory(memory_usage(), ended)
        time = []
        start = timeit.default_timer()
        bubble_sort(lst)
        end = timeit.default_timer()
        ended = True
        get_memory(memory_usage(), ended)
        time.append(end-start)
        time_sort = float(sum(time)/len(time))
        time_entry.insert(INSERT, time_sort)
        t1 = float(time_sort)
        mem_diff = m2
        space_entry.insert(INSERT, mem_diff)
        mem1 = float(mem_diff)
    elif sort_var == "Insertion Sort":
        def insertion_sort(sort_list):
            for i in range(1, len(sort_list)):
                key = sort_list[i]
                j = i - 1
                while j >= 0 and key < sort_list[j]:
                    sort_list[j + 1] = sort_list[j]
                    j -= 1
                sort_list[j + 1] = key
            out_list = sort_list
            list1.insert(END, out_list)
            ended = False
            get_memory(memory_usage(), ended)
        time = []
        start = timeit.default_timer()
        insertion_sort(lst)
        end = timeit.default_timer()
        ended = True
        get_memory(memory_usage(), ended)
        time.append(end-start)
        time_sort = (sum(time)/len(time))
        time_entry.insert(INSERT, time_sort)
        t2 = float(time_sort)
        mem_diff = m2
        space_entry.insert(INSERT, mem_diff)
        mem2 = float(mem_diff)
    elif sort_var == "Selection Sort":
        def selection_sort(sort_list):
            for i in range(len(sort_list)):
                smallest_element = min(sort_list[i:])
                index_of_smallest = sort_list.index(smallest_element)
                sort_list[i], sort_list[index_of_smallest] = sort_list[index_of_smallest], sort_list[i]
            out_list = sort_list
            list1.insert(END, out_list)
            ended = False
            get_memory(memory_usage(), ended)
        mem_diff = []
        time = []
        start = timeit.default_timer()
        selection_sort(lst)
        end = timeit.default_timer()
        ended = True
        get_memory(memory_usage(), ended)
        time.append(end-start)
        time_sort = (sum(time)/len(time))
        time_entry.insert(INSERT, time_sort)
        t3 = float(time_sort)
        mem_diff = m2
        space_entry.insert(INSERT, mem_diff)
        mem3 = float(mem_diff)
    elif sort_var == "Merge Sort":
        def mergeSort(nlist):
            if len(nlist) > 1:
                mid = len(nlist)//2
                lefthalf = nlist[:mid]
                righthalf = nlist[mid:]
                mergeSort(lefthalf)
                mergeSort(righthalf)
                i = j = k = 0
                while i < len(lefthalf) and j < len(righthalf):
                    if lefthalf[i] < righthalf[j]:
                        nlist[k] = lefthalf[i]
                        i = i+1
                    else:
                        nlist[k] = righthalf[j]
                        j = j+1
                    k = k+1
                while i < len(lefthalf):
                    nlist[k] = lefthalf[i]
                    i = i+1
                    k = k+1
                while j < len(righthalf):
                    nlist[k] = righthalf[j]
                    j = j+1
                    k = k+1
            out_list = nlist
            ended = False
            get_memory(memory_usage(), ended)
        mem_diff = []
        time = []
        start = timeit.default_timer()
        mergeSort(lst)
        out_list1 = lst
        list1.insert(END, out_list1)
        end = timeit.default_timer()
        ended = True
        get_memory(memory_usage(), ended)
        time.append(end-start)
        time_sort = (sum(time)/len(time))
        time_entry.insert(INSERT, time_sort)
        t4 = float(time_sort)
        mem_diff = m2
        space_entry.insert(INSERT, mem_diff)
        mem4 = float(mem_diff)
    elif sort_var == "Quick sort":
        def partition(sort_list, low, high):
            i = (low - 1)
            pivot = sort_list[high]
            for j in range(low, high):
                if sort_list[j] <= pivot:
                    i += 1
                    sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
            sort_list[i+1], sort_list[high] = sort_list[high], sort_list[i+1]
            return (i+1)

        def quick_sort(sort_list, low, high):
            if low < high:
                pi = partition(sort_list, low, high)
                quick_sort(sort_list, low, pi-1)
                quick_sort(sort_list, pi+1, high)
            ended = False
            get_memory(memory_usage(), ended)
        mem_diff = []
        time = []
        start = timeit.default_timer()
        low = 0
        high = len(lst) - 1
        quick_sort(lst, low, high)
        out_list = lst
        list1.insert(END, out_list)
        end = timeit.default_timer()
        ended = True
        get_memory(memory_usage(), ended)
        time.append(end-start)
        time_sort = (sum(time)/len(time))
        time_entry.insert(INSERT, time_sort)
        t5 = float(time_sort)
        mem_diff = m2
        space_entry.insert(INSERT, mem_diff)
        mem5 = float(mem_diff)


root = Tk()
root.resizable(FALSE, FALSE)
root.title("COMPARISON OF SORTING TECHNIQUES")

heading_name = Label(root, text="SORTING TECHNIQUES", font="Arial 18 bold")
heading_name.grid(row=1, column=0, columnspan=18, rowspan=3, sticky=N)
select_name = Label(root, text="CHOOSE THE SORTING TECHNIQUIES: ")
select_name.grid(row=5, column=1, sticky=W)
# combo box
sorting_name = StringVar()
new_combobox = Combobox(root, width=16, state="readonly",
                        textvariable=sorting_name)
new_combobox["values"] = ("Bubble Sort", "Insertion Sort",
                          "Selection Sort", "Merge Sort", "Quick sort")
new_combobox.current(0)
new_combobox.grid(row=5, column=2, sticky=W)
new_submit = Button(root, text="SUBMIT", bd=4, command=call_me)
new_submit.grid(row=5, column=3, sticky=W)
enter_size = Label(
    root, text="ENTER THE NUMBER OF ELEMENT(UNDER 1 TO 30000): ")
enter_size.grid(row=6, column=1, sticky=W)
# entry box
size_var = IntVar()
size_entry = Entry(root, width=18, textvariable=size_var, bd=4)
size_entry.grid(row=6, column=2, sticky=W)
size_entry.delete(0, 'end')
size_entry.config(state=DISABLED)
new_submit2 = Button(root, text="SUBMIT", bd=4, command=button_click2)
new_submit2.grid(row=6, column=3, sticky=W)
new_submit2.config(state=DISABLED)
new_submit3 = Button(root, text="ENTER THE VALUES",
                     bd=4, command=button_click3)
new_submit3.grid(row=7, column=1, columnspan=2, sticky=N)
new_submit3.config(state=DISABLED)
new_submit4 = Button(root, text="SORT THESE ELEMENTS",
                     bd=4, command=button_click4)
new_submit4.grid(row=11, column=1, columnspan=3, sticky=N)
new_submit4.config(state=DISABLED)
sort_element = Label(root, text="THE SORTED ELEMENTS ARE  : ")
sort_element.grid(row=13, column=1, sticky=W)
list1 = Listbox(root, height=6, width=35, bd=4)
list1.grid(row=14, column=1, rowspan=6, columnspan=4)
sb1 = Scrollbar(root, orient=HORIZONTAL)
sb1.grid(row=20, column=1, columnspan=4, sticky=S)
list1.configure(xscrollcommand=sb1.set)
sb1.configure(command=list1.xview)
time_element = Label(root, text="TIME COMPLEXITY OF SORTING : ")
time_element.grid(row=23, column=1, sticky=W)
# entry box
time_entry = Entry(root, width=28, bd=4)
time_entry.grid(row=23, column=2, columnspan=2, sticky=W)
time_entry.config(state=DISABLED)
space_element = Label(root, text="SPACE COMPLEXITY OF SORTING : ")
space_element.grid(row=24, column=1, sticky=W)
# entry box
space_entry = Entry(root, width=28, bd=4)
space_entry.grid(row=24, column=2, columnspan=2, sticky=W)
space_entry.config(state=DISABLED)
select_name = Label(root, text="SORTING ALGORITHM : ")
select_name.grid(row=5, column=9, sticky=W, columnspan=5)
list2 = Listbox(root, height=18, width=45, bd=5)
list2.grid(row=6, column=9, rowspan=20, columnspan=8)
sb2 = Scrollbar(root)
sb3 = Scrollbar(root, orient=HORIZONTAL)
sb2.grid(row=8, column=18, rowspan=9)
sb3.grid(row=27, column=9, columnspan=8)
list2.configure(yscrollcommand=sb2.set)
sb2.configure(command=list2.yview)
list2.configure(xscrollcommand=sb3.set)
sb3.configure(command=list2.xview)
# matplotlib


def button_click5():
    if (full_com == 1):
        def openwindow():
            if (not(t1 == 0) and not(t2 == 0)):
                sorting = ["Bubble Sort", "Insertion Sort"]
                time_complexity = [float(t1), float(t2)]
                plt.plot(sorting, time_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Time(in mili second)')
                plt.title("Time Comparison of Sorting Technique")
                plt.show()
            elif (not(t2 == 0) and not(t3 == 0)):
                sorting = ["Insertion Sort", "Selection Sort"]
                time_complexity = [float(t2), float(t3)]
                plt.plot(sorting, time_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Time(in mili second)')
                plt.title("Time Comparison of Sorting Technique")
                plt.show()
            elif (not(t3 == 0) and not(t4 == 0)):
                sorting = ["Selection Sort", "Merge Sort"]
                time_complexity = [float(t3), float(t4)]
                plt.plot(sorting, time_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Time(in mili second)')
                plt.title("Time Comparison of Sorting Technique")
                plt.show()
            elif (not(t4 == 0) and not(t5 == 0)):
                sorting = ["Merge Sort", "Quick Sort"]
                time_complexity = [float(t4), float(t5)]
                plt.plot(sorting, time_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Time(in mili second)')
                plt.title("Time Comparison of Sorting Technique")
                plt.show()
            elif (not (t1 == 0) and not(t3 == 0)):
                sorting = ["Bubble Sort", "Selection Sort"]
                time_complexity = [float(t1), float(t3)]
                plt.plot(sorting, time_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Time(in mili second)')
                plt.title("Time Comparison of Sorting Technique")
                plt.show()
            elif (not(t1 == 0) and not(t4 == 0)):
                sorting = ["Bubble Sort", "Merge Sort"]
                time_complexity = [float(t1), float(t4)]
                plt.plot(sorting, time_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Time(in mili second)')
                plt.title("Time Comparison of Sorting Technique")
                plt.show()
            elif (not(t1 == 0) and not(t5 == 0)):
                sorting = ["Bubble Sort", "Quick Sort"]
                time_complexity = [float(t1), float(t5)]
                plt.plot(sorting, time_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Time(in mili second)')
                plt.title("Time Comparison of Sorting Technique")
                plt.show()
            elif (not(t2 == 0) and not(t4 == 0)):
                sorting = ["Insertion Sort", "Merge Sort"]
                time_complexity = [float(t2), float(t4)]
                plt.plot(sorting, time_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Time(in mili second)')
                plt.title("Time Comparison of Sorting Technique")
                plt.show()
            elif (not(t2 == 0) and not(t5 == 0)):
                sorting = ["Insertion Sort", "Quick Sort"]
                time_complexity = [float(t2), float(t5)]
                plt.plot(sorting, time_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Time(in mili second)')
                plt.title("Time Comparison of Sorting Technique")
                plt.show()
            elif (not(t3 == 0) and not(t5 == 0)):
                sorting = ["Selection Sort", "Quick Sort"]
                time_complexity = [float(t3), float(t5)]
                plt.plot(sorting, time_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Time(in mili second)')
                plt.title("Time Comparison of Sorting Technique")
                plt.show()

        def openwindow2():
            if (not(mem1 == 0) and not(mem2 == 0)):
                sorting = ["Bubble Sort", "Insertion Sort"]
                space_complexity = [float(mem1), float(mem2)]
                plt.plot(sorting, space_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Space(in mb)')
                plt.title("space Comparison of Sorting Technique")
                plt.show()
            elif (not(mem1 == 0) and not(mem3 == 0)):
                sorting = ["Bubble Sort", "Selection Sort"]
                space_complexity = [float(mem1), float(mem3)]
                plt.plot(sorting, space_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Space(in mb)')
                plt.title("space Comparison of Sorting Technique")
                plt.show()
            elif (not(mem1 == 0) and not(mem4 == 0)):
                sorting = ["Bubble Sort", "Merge Sort"]
                space_complexity = [float(mem1), float(mem4)]
                plt.plot(sorting, space_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Space(in mb)')
                plt.title("space Comparison of Sorting Technique")
                plt.show()
            elif (not(mem1 == 0) and not(mem5 == 0)):
                sorting = ["Bubble Sort", "Quick Sort"]
                space_complexity = [float(mem1), float(mem5)]
                plt.plot(sorting, space_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Space(in mb)')
                plt.title("space Comparison of Sorting Technique")
                plt.show()
            elif (not(mem2 == 0) and not(mem3 == 0)):
                sorting = ["Insertion Sort", "Selection Sort"]
                space_complexity = [float(mem2), float(mem3)]
                plt.plot(sorting, space_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Space(in mb)')
                plt.title("space Comparison of Sorting Technique")
                plt.show()
            elif (not(mem2 == 0) and not(mem4 == 0)):
                sorting = ["Insertion Sort", "Merge Sort"]
                space_complexity = [float(mem2), float(mem4)]
                plt.plot(sorting, space_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Space(in mb)')
                plt.title("space Comparison of Sorting Technique")
                plt.show()
            elif (not(mem2 == 0) and not(mem5 == 0)):
                sorting = ["Insertion Sort", "Quick Sort"]
                space_complexity = [float(mem2), float(mem5)]
                plt.plot(sorting, space_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Space(in mb)')
                plt.title("space Comparison of Sorting Technique")
                plt.show()
            elif (not(mem3 == 0) and not(mem4 == 0)):
                sorting = ["Selection Sort", "Merge Sort"]
                space_complexity = [float(mem3), float(mem4)]
                plt.plot(sorting, space_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Space(in mb)')
                plt.title("space Comparison of Sorting Technique")
                plt.show()
            elif (not(mem3 == 0) and not(mem5 == 0)):
                sorting = ["Selection Sort", "Quick Sort"]
                space_complexity = [float(mem3), float(mem5)]
                plt.plot(sorting, space_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Space(in mb)')
                plt.title("space Comparison of Sorting Technique")
                plt.show()
            elif (not (mem4 == 0) and not(mem5 == 0)):
                sorting = ["Merge Sort", "Quick Sort"]
                space_complexity = [float(mem4), float(mem5)]
                plt.plot(sorting, space_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Space(in mb)')
                plt.title("space Comparison of Sorting Technique")
                plt.show()
        top = Toplevel()
        top.title("GRAPH COMPARISON")
        top.geometry("300x200")
        button1 = Button(top, text="TIME COMPLEXITY", command=openwindow)
        button1.pack()
        button2 = Button(top, text="SPACE COMPLEXITY", command=openwindow2)
        button2.pack()
    elif (full_com == 2):
        def openwindow():
            if (not(t1 == 0) and not (t2 == 0) and not(t3 == 0)):
                sorting = ["Bubble Sort", "Insertion Sort", "Selection Sort"]
                time_complexity = [float(t1), float(t2), float(t3)]
                plt.plot(sorting, time_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Time(in mili second)')
                plt.title("Time Comparison of Sorting Technique")
                plt.show()
            elif (not(t1 == 0) and not (t4 == 0) and not (t5 == 0)):
                sorting = ["Bubble Sort", "Merge Sort", "Quick Sort"]
                time_complexity = [float(t1), float(t4), float(t5)]
                plt.plot(sorting, time_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Time(in mili second)')
                plt.title("Time Comparison of Sorting Technique")
                plt.show()
            elif (not(t1 == 0) and not (t2 == 0) and not (t4 == 0)):
                sorting = ["Bubble Sort", "Insertion Sort", "Merge Sort"]
                time_complexity = [float(t1), float(t2), float(t4)]
                plt.plot(sorting, time_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Time(in mili second)')
                plt.title("Time Comparison of Sorting Technique")
                plt.show()
            elif (not(t1 == 0) and not (t2 == 0) and not (t5 == 0)):
                sorting = ["Bubble Sort", "Insertion Sort", "Quick Sort"]
                time_complexity = [float(t1), float(t2), float(t5)]
                plt.plot(sorting, time_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Time(in mili second)')
                plt.title("Time Comparison of Sorting Technique")
                plt.show()
            elif (not(t1 == 0) and not(t3 == 0) and not (t4 == 0)):
                sorting = ["Bubble Sort", "Selection Sort", "Merge Sort"]
                time_complexity = [float(t1), float(t3), float(t4)]
                plt.plot(sorting, time_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Time(in mili second)')
                plt.title("Time Comparison of Sorting Technique")
                plt.show()
            elif (not(t1 == 0) and not(t3 == 0) and not (t5 == 0)):
                sorting = ["Bubble Sort", "Selection Sort", "Quick Sort"]
                time_complexity = [float(t1), float(t3), float(t5)]
                plt.plot(sorting, time_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Time(in mili second)')
                plt.title("Time Comparison of Sorting Technique")
                plt.show()
            elif (not (t2 == 0) and not(t3 == 0) and not (t4 == 0)):
                sorting = ["Insertion Sort", "Selection Sort", "Merge Sort"]
                time_complexity = [float(t2), float(t3), float(t5)]
                plt.plot(sorting, time_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Time(in mili second)')
                plt.title("Time Comparison of Sorting Technique")
                plt.show()
            elif (not (t2 == 0) and not(t3 == 0) and not (t5 == 0)):
                sorting = ["Insertion Sort", "Selection Sort", "Quick Sort"]
                time_complexity = [float(t2), float(t3), float(t5)]
                plt.plot(sorting, time_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Time(in mili second)')
                plt.title("Time Comparison of Sorting Technique")
                plt.show()
            elif (not (t2 == 0) and not (t4 == 0) and not (t5 == 0)):
                sorting = ["Insertion Sort", "Merge Sort", "Quick Sort"]
                time_complexity = [float(t2), float(t4), float(t5)]
                plt.plot(sorting, time_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Time(in mili second)')
                plt.title("Time Comparison of Sorting Technique")
                plt.show()
            elif (not(t3 == 0) and not (t4 == 0) and not (t5 == 0)):
                sorting = ["Selection Sort", "Merge Sort", "Quick Sort"]
                time_complexity = [float(t3), float(t4), float(t5)]
                plt.plot(sorting, time_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Time(in mili second)')
                plt.title("Time Comparison of Sorting Technique")
                plt.show()

        def openwindow2():
            if (not(mem1 == 0) and not (mem2 == 0) and not(mem3 == 0)):
                sorting = ["Bubble Sort", "Insertion Sort", "Selection Sort"]
                space_complexity = [float(mem1), float(mem2), float(mem3)]
                plt.plot(sorting, space_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Space(in mb)')
                plt.title("space Comparison of Sorting Technique")
                plt.show()
            elif (not(mem1 == 0) and not (mem2 == 0) and not (mem4 == 0)):
                sorting = ["Bubble Sort", "Insertion Sort", "Merge Sort"]
                space_complexity = [float(mem1), float(mem2), float(mem4)]
                plt.plot(sorting, space_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Space(in mb)')
                plt.title("space Comparison of Sorting Technique")
                plt.show()
            elif (not(mem1 == 0) and not (mem2 == 0) and not (mem5 == 0)):
                sorting = ["Bubble Sort", "Insertion Sort", "Quick Sort"]
                space_complexity = [float(mem1), float(mem2), float(mem5)]
                plt.plot(sorting, space_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Space(in mb)')
                plt.title("space Comparison of Sorting Technique")
                plt.show()
            elif (not(mem1 == 0) and not(mem3 == 0) and not (mem4 == 0)):
                sorting = ["Bubble Sort", "Selection Sort", "Merge Sort"]
                space_complexity = [float(mem1), float(mem3), float(mem4)]
                plt.plot(sorting, space_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Space(in mb)')
                plt.title("space Comparison of Sorting Technique")
                plt.show()
            elif (not(mem1 == 0) and not(mem3 == 0) and not (mem5 == 0)):
                sorting = ["Bubble Sort", "Selection Sort", "Quick Sort"]
                space_complexity = [float(mem1), float(mem3), float(mem5)]
                plt.plot(sorting, space_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Space(in mb)')
                plt.title("space Comparison of Sorting Technique")
                plt.show()
            elif (not(mem1 == 0) and not (mem4 == 0) and not (mem5 == 0)):
                sorting = ["Bubble Sort", "Merge Sort", "Quick Sort"]
                space_complexity = [float(mem1), float(mem4), float(mem5)]
                plt.plot(sorting, space_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Space(in mb)')
                plt.title("space Comparison of Sorting Technique")
                plt.show()
            elif (not (mem2 == 0) and not(mem3 == 0) and not (mem4 == 0)):
                sorting = ["Insertion Sort", "Selection Sort", "Merge Sort"]
                space_complexity = [float(mem2), float(mem3), float(mem4)]
                plt.plot(sorting, space_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Space(in mb)')
                plt.title("space Comparison of Sorting Technique")
                plt.show()
            elif (not (mem2 == 0) and not(mem3 == 0) and not (mem5 == 0)):
                sorting = ["Insertion Sort", "Selection Sort", "Quick Sort"]
                space_complexity = [float(mem2), float(mem3), float(mem5)]
                plt.plot(sorting, space_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Space(in mb)')
                plt.title("space Comparison of Sorting Technique")
                plt.show()
            elif (not (mem2 == 0) and not (mem4 == 0) and not (mem5 == 0)):
                sorting = ["Insertion Sort", "Merge Sort", "Quick Sort"]
                space_complexity = [float(mem2), float(mem4), float(mem5)]
                plt.plot(sorting, space_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Space(in mb)')
                plt.title("space Comparison of Sorting Technique")
                plt.show()
            elif (not(mem3 == 0) and not (mem4 == 0) and not (mem5 == 0)):
                sorting = ["Selection Sort", "Merge Sort", "Quick Sort"]
                space_complexity = [float(mem3), float(mem4), float(mem5)]
                plt.plot(sorting, space_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Space(in mb)')
                plt.title("space Comparison of Sorting Technique")
                plt.show()
        top = Toplevel()
        top.title("GRAPH COMPARISON")
        top.geometry("300x200")
        button1 = Button(top, text="TIME COMPLEXITY", command=openwindow)
        button1.pack()
        button2 = Button(top, text="SPACE COMPLEXITY", command=openwindow2)
        button2.pack()
    elif (full_com == 3):
        def openwindow():
            if (not(t1 == 0) and not (t2 == 0) and not(t3 == 0) and not (t4 == 0)):
                sorting = ["Bubble Sort", "Insertion Sort",
                           "Selection Sort", "Merge Sort"]
                time_complexity = [float(t1), float(t2), float(t3), float(t4)]
                plt.plot(sorting, time_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Time(in mili second)')
                plt.title("Time Comparison of Sorting Technique")
                plt.show()
            elif (not(t1 == 0) and not (t2 == 0) and not(t3 == 0) and not (t5 == 0)):
                sorting = ["Bubble Sort", "Insertion Sort",
                           "Selection Sort", "Quick Sort"]
                time_complexity = [float(t1), float(t2), float(t3), float(t5)]
                plt.plot(sorting, time_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Time(in mili second)')
                plt.title("Time Comparison of Sorting Technique")
                plt.show()
            elif (not(t1 == 0) and not(t3 == 0) and not (t4 == 0) and not (t5 == 0)):
                sorting = ["Bubble Sort", "Selection Sort",
                           "Merge Sort", "Quick Sort"]
                time_complexity = [float(t1), float(t3), float(t4), float(t5)]
                plt.plot(sorting, time_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Time(in mili second)')
                plt.title("Time Comparison of Sorting Technique")
                plt.show()
            elif (not (t2 == 0) and not(t3 == 0) and not (t4 == 0) and not (t5 == 0)):
                sorting = ["Insertion Sort", "Selection Sort",
                           "Merge Sort", "Quick Sort"]
                time_complexity = [float(t2), float(t3), float(t4), float(t5)]
                plt.plot(sorting, time_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Time(in mili second)')
                plt.title("Time Comparison of Sorting Technique")
                plt.show()

        def openwindow2():
            if (not(mem1 == 0) and not (mem2 == 0) and not(mem3 == 0) and not (mem4 == 0)):
                sorting = ["Bubble Sort", "Insertion Sort",
                           "Selection Sort", "Merge Sort"]
                space_complexity = [float(mem1), float(
                    mem2), float(mem3), float(mem4)]
                plt.plot(sorting, space_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Space(in mb)')
                plt.title("space Comparison of Sorting Technique")
                plt.show()
            elif (not(mem1 == 0) and not (mem2 == 0) and not(mem3 == 0) and not (mem5 == 0)):
                sorting = ["Bubble Sort", "Insertion Sort",
                           "Selection Sort", "Quick Sort"]
                space_complexity = [float(mem1), float(
                    mem2), float(mem3), float(mem5)]
                plt.plot(sorting, space_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Space(in mb)')
                plt.title("space Comparison of Sorting Technique")
                plt.show()
            elif (not(mem1 == 0) and not (mem2 == 0) and not (mem4 == 0) and not (mem5 == 0)):
                sorting = ["Bubble Sort", "Insertion Sort",
                           "Merge Sort", "Quick Sort"]
                space_complexity = [float(mem1), float(
                    mem2), float(mem4), float(mem5)]
                plt.plot(sorting, space_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Space(in mb)')
                plt.title("space Comparison of Sorting Technique")
                plt.show()
            elif (not(mem1 == 0) and not(mem3 == 0) and not (mem4 == 0) and not (mem5 == 0)):
                sorting = ["Bubble Sort", "Selection Sort",
                           "Merge Sort", "Quick Sort"]
                space_complexity = [float(mem1), float(
                    mem3), float(mem4), float(mem5)]
                plt.plot(sorting, space_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Space(in mb)')
                plt.title("space Comparison of Sorting Technique")
                plt.show()
            elif (not (mem2 == 0) and not(mem3 == 0) and not (mem4 == 0) and not (mem5 == 0)):
                sorting = ["Insertion Sort", "Selection Sort",
                           "Merge Sort", "Quick Sort"]
                space_complexity = [float(mem2), float(
                    mem3), float(mem4), float(mem5)]
                plt.plot(sorting, space_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Space(in mb)')
                plt.title("space Comparison of Sorting Technique")
                plt.show()
        top = Toplevel()
        top.title("GRAPH COMPARISON")
        top.geometry("300x200")
        button1 = Button(top, text="TIME COMPLEXITY", command=openwindow)
        button1.pack()
        button2 = Button(top, text="SPACE COMPLEXITY", command=openwindow2)
        button2.pack()
    elif (full_com == 4):
        def openwindow():
            if (not(t1 == 0) and not (t2 == 0) and not(t3 == 0) and not (t4 == 0) and not (t5 == 0)):
                sorting = ["Bubble Sort", "Insertion Sort",
                           "Selection Sort", "Merge Sort", "Quick Sort"]
                time_complexity = [float(t1), float(
                    t2), float(t3), float(t4), float(t5)]
                plt.plot(sorting, time_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Time(in mili second)')
                plt.title("Time Comparison of Sorting Technique")
                plt.show()
            else:
                messagebox.showerror(
                    "Error", "Please choose all sorting techniques")

        def openwindow2():
            if (not(mem1 == 0) and not (mem2 == 0) and not(mem3 == 0) and not (mem4 == 0) and not (mem5 == 0)):
                sorting = ["Bubble Sort", "Insertion Sort",
                           "Selection Sort", "Merge Sort", "Quick Sort"]
                space_complexity = [float(mem1), float(
                    mem2), float(mem3), float(mem4), float(mem5)]
                plt.plot(sorting, space_complexity)
                plt.xlabel('Sorting')
                plt.ylabel('Space(in mb)')
                plt.title("space Comparison of Sorting Technique")
                plt.show()
        top = Toplevel()
        top.title("GRAPH COMPARISON")
        top.geometry("300x200")
        button1 = Button(top, text="TIME COMPLEXITY", command=openwindow)
        button1.pack()
        button2 = Button(top, text="SPACE COMPLEXITY", command=openwindow2)
        button2.pack()


new_submit5 = Button(root, text="GRAPH COMPARISON",
                     bd=4, command=button_click5)
new_submit5.grid(row=27, column=2, columnspan=2, sticky=W)
new_submit5.config(state=DISABLED)
new_submit6 = Button(root, text="COMPARISON", bd=4, command=button_click6)
new_submit6.grid(row=27, column=1, sticky=N)
new_submit6.config(state=DISABLED)


def button_click7():
    global oper
    global full_com
    full_com = 0
    oper = 0
    new_combobox.set('')
    new_combobox.config(state=NORMAL)
    new_submit.config(state=NORMAL)
    list2.delete(0, END)
    list1.delete(0, END)
    time_entry.delete(0, 'end')
    size_entry.config(state=NORMAL)
    size_entry.delete(0, 'end')
    space_entry.delete(0, 'end')
    space_entry.config(state=DISABLED)
    time_entry.config(state=DISABLED)
    size_entry.config(state=DISABLED)
    new_submit2.config(state=DISABLED)
    new_submit3.config(state=DISABLED)
    new_submit4.config(state=DISABLED)
    new_submit5.config(state=DISABLED)
    new_submit6.config(state=DISABLED)
    new_submit7.config(state=DISABLED)


new_submit7 = Button(root, text="RESET", bd=4, command=button_click7)
new_submit7.grid(row=27, column=5, sticky=W)
new_submit7.config(state=DISABLED)
root.mainloop()
