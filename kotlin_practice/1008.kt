fun main(){
    val input = readLine()
    val arr = input?.split(" ")

    val num1 = arr?.get(0)?.toDouble()
    val num2 = arr?.get(1)?.toDouble()

    val result = num1!! / num2!!
    print(result)
}
