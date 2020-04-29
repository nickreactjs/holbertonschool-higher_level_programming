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
	listint_t *node1 = *head, *node2 = *head, *new = NULL;
	int i = 0;

	while (node2)
	{
		if (node2->n > number)
		{
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);
			new->n = number;
			if (node1->n > number)
			{
				new->next = node1;
				return (new);
			}
			node1->next = new;
			new->next = node2;
			return (new);
		}
		node1 = node2;
		node2 = node2->next;
		i++;
	}
	return (add_nodeint_end(head, i));
}
