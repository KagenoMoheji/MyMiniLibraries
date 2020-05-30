# MergeChildInAssocArray

## Set up
1. Download `MoheFuncs.php`.
2. Include `MoheFuncs` and Make an instance of class `MoheFuncs`.
```php
<?php
include "MoheFuncs.php";
// include_once "MoheFuncs.php";

$mf = new MoheFuncs();
?>
```
3. Call functions and use...


## Functions
### 1. MergeChildInAssocArray
- Japanese description is written in my blog below.  
[【PHP】共通キーのバリューを合併する関数を自作した](https://www.shadowmoheji.ml/article.php?link=d13)

- Because there may be not a function that can merge "child(the second)" arrays, I wrote this function.

- PHP-version
    - PHP5.2~

- Input
    1. First associated array
    2. Second associated array
- Output
    - Merged associated array

- Examples
```php
<?php
include "MoheFuncs.php";
$mf=new MoheFuncs();

//Arrays have diferent keys.
$arr1=array("a"=>1);
$arr2=array("b"=>2);
print_r($mf::MergeChildInAssocArray($arr1,$arr2));

echo "=================================\n";

//Arrays have common keys.
$arr3=array("c"=>array(0,1));
$arr4=array("c"=>array(2,3));
print_r($mf->MergeChildInAssocArray($arr3,$arr4));
?>
```
```:Result
Array
(
    [a] => 1
    [b] => 2
)
=================================
Array
(
    [c] => Array
        (
            [0] => 0
            [1] => 1
            [2] => 2
            [3] => 3
        )

)
```