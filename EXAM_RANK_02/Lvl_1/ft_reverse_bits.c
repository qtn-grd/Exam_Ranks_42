#include <stdio.h>

unsigned char   reverse_bits(unsigned char octet)
{
    int             i = 8;
    unsigned char   res = 0;

    while (i--)
    {
        res = (res << 1) | (octet & 1);
        octet >>= 1;
    }
    return (res);
}

int     main(int argc, char **argv)
{
    if (argc == 2)
        printf("%d", reverse_bits(argv[1][0]));
    return (0);
}