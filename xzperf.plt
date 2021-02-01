# replace function
# replaces string s1 by string s2 in string s
Replace(s,s1,s2) = (RP_s="", RP_n=1, (sum[RP_i=1:strlen(s)] ((s[RP_n:RP_n+strlen(s1)-1] eq s1 ? (RP_s=RP_s.s2, RP_n=RP_n+strlen(s1)) : (RP_s=RP_s.s[RP_n:RP_n], RP_n=RP_n+1)), 0)), RP_s)

set title "XZ compression"
set grid
set mxtics
set mytics
set terminal wxt
set output "D:/my/src/xzperf/xzperf.svg"
plot "D:/my/src/xzperf/xzperf.txt" using 2:1:(Replace(Replace(strcol(3), ',', '\n'), "--lzma1=", "")) with labels hypertext po pt 7 ps 1.5, "D:/my/src/xzperf/xzperf.txt" using 2:1 wi linespoints pt 7 ps 1

