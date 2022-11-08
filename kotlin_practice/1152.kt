fun main(){
    val str = readLine()?.split(' ')
    var count = 0
    for (tmp: String in str!!){
        if(tmp.length != 0){
            count++
        }
    }
    println(count)
}
