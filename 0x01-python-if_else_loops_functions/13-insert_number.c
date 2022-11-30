#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>


listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *ptr;

	tmp = malloc(sizeof(listint_t));
	if (tmp == NULL)
		return (NULL);
	ptr = malloc(sizeof(listint_t));
	if (ptr == NULL)
		return (NULL);
	tmp->n = number;
	tmp->next = NULL;
	ptr = *head;
	while (ptr != NULL)
	{
		if (ptr->n >= number)
		{
			tmp = ptr;
			ptr = tmp;
		}
		ptr = ptr->next;
	}
	return (tmp);
}
