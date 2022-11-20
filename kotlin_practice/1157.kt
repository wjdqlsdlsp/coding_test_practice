fun main(){
    val input = readLine()
    val map = mutableMapOf<String, Int>()
    for (a in input!!.iterator()){
        val tmp = a.uppercase()
        if (tmp in map.keys) {
            map[tmp] = map[tmp]!! + 1
        } else {
            map[tmp] = 1
        }
    }

    var result = "?"
    var count = 0
    for(a in map.iterator()){
        if (a.value > count){
            result = a.key
            count = a.value
        } else if (a.value == count) {
            count = a.value
            result = "?"
        }
    }
    print(result)
}