//Logistic regression
val data = spark.textFile(...).map(readPoint).cache() //RDD
var w = Vector.random(D) //任意生成点
for (i <- 1 to ITERATIONS) {
val gradient = data.map(p =>
(1 / (1 + exp(-p.y*(w dot p.x))) - 1) * p.y * p.x
).reduce(_ + _)
w -= gradient // 角度
}
println("Final w: " + w)