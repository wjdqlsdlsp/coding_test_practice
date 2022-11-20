fun main(){
    val input = readLine()
    val arr = input?.split(" ")
    val result = arr?.get(0)!!.toInt() - arr?.get(1)!!.toInt()
    print(result)
}