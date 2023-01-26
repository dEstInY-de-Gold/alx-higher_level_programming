#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *ptr;

	ptr = malloc(sizeof(listint_t));
	if (ptr == NULL)
	{
		printf("Malloc error!!\n");
		return (1);
	}
	while (head)
	{
		head = head->next;
	}
}
