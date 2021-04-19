library(Rcpp)
library(V8)

src<-function(x){
  cat(paste(x, "\n", sep=""))
  Rcpp::sourceCpp(x, cacheDir='tmp') ## source c/c++ fxn
}

src("cpp/file_read.cpp") # read file

ctx <- v8()

ctx$assign("use_html", FALSE)
ctx$source("DUALuse.js")





