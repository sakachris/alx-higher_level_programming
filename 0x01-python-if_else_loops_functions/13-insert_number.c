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
	listint_t *temp, *add;

	add = malloc(sizeof(listint_t));
	if (!add)
		return (NULL);

	add->n = number;
	temp = *head;
	if (temp == NULL || number < temp->n)
	{
		add->next = temp;
		*head = add;
		return (add);
	}

	while (temp->next != NULL && number > temp->next->n)
	{
		temp = temp->next;
	}
	add->next = temp->next;
	temp->next = add;

	return (add);
}
