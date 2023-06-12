#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - check if a list is palindrome
 * @head: pointer to the first node
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *fast, *slow, *temp, *prev = NULL;

	fast = *head;
	slow = *head;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	while (slow)
	{
		temp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = temp;
	}

	while (prev)
	{
		if ((*head)->n != prev->n)
			return (0);
		*head = (*head)->next;
		prev = prev->next;
	}
	return (1);
}
