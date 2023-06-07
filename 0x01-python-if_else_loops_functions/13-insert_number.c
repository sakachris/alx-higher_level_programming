#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts node in a sorted list
 * @head: pointer to first node
 * @number: data to be added
 *
 * Return: address of inserted node
 */

listint_t *insert_node(listint_t **head, int number)
{
	unsigned int i, pos = 0;
	listint_t *t, *temp, *add;

	if (!head)
		return (NULL);

	add = malloc(sizeof(listint_t));
	if (!add)
		return (NULL);

	t = *head;
	while (t != NULL)
	{
		if (number <= temp->n)
			break;
		pos++;
		temp = temp->next;
	}

	add->n = number;

	if (pos == 0)
	{
		add->next = *head;
		*head = add;
		return (add);
	}
	else
	{
		temp = *head;
		for (i = 0; i < pos - 1; i++)
		{
			temp = temp->next;
		}
		add->next = temp->next;
		temp->next = add;
	}

	return (add);
}
