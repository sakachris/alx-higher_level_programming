#include "lists.h"

/**
 * check_cycle - checks for a cycle in a linked list
 * @list: list to check
 *
 * Return: 1 if found, 0 if not found
 */

int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	if (list == NULL)
		return (0);

	slow = list;
	fast = list->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
