library(Rcpp)
library(V8)

ctx <- v8()

ctx$assign("use_html", FALSE)
ctx$source("DUALuse.js")


