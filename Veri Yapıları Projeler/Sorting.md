
# Verilen dizi: [22, 27, 16, 2, 18, 6]

## Insertion Sort aşamaları:

 *   [22, 27, 16, 2, 18, 6] -> ilk eleman zaten sıralı kabul edilir.
 *   [22, 27, 16, 2, 18, 6] -> 27, 22'den büyük olduğu için yer değiştirilir: [22, 27, 16, 2, 18, 6]
 *   [16, 22, 27, 2, 18, 6] -> 16, 22'den küçük olduğu için yer değiştirilir: [16, 22, 27, 2, 18, 6]
 *   [2, 16, 22, 27, 18, 6] -> 2, 16'dan küçük olduğu için yer değiştirilir: [2, 16, 22, 27, 18, 6]
 *   [2, 16, 18, 22, 27, 6] -> 18, 27'den küçük olduğu için yer değiştirilir: [2, 16, 18, 22, 27, 6]
 *   [2, 6, 16, 18, 22, 27] -> 6, 16'dan küçük olduğu için yer değiştirilir: [2, 6, 16, 18, 22, 27]
Dizi sıralandıktan sonra: [2, 6, 16, 18, 22, 27]

Insertion Sort algoritmasının Big-O gösterimi O(n^2)'dir.



#Time Complexity: Dizi sıralandıktan sonra 18 sayısı aşağıdaki case'lerden hangisinin kapsamına girer? Yazınız

Average case: Aradığımız sayının ortada olması
Worst case: Aradığımız sayının sonda olması
Best case: Aradığımız sayının dizinin en başında olması.


[7,3,5,8,2,9,4,15,6] dizisinin Selection Sort'a göre ilk 4 adımını yazınız.
Dizi sıralandıktan sonra 18 sayısı için Average case kapsamına girer. Bu durumda, dizinin ortasında bir eleman olarak aranan sayının bulunması beklenir.

Selection Sort aşamaları:

 *   [7, 3, 5, 8, 2, 9, 4, 15, 6] -> minimum elemanı bulmak için 2 seçilir ve başa yerleştirilir: [2, 3, 5, 8, 7, 9, 4, 15, 6]
 *   [2, 3, 5, 8, 7, 9, 4, 15, 6] -> minimum elemanı bulmak için 3 seçilir ve 2. sıradaki elemanla yer değiştirilir: [2, 3, 5, 8, 7, 9, 4, 15, 6]
 *   [2, 3, 4, 8, 7, 9, 5, 15, 6] -> minimum elemanı bulmak için 4 seçilir ve 3. sıradaki elemanla yer değiştirilir: [2, 3, 4, 8, 7, 9, 5, 15, 6]
 *   [2, 3, 4, 5, 7, 9, 8, 15, 6] -> minimum elemanı bulmak için 5 seçilir ve 4. sıradaki elemanla yer değiştirilir: [2, 3, 4, 5, 7, 9, 8, 15, 6]
Dizinin ilk 4 adımı sonrasında sırasıyla en küçük 4 eleman yer değiştirmiş oldu ve dizi aşağıdaki hale geldi:

[2, 3, 4, 5, 7, 9, 8, 15, 6]
