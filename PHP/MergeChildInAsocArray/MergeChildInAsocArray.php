<?php

class MoheFuncs{
    function MergeChildInAssocArray($parent1,$parent2){
        //Get keys in only $parent2(second array).
        $Notp1Keys=array_diff_key($parent2,$parent1);
        
        //Merge the common keys betweem $parent1 and $parent2.
        foreach($parent2 as $p2Key=>$p2Value){
            foreach($parent1 as $p1Key=>&$p1Value){
                if($p2Key===$p1Key){
                    if((is_array($p2Value))&&(is_array($p1Value))){//Are the values which $parent1 and $parent2 have arrays? If not, convert to an array and merge.
                        $p1Value=array_merge($p1Value,$p2Value);
                    }else{
                        $p1Value=(is_array($p1Value)) ? $p1Value:array($p1Value);
                        $p2Value=(is_array($p2Value)) ? $p2Value:array($p2Value);
                        
                        $p1Value=array_merge($p1Value,$p2Value);
                    }
                }
            }
        }
        
        //Append keys and values in only $parent2 to $parent1.
        $parent1=(count($Notp1Keys)>0) ? $parent1+$Notp1Keys:$parent1;
        
        return $parent1;
    }
    
}


?>