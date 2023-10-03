#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - inserts a new node into a sorted singly linked list
 * @head: a double pointer to the head of the list
 * @number: the number to be inserted
 *
 * Return: the address of the new node, or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode = malloc(sizeof(listint_t));

	if (newNode == NULL)
	{
		return (NULL);
	}

	newNode->n = number;

	if (*head == NULL || (*head)->n >= newNode->n)
	{
		newNode->next = *head;
		*head = newNode;
	}
	else
	{
		listint_t *current = *head;

		while (current->next != NULL && current->next->n < newNode->n)
		{
			current = current->next;
		}
		newNode->next = current->next;
		current->next = newNode;
	}

	return (newNode);
}
