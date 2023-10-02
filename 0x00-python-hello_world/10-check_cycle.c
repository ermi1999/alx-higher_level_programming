#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: Pointer to the head of the linked list.
 *
 * Return: 0 if no cycle is found, 1 if a cycle is found.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_loop = list;
	listint_t *fast_loop = list;

	if (list == NULL || list->next == NULL)
		return (0);

	while (fast_loop != NULL && fast_loop->next != NULL)
	{
		slow_loop = slow_loop->next;
		fast_loop = fast_loop->next->next;

		if (slow_loop == fast_loop)
			return (1);
	}

	return (0);
}
