fun main(){
    val str = readLine()?.split(" ")
    println("${str?.get(0)?.toInt()?.plus(str?.get(1)?.toInt()!!)}")
}
