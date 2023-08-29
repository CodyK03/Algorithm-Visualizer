import pygame
import math
import time
import random

pygame.init()
pygame.display.set_caption("Sorting Algorithm Visualizer")

class guiInfoClass:
    #Create fonts
    bodyFont = pygame.font.SysFont('times new roman', 20)
    headerFont = pygame.font.SysFont('times new roman', 40)

    #Create possible colors for sorting rectangles
    grayVariations = [
		(160, 160, 160),
		(192, 192, 192),
		(255, 255, 255),
	]

    #Set padding for sorting rectangles
    padding = 150

    #Initialize sorting rectangles
    def __init__(self, width, height, list):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        self.createList(list)
    
    #Set up sorting rectangles
    def createList(self, list):
        self.list = list
        self.min = min(list)
        self.max = max(list)

        self.rectWidth = math.floor((self.width) / len(list))
        self.rectHeight = math.floor((self.height - self.padding) / (self.max - self.min))

def makeBackground(drawInfo, algo_name):
    #Set Background Color
    drawInfo.window.fill((0, 0, 0))

    #Create background boxes
    titleBackground = pygame.Rect(0, 0, drawInfo.width, 70)
    pygame.draw.rect(drawInfo.window, (60, 60, 60), titleBackground)
    instructionBackground = pygame.Rect(0, 70, drawInfo.width, 80)
    pygame.draw.rect(drawInfo.window, (75, 75, 75), instructionBackground)

    #Display Title
    title = drawInfo.headerFont.render("Algorithm Visualizer: " + algo_name, 1, (255, 165, 0))
    drawInfo.window.blit(title, (drawInfo.width/2 - title.get_width()/2 , 5))


    #Display Instructions
    topInstruct = drawInfo.bodyFont.render("C: Clear, Space Bar: Start Sorting, B: Bubble Sort, I: Insertion Sort", 1, (255, 255, 255))
    bottomInstruct = drawInfo.bodyFont.render("S: Selection Sort, M: Merge Sort, Q: Quick Sort, H: Heap Sort, R: Radix Sort", 1, (255, 255, 255))
    drawInfo.window.blit(topInstruct, (drawInfo.width/2 - topInstruct.get_width()/2 , 85))
    drawInfo.window.blit(bottomInstruct, (drawInfo.width/2 - bottomInstruct.get_width()/2 , 120))


    makeRectangleList(drawInfo)
    
    pygame.display.update()


def makeRectangleList(drawInfo, clear=False):
    #Take list from drawInfo
    list = drawInfo.list

    #Slow the speed of the blocks showing up
    time.sleep(.01)

    #Clear the previous rectangle before drawing a new one
    if clear:
        clear_rect = (0, drawInfo.padding, drawInfo.width, drawInfo.height - drawInfo.padding)
        pygame.draw.rect(drawInfo.window, (0, 0, 0), clear_rect)

    #Iterate through each value
    for i in range(len(list)):

        #Setting the coords for each rectangle to start drawing from
        x = i * drawInfo.rectWidth
        y = drawInfo.height - (list[i] - drawInfo.min) * drawInfo.rectHeight

        #Setting the color for each rectangle
        color = drawInfo.grayVariations[i % 3]

        #Drawing the rectangle
        pygame.draw.rect(drawInfo.window, color, (x, y, drawInfo.rectWidth, drawInfo.height))

    if clear:
        pygame.display.update()


def generateValueList(n, min, max):
	list = []
        
	for i in range(n):
        #Get a random number between the min and max and add it to the list
		num = random.randint(min, max)
		list.append(num)

	return list


def bubbleSort(drawInfo):
    list = drawInfo.list
    #loop through list
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            #if element j is greater than the next then swap them
            if list[j] > list[j+1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                #redraw rectangles accordingly
                makeRectangleList(drawInfo, True)


def selectionSort(drawInfo):
    list = drawInfo.list
    #iterate through list
    for i in range(len(list)):
        min_index = i
        for j in range(i+1, len(list)):
            #reselect min element after each iteration
            if (list[j] < list[min_index]):
                min_index = j
        #swap elements
        list[i], list[min_index] = list[min_index], list[i]
        #redraw rectangles accordingly
        makeRectangleList(drawInfo, True)


def insertionSort(drawInfo):
    list = drawInfo.list
    
    #iterate through list
    for i in range(1, len(list)):
        current = list[i]
        #loop until an element is found that is smaller than current
        while i > 0 and list[i-1] > current:
            #shift elements to the right
            list[i] = list[i - 1]
            i = i - 1
            #move current into the element smaller than it
            list[i] = current
            #redraw rectangles accordingly
            makeRectangleList(drawInfo, True)

def quickSort(drawInfo):
    list = drawInfo.list

    l = 0
    h = len(list) - 1

    size = h
    stack = [0] * (size)
    
    top = -1
    #push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
    
    #While not empty, continue popping from stack
    while top >= 0:
        #Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
    
        i = ( l - 1 )
        x = list[h]
        
        for j in range(l, h):
            if list[j] <= x:
                #increment the index of the smaller element and swap
                i = i + 1
                list[i], list[j] = list[j], list[i]
                #redraw rectangles accordingly
                makeRectangleList(drawInfo, True)

        #swap values
        list[i + 1], list[h] = list[h], list[i + 1]
        #redraw rectangles accordingly
        makeRectangleList(drawInfo, True)

        p = (i + 1)
        #If elements on left of pivot then push left side onto stack
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
	    #If elements on right of pivot, push right side onto stack
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


def mergeSort(drawInfo):
    list = drawInfo.list

    width = 1   
    n = len(list)                                         
    while (width < n):
        l=0
        while (l < n):
            #Merge two halves of the array
            r = min(l+(width*2-1), n-1)        
            m = min(l+width-1,n-1)          
            n1 = m - l + 1
            n2 = r - m
            L = [0] * n1
            R = [0] * n2

            #Copy data to temp arrays
            for i in range(0, n1):
                L[i] = list[l + i]
            for i in range(0, n2):
                R[i] = list[m + i + 1]

            #Merging temp arrays back into list
            i, j, k = 0, 0, l
            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    list[k] = L[i]
                    makeRectangleList(drawInfo, True)
                    i += 1
                else:
                    list[k] = R[j]
                    makeRectangleList(drawInfo, True)
                    j += 1
                k += 1
            #Copy remaining L elements
            while i < n1:
                list[k] = L[i]
                makeRectangleList(drawInfo, True)
                i += 1
                k += 1
            #Copy remaining R elements
            while j < n2:
                list[k] = R[j]
                makeRectangleList(drawInfo, True)
                j += 1
                k += 1
            l += width*2
        width *= 2

def heapSort(drawInfo):
    list = drawInfo.list
    n = len(list)
    for i in range(n):
        #if child is bigger than parent
        if list[i] > list[int((i - 1) / 2)]:
            j = i
            #swap child until parent is bigger
            while list[j] > list[int((j - 1) / 2)]:
                (list[j], list[int((j - 1) / 2)]) = (list[int((j - 1) / 2)], list[j])
                #Update rectangles accordingly
                makeRectangleList(drawInfo, True)
                j = int((j - 1) / 2)
 
    for i in range(n - 1, 0, -1):
        #swap first element with last
        list[0], list[i] = list[i], list[0]
        #update rectangles accordingly
        makeRectangleList(drawInfo, True)
        j, index = 0, 0
         
        while True:
            index = 2 * j + 1
            
            #if left child is smaller than right, point index to right
            if (index < (i - 1) and list[index] < list[index + 1]):
                index += 1
            #if parent is smaller than child, swap parent with child
            if index < i and list[j] < list[index]:
                list[j], list[index] = list[index], list[j]
                #update rectangles accordingly
                makeRectangleList(drawInfo, True)
         
            j = index
            if index >= i:
                break

def radixSort(drawInfo):
    list = drawInfo.list

    #find max num
    max1 = max(list)
 
    exp = 1
    #Count for each number
    while max1 // exp > 0:
        n = len(list)
        output = [0] * (n)
        count = [0] * (10)
        
        #store num of occurences in count
        for i in range(0, n):
            index = (list[i]/exp)
            count[int((index)%10)] += 1
        for i in range(1,10):
            count[i] += count[i-1]

        #make output array
        i = n-1
        while i>=0:
            index = (list[i]/exp)
            output[count[int((index)%10)] - 1] = list[i]
            count[int((index)%10)] -= 1
            i -= 1
        #copy output array to list
        i = 0
        for i in range(0,len(list)):
            list[i] = output[i]
            makeRectangleList(drawInfo, True)
        exp *= 10


def main():
    exit = False

    n = 50
    min = 0
    max = 100

    list = generateValueList(n, min, max)
    drawInfo = guiInfoClass(800, 600, list)
    sorting = False

    algorithm = bubbleSort
    algoName = "Bubble Sort"

    while not exit:

        makeBackground(drawInfo, algoName)

        for event in pygame.event.get():

            #Exit while loop when user attempts to close program
            if event.type == pygame.QUIT:
                exit = True

            #Keep looping if no key was pressed
            if event.type != pygame.KEYDOWN:
                continue

            #Selecting sorting algorithm/action based off of key pressed
            if event.key == pygame.K_c:
                list = generateValueList(n, min, max)
                drawInfo.createList(list)
                sorting = False
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                algorithm(drawInfo)
            elif event.key == pygame.K_i and not sorting:
                algorithm = insertionSort
                algoName = "Insertion Sort"
            elif event.key == pygame.K_b and not sorting:
                algorithm = bubbleSort
                algoName = "Bubble Sort"
            elif event.key == pygame.K_s and not sorting:
                algorithm = selectionSort
                algoName = "Selection Sort"
            elif event.key == pygame.K_q and not sorting:
                algorithm = quickSort
                algoName = "Quick Sort"
            elif event.key == pygame.K_m and not sorting:
                algorithm = mergeSort
                algoName = "Merge Sort"
            elif event.key == pygame.K_h and not sorting:
                algorithm = heapSort
                algoName = "Heap Sort"
            elif event.key == pygame.K_r and not sorting:
                algorithm = radixSort
                algoName = "Radix Sort"
            
    pygame.quit()


if __name__ == "__main__":
	main()