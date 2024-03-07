def sorting_selection(input_list, filehandler = None):
    for idx in range(len(input_list)):
        min_idx = idx
        for j in range(idx + 1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
                
        if filehandler != None:
            input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]
            filehandler[idx], filehandler[min_idx] = filehandler[min_idx], filehandler[idx]
        else:    
            input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]
        
    return input_list, filehandler
    
def splitFiles(data, size):
    pos = 0
    tempBuffer = []
    filename_list = []
    for i in range(1,len(data)+1):
        tempBuffer.append(int(data[i-1]))
        if i % size == 0:
            pos += 1
            sorting_selection(tempBuffer)
            for i in range(len(tempBuffer)):
                tempBuffer[i] = str(tempBuffer[i])
                tempBuffer[i] = tempBuffer[i]+'\n'
            filename = "tempFile" + str(pos) 
            f = open(filename, "w+")
            f.writelines(tempBuffer)
            filename_list.append(filename)
            tempBuffer = []
    
    return filename_list

def handleFile(namafile):
    f = open(namafile, "r+")
    data = f.readlines()
    data.pop(0)
    f.close()
    
    f = open(namafile, "w+")
    f.writelines(data)
    f.close() 

def mergeSortedFile(filename_list,output_file, size):
    sorted_output = []
    filehandler = []
    tmp_sorted = []
    filename = ""
    i = 0
    sorted_file = open(output_file, 'w+')
    while len(sorted_output) < (size+1):
        if i < 10:
            f = open(filename_list[i], "r+")
            number = f.readline()
            filehandler.append(filename_list[i])
            number = int(number)
            tmp_sorted.append(number)
        else:
            tmp_sorted, filehandler = sorting_selection(tmp_sorted, filehandler)
            if tmp_sorted == []:
                break
            else:
                sorted_output.append(tmp_sorted[0])
                sorted_file.write(str(tmp_sorted[0]) + '\n')
            filename = filehandler[0]
            tmp_sorted.pop(0); filehandler.pop(0);
            
            handleFile(filename)
            
            f = open(filename, "r+")
            number = f.readline()
            if number == '':
                continue
            else:
                number = int(number)
                tmp_sorted.append(number); filehandler.append(filename);
        i += 1
    sorted_file.close()       
    return sorted_output
    
size = 10
filename = 'largefile'
fo = open(filename, "r+")
data = fo.readlines()
filename_list = splitFiles(data, size)
final_sorted = mergeSortedFile(filename_list, 'sortedFile', len(data))
print(final_sorted)