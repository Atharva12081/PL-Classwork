list1 = ["apple", "banana", "cherry"]
list2 = [1,2,3]

#add
list1.append("pineapple")
list1.insert(2, "orange")
list1.extend(["mango", "grape"])

#modify
list2[3] = 60 
list2[1:3] = [20, 30, 40]

#remove
list1.remove("banana")
list1.pop(3) 
list1.clear()

#sort
list1.sort()
list2.sort(reverse=True)


set1 = {"1", "2", "3"}
set2 = {"3", "4", "2"}

set1|set2 #union
set1.union( set2 )

set1&set2 #intersection
set1.intersection( set2 )

set1-set2 #difference
set1.difference( set2 )

set1-set2 #symmetric differenc
set1.symmetric_difference( set2 )

set1.add("5")
set1.remove("2")
set1.discard("10")
set1.pop()
set1.clear()
set1.update( {"6", "7"} )


list1 = ["apple", "banana", "cherry"]
list2 = [1,2,3] 
set1 = {"1", "2", "3"}
set2 = {"3", "4", "2"}


