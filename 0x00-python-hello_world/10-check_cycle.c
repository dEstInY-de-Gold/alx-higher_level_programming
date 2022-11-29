#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *tmp;
	int num;

	tmp = malloc(sizeof(listint_t));
	if (tmp == NULL)
		exit(0);
	tmp = list;
	while (*list)
	{
		list = list->next;
	}
}
