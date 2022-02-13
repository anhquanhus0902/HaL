# 1-line comment
#=

Multiple-line comment

=#
my_name = "Anh Quan"
test_num = 21
println("Hello $my_name, age is $test_num")

# dictionary
test_dict = Dict("quan" => 19,"ha" => 22)
test_dict["nhat"] = 20
println(test_dict)
pop!(test_dict, "nhat")
println(test_dict)

# tuple
test_tuple = (4,5,6)
println(test_tuple)
println(test_tuple[2])
# tuples are immutable: test_tuple[1] = 10 throw an error

# array
test_array = [4,5,6,7]
println(test_array)
test_array[2] = 11
println(test_array)
push!(test_array, 9)
println(test_array)
pop!(test_array)
println(test_array)

# random array
#println(rand(4, 3))

# loops

# while loop

i = 0
while i < 10
    global i += 1
    print("$i ")
end
println()

i = 1
while i <= length(test_array)
    println("Num is $(test_array[i])")
    global i += 1
end 

# for loop

for i in 1:3
    println(i)
end   

for el in test_tuple
    println(el)
end    

# zeros matrix
display(zeros(3,3))
println()
# array comprehension
C = [i+j for i in 1:5, j in 1:5]
display(C)
println()
# conditional
x = 9
y = 5
# if x > y
#     println("$x is larger than $y")
# elseif x == y
#     println("$x is equal to $y")
# else
#     println("$x is smaller than $y")
# end   
(x > y) && println("$x is larger than $y")

# function
function hello(name)
    return "Hello $name"
end

println(hello("Quan"))

hello2(name) = println("Hello2 $name")
hello2("quan")

# anonymous function
hello3 = name -> println("Hi $name")
hello3("Quan")
