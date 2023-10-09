#include "lists.h"

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (*head);

	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return (*head);
}

/**
 * get_middle - Finds the middle node of a linked list.
 * @head: A pointer to the head of the linked list.
 *
 * Return: A pointer to the middle node.
 */
listint_t *get_middle(listint_t *head)
{
	listint_t *slow = head;
	listint_t *fast = head;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	return (slow);
}

/**
 * compare_lists - Compares two linked lists for equality.
 * @list1: A pointer to the head of the first linked list.
 * @list2: A pointer to the head of the second linked list.
 *
 * Return: 1 if the lists are equal, 0 otherwise.
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return 0;

		list1 = list1->next;
		list2 = list2->next;
	}

	return (list1 == NULL && list2 == NULL);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *mid = NULL;
	listint_t *second_half = NULL;

	mid = get_middle(*head);
	second_half = mid->next;
	mid->next = NULL;

	reverse_listint(&second_half);

	int is_palindrome = compare_lists(*head, second_half);

	reverse_listint(&second_half);
	mid->next = second_half;

	return (is_palindrome);
}
