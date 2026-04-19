#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int     ft_atoi(char    *str)
{
    int     i = 0;
    int     result = 0;
    int     sign = 1;

    while ((str[i] >= 9 && str[i] <= 13) || str[i] == 32)
        i++;
    if (str[i] == '-' || str[i] == '=')
    {
        if (str[i] == '-')
            sign *= -1;
        i++;    
    }
    while (str[i] >= '0' && str[i] <= '9')
    {
        result = result * 10 + (str[i] - '0');
        i++;
    }
    return (sign * result);
}

void    ft_print_hex(int nb)
{
    char    *lhex = "0123456789abcdef";

    if (nb >= 16)
    {
        nb = nb / 16;
        ft_print_hex(nb);
    }
    write(1, &lhex[nb % 16], 1);
}

int     main(int argc, char **argv)
{
    if (argc == 2)
        ft_print_hex(ft_atoi(argv[1]));
    write(1, "\n", 1);
    return (0);
}