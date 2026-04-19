#include <stdlib.h>
#include <stdio.h>

int     ft_absolute(int nbr)
{
    if (nbr < 0)
        nbr *= -1;
    return (nbr);
}

int     *ft_range(int start, int end)
{
    int     *array;
    int     i;
    int     size;
    
    i = 0;
    size = ft_absolute(end - start);
    array = malloc(sizeof(int) * (size + 1));
    if (!array)
        return (NULL);
    if (start <= end)
    {
        while (i <= size)
        {
            array[i] = start;
            i++;
            start++;
        }
    }
    if (end < start)
    {
        while (i <= size)
        {
            array[i] = start;
            i++;
            start--;
        }
    }
    return (array);
}

// int     main(void)
// {
//     int     i;
//     int     *array;
    
//     i = 0;
//     array = ft_range(-2, -5);
//     while (i < 11)
//     {
//         printf("%d\n", array[i]);
//         i++;
//     }
//     return (0);
// }
