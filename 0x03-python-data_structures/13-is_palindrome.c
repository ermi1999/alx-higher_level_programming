#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - Reverses a linked list
 * @head: Pointer to the head of the list
 * Return: Pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
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

    return prev;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to a pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return 1;

    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *second_half = NULL;
    listint_t *mid_node = NULL;
    int is_palindrome = 1;

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;

        prev = slow;
        slow = slow->next;
    }

    if (fast != NULL)
    {
        mid_node = slow;
        slow = slow->next;
    }

    second_half = slow;
    prev->next = NULL;
    second_half = reverse_list(second_half);

    listint_t *p1 = *head;
    listint_t *p2 = second_half;

    while (p1 != NULL && p2 != NULL)
    {
        if (p1->n != p2->n)
        {
            is_palindrome = 0;
            break;
        }

        p1 = p1->next;
        p2 = p2->next;
    }

    prev->next = reverse_list(second_half);

    if (mid_node != NULL)
    {
        prev->next = mid_node;
        mid_node->next = reverse_list(mid_node->next);
    }

    return is_palindrome;
}
