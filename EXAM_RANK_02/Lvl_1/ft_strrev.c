char    *ft_strrev(char *str)
{
    if (!str)
        return (str);

    int     start = 0;
    int     end = 0;

    while (str[end])
        end++;
    end--;

    while (str[start] && start <= end)
    {
        char    temp;
        temp = str[start];
        str[start] = str[end];
        str[end] = temp;
        start++;
        end--;
    }
    return (str);
}

#include <stdio.h>

int     main(void)
{
    char    test1[] = "Salut";

    printf("%s\n", test1);
    ft_strrev(test1);
    printf("%s\n", test1);

    return (0);
}