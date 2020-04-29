#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert node in sorted list
 * @head: head of linked list
 * @number: value
 * Return: new address of node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node1 = *head, *node2 = *head;
	listint_t *new = malloc(sizeof(listint_t));
	int i = 0;

	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (!node2 || node2->n > number)
	{
		new->next = node2;
		*head = new;
		return (new);
	}

	while (node2)
	{
		if (node2->n > number)
		{
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);
			new->n = number;
			node1->next = new;
			new->next = node2;
			return (new);
		}
		node1 = node2;
		node2 = node2->next;
		i++;
	}
	node1->next = new;
	return (new);
}
