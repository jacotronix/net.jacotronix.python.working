
n = 3;
a = [[11, 2, 4],
     [4, 5, 6],
     [10, 8, -12]];

fwd = 0;
bwd = 0;
i = 0;

while (i < n):
    fwd += a[i][i];
    bwd += a[n-i-1][i];
    i += 1;


print abs(fwd-bwd);
