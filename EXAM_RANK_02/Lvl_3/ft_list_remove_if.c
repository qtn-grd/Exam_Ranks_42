#include <stdio.h>
#include <stdlib.h>


typedef struct s_list
{
    void            *data;
    struct s_list   *next;
}               t_list;

void ft_list_remove_if(t_list **begin_list, void *data_ref, int (*cmp)())
{
    if (!begin_list || !*begin_list)
        return;

    t_list      *temp;

    while ((*begin_list) && cmp(data_ref, (*begin_list)->data) == 0)
    {
        temp = (*begin_list)->next;
        free(*begin_list);
        *begin_list = temp;
    }
    
    t_list      *current;
    current = *begin_list;

    while (current->next)
    {        
        if(cmp(data_ref, current->next->data) == 0)
        {
            temp = current->next->next;
            free(current->next);
            current->next = temp;
        }
        else
            current = current->next;
    }
}