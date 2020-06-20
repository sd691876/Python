from Conversion import Bin2Dec,Dec2Bin,Dec2Hex,Hex2Dec,Oct2Dec,Dec2Oct
from bs import Bubble_sort
#Problem 3
print('二進位轉十進位:',Bin2Dec('10101010'))
print('十進位轉二進位:',Dec2Bin(170))
print('八進位轉十進位:',Oct2Dec('252'))
print('十進位轉八進位:',Dec2Oct(170))
print('十進位轉十六進位:',Dec2Hex(170))
print('十六進位轉十進位:',Hex2Dec('AA'))
print('十六進位轉二進位:',Dec2Bin(Hex2Dec('AA')))
print('二進位轉十六進位:',Dec2Hex(Bin2Dec('10101010')))

#Problem 4
number = [int(num) for  num in input('Enter numbers: ').split(" ")]
Bubble_sort(number)
