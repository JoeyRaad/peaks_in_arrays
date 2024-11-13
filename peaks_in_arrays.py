def find_peaks(array):

    #list to store all peaks and another one to get length of array
    peaks, n = [], len(array)
    
    #check for edge cases
    if not array:
        return 0
    #check for logical cases
    if n<3:
        return 0
    
    #aim is to start from 2nd and end at before last number cuz peak only occurs between 2 numbers
    for i in range(len(array)):

        if array[i]>array[i-1] and array[i]>array[i+1]:
            peaks.append(i)

    return peaks

array = [1, 4, 2, 7, 4, 6, 2]
print(find_peaks(array))


