
#Binary tree
    verilen dizi:[7, 5, 1, 8, 3, 6, 0, 9, 4, 2]

Başlangıçta ağaç boş olduğu için ilk olarak 7 kök eleman olarak eklenir.
* 5, kökün soluna eklenir:
* 1, kökün soluna eklenir:
* 8, kökün sağına eklenir:
* 3, 5'in soluna eklenir:
* 6, 5'in sağına eklenir:
* 0, 1'in soluna eklenir:
* 9, 8'in sağına eklenir:
* 4, 3'ün sağına eklenir:
* 2, 3'ün soluna eklenir:

** Ağaç tamamlandıktan sonra inorder olarak gezersek: 0, 2, 3, 4, 5, 6, 7, 8, 9, 1 şeklinde elemanlar sıralanır.

Ağacın son hali şu şekildedir:

Copy code
              7
            /   \
           /     \
          5       1
         / \     / \
        3   6   N   8
       / \     
      0   4   
     /
    2