#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head);
listint_t *backward_list(listint_t *head);

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the list
 * Return: pointer to the new head of the reversed list
 */
listint_t *backward_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to the head of the list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		prev = slow;
		slow = slow->next;
	}

	prev->next = backward_list(slow);
	listint_t *left = *head;
	listint_t *right = prev->next;

	while (right != NULL)
	{
		if (left->n != right->n)
			return (0);

		left = left->next;
		right = right->next;
	}

	return (1);
}
