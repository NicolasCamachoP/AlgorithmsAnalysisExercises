set terminal png

l(x)=a1*x + a0
p(x)=a2*x*x + a1*x + a0
c(x)=a3*x*x*x + a2*x*x + a1*x + a0

set output "Bubble.png"
set title "BubbleSort timing"
set xlabel "Size (n)"
set ylabel "Time (s)"
fit p(x) "data.res" using 1:2 via a2, a1, a0
plot "data.res" using 1:2 with lines notitle, p(x)

set output "Insertion.png"
set title "InsertionSort timing"
set xlabel "Size (n)"
set ylabel "Time (s)"
plot "data.res" using 1:3 with lines notitle

set output "Quick.png"
set title "QuickSort timing"
set xlabel "Size (n)"
set ylabel "Time (s)"
plot "data.res" using 1:4 with lines notitle

## eof - create_figs.gnuplot
