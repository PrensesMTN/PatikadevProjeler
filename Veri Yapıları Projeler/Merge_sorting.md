# Verilen dizi: [16, 21, 11, 8, 12, 22]

## Merge Sort aşamaları:

 *   [16, 21, 11, 8, 12, 22] -> ilk olarak diziyi ikiye bölüyoruz: [16, 21, 11] ve [8, 12, 22]
 *   [16, 21, 11] -> sol tarafı tekrar ikiye bölüyoruz: [16] ve [21, 11]
 *   [21, 11] -> sağ tarafı sıralı hale getiriyoruz: [11, 21]
 *   [16] ve [11, 21] -> iki parçayı birleştiriyoruz: [11, 16, 21]
 *   [8, 12, 22] -> sağ tarafı tekrar ikiye bölüyoruz: [8, 12] ve [22]
 *   [8, 12] -> sol tarafı sıralı hale getiriyoruz: [8, 12]
 *   [8, 12] ve [22] -> iki parçayı birleştiriyoruz: [8, 12, 22]
 *   [11, 16, 21] ve [8, 12, 22] -> iki sıralı parçayı birleştiriyoruz: [8, 11, 12, 16, 21, 22]
 *   Dizi sıralandıktan sonra: [8, 11, 12, 16, 21, 22]

Merge Sort algoritmasının Big-O gösterimi O(nlogn)'di
